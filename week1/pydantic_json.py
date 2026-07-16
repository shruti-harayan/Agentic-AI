import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
	raise ValueError("api error")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"

#to structure LLM output
from pydantic import BaseModel
class Ticket(BaseModel):
	name:str
	email:str
	contact:int
	issue:str

schema=Ticket.model_json_schema()
response_format={
	"type":"json_object"
}

system_prompt=f""" Extract personal information from the ticket strictly based on this schema {schema} and give output in json format"""

message_system={
	"role":"system",
	"content":system_prompt
}

text="Hello, my name is shruti. I have an issue with my laptop it is not working . My email is shruti@gmail.com and i live in mumbai. my contact no. is 1234567890"

prompt=f""" This is a customer ticket. please extract personal information from this {text} """

message={
"role":role,
"content":prompt
}
messages=[message_system,message]

response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)

ans=response.choices[0].message.content
print(ans)

print("##################################")

#how to read the output
import json
raw_json=ans
data=json.loads(raw_json)
ticket=Ticket(**data)

print(ticket.name)
print(ticket.email)
print(ticket.contact)
print(ticket.issue)