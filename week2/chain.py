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

JD="""  
We are hiring Python Backend Developer
Requirements:python, fastapi, sql, docker, AWS
2+ years of experience 
"""
Resume=""" 
Name: Shruti Harayan
Experience: 1 year of experience as software engineer
skills: python, sqlite, fastapi, aws
Projects:Build full stack grading management system using fastapi as backend
"""
def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role":"system",
        "content":system_prompt
    }
    user_msg={
        "role":"user",
        "content":user_prompt
    }
    messages=[sys_msg,user_msg]
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_res_extract():
    system_prompt="You are a resume parser. You will be given a resume and you need to extract only Skills from it. Do not include any other information."
    user_prompt=f"Resume: {Resume}"
    return ask_llm(system_prompt,user_prompt)

def step2_jd_extract():
    system_prompt="You are a job description parser. You will be given a job description and you need to extract only Skills from it. Do not include any other information."
    user_prompt=f"Job Description: {JD}"
    return ask_llm(system_prompt,user_prompt)

def step3_compare_skills(resume_skills,jd_skills):
    system_prompt="You are a skill matcher. You will be given two sets of skills, one from a resume and one from a job description. You need to compare the two sets and produce a match score between 0 and 100, where 100 means all skills match and 0 means no skills match. Also provide a short verdict whether the candidate is a good fit."
    user_prompt=f"Resume Skills: {resume_skills}\nJob Description Skills: {jd_skills}"
    return ask_llm(system_prompt,user_prompt)

candidate_skills=step1_res_extract()

job_skills=step2_jd_extract()

score=step3_compare_skills(candidate_skills,job_skills)
print("Candidate Skills:", candidate_skills)
print("Job Description Skills:", job_skills)
print("Match Score:", score)
