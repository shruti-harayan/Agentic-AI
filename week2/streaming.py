import os
from time import sleep
from dotenv import load_dotenv
from groq import Groq
import re

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key Not found")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

prompt="explain how internet works."
messages=[{"role":"user","content":prompt}]

#without streaming
# response=client.chat.completions.create(model=model,messages=messages)      
# answer=response.choices[0].message.content
# print(answer)

#with streaming
response=client.chat.completions.create(model=model,messages=messages,stream=True)
for chunk in response:
    content=chunk.choices[0].delta.content
    if content:
        print(content,end="",flush=True)