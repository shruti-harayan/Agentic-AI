import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
	raise ValueError("api error")

client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

def llm_ans(prompt):
	message={
		"role":"user",
		"content":prompt
	}
	messages=[message]
	response=client.chat.completions.create(model=model,messages=messages)

	ans=response.choices[0].message.content
	return ans

example_prompt="""
#ROLE
You are a support assistant at a mobile/laptop company.

#TASK
You have to classify the issue in a category.


#CONSTRAINT
You have to classify the issue in one of the three categories namely billing,technical or return.

#OUTPUT FORMAT
Your answer should be in one word only. The one word should be from one of the categories.

#EXAMPLE
For instance if a user complain says he wants a refund then the category should be return.

#FALLBACK
If the issue is unrelated to any of the categories mentioned in the constraints then the answer should be OTHER.

This is a user complaint: My laptop is not working.
"""

print(llm_ans(example_prompt))