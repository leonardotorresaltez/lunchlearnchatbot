import openai
import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) #read local .env file
openai.api_key=os.getenv('OPENAI_API_KEY')
messages = []
system_message = "Eres un asistente divertido y responde con bromas a las preguntas del usuario"
messages.append({"role":"system","content":system_message})


exit_conditions = (":q", "quit", "exit")
while True:
    query = input("usuario>> ")
    if query in exit_conditions:
        break
    else:
        
        messages.append({"role":"user","content": query})
        response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
        print("chatbot>> "+ response["choices"][0]["message"]["content"])


