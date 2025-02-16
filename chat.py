from openai import OpenAI
from dotenv import load_dotenv
import os

#importation de l'API
load_dotenv()
api_key = os.getenv("API_KEY")


def main():
    with open("prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    client = OpenAI(
        base_url="https://api.scaleway.ai/488b2cbb-38e3-4cdb-ac85-7aef7f019264/v1",
        api_key="d67906c0-c6ba-4db9-bbf3-fbc34adf6d21"  # Remplace avec ta clé API IAM
    )

    chat_history = [{"role": "system", "content": system_prompt}]
    
    # Première requête à l'IA
    response = client.chat.completions.create(
        model="llama-3.3-70b-instruct",
        messages=chat_history,
        max_tokens=2048,
        temperature=0.7,
        top_p=0.7,
        presence_penalty=0,
        stream=True,
    )
    
    print("Chatbot : ", end="")
    bot_response = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            bot_response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()
    
    chat_history.append({"role": "assistant", "content": bot_response})
    
    while True:
        user_input = input("Vous : ")
        if user_input.lower() == "exit":
            print("Chatbot : Au revoir !")
            break
        
        chat_history.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="llama-3.3-70b-instruct",
            messages=chat_history,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.7,
            presence_penalty=0,
            stream=True,
        )
        
        print("Chatbot : ", end="")
        bot_response = ""
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                bot_response += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()
        
        chat_history.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    main()