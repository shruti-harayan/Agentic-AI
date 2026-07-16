import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
	raise ValueError("api error")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"
role="user"
prompt="Do you know Agentic AI"
message={
"role":role,
"content":prompt
}
messages=[message]
response=client.chat.completions.create(model=model,messages=messages)
print(response)

print("##########################################################")
ans=response.choices[0].message.content
print(ans)