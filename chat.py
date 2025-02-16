from timeout import *
from openai import OpenAI

def get_report(API_KEY):
    with open("prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    client = OpenAI(
        base_url="https://api.scaleway.ai/488b2cbb-38e3-4cdb-ac85-7aef7f019264/v1",
        api_key=API_KEY
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
    
    print("Assistant Doctolib : ", end="")
    bot_response = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            bot_response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()
    
    chat_history.append({"role": "assistant", "content": bot_response})
    
    while True:
        start_counter()
        user_input = input("... ")
        if user_input:
            stop_counter() #le patient a émis une réponse

        if user_input.lower() == "exit":
            print("Debug pour dev.")
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
        
        
        print("Assistant Doctolib : ", end="")
        bot_response = ""
        for chunk in response:
            if chunk.choices and chunk.choices[0].delta.content:
                bot_response += chunk.choices[0].delta.content
                print(chunk.choices[0].delta.content, end="", flush=True)
        print()
        
        chat_history.append({"role": "assistant", "content": bot_response})

