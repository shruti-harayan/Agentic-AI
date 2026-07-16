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
prompt="suggest me 3 names for my AI startup"

message_system={
	"role":"system",
	"content":"you are a brand strategist. Answer in one word"
}
message={
"role":role,
"content":prompt
}
messages=[message_system,message]
response=client.chat.completions.create(model=model,messages=messages,temperature=0)
#print(response)

print("##########################################################")
ans=response.choices[0].message.content
print(ans)