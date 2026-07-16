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

promp1="hi"
promp2="explain token in details"
promp3="write a 1000 word essay on machine learning"

prompts=[promp1,promp2,promp3]
for prompt in prompts:
    message={
    "role":role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=50)
    usage=response.usage
    print(f"prompt: {prompt}->your tokens:{usage.prompt_tokens}. completion tokens: {usage.completion_tokens} Total tokens:{usage.total_tokens} Finish reason:{response.choices[0].finish_reason}")
