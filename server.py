from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from api import get_api
from to_pdf import to_pdf
# from sse_starlette.sse import EventSourceResponse
from openai import OpenAI
from pydantic import BaseModel
from loguru import logger
import os

app = FastAPI()

logger.add("logs/app.log", rotation="1 day", retention="7 days", compression="zip")

logger.info("Application has started.")


API_KEY=get_api()
# Serve static files (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

with open("prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

client = OpenAI(
    base_url="https://api.scaleway.ai/488b2cbb-38e3-4cdb-ac85-7aef7f019264/v1",
    api_key=API_KEY
)

class ChatRequest(BaseModel):
    message: str
    chat_history: list

@app.get("/")
def read_root():
    logger.info("Loading Home Page.")
    return FileResponse("static/index.html")
    
    
@app.post("/chat")
async def chat(request: ChatRequest):
    logger.info(API_KEY)
    logger.info("Posting Chat.")

    if not request.chat_history:
        logger.info("Chatting For the 1st Time.")
        chat_history = [{"role": "system", "content": system_prompt}]
    else:
        chat_history = request.chat_history
        chat_history.append({"role": "user", "content": request.message})

    logger.info("Calling qwen.")

    # Prepare a generator for streaming the response to the client
    response = client.chat.completions.create(
        model="qwen2.5-coder-32b-instruct",
        messages=chat_history,
        max_tokens=512,
        temperature=0.25,
        top_p=1,
        presence_penalty=0,
        stream=False,
    )

    logger.info("Posting Chat.")

    bot_response = response.choices[0].message.content
    if "END_DATA_COLLECTION" in bot_response:
        to_pdf(bot_response)

    chat_history.append({"role": "assistant", "content": bot_response})
    return {"response": bot_response, "chat_history": chat_history}