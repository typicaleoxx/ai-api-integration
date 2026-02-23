# This program shows us how we can integrate AI models using API keys to generate text based response
from google import genai
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is missing from .env")

user_question = input("Please enter your question to genAI: ")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=user_question
    + "please answer and explain simple words i want to learn everything about it, its content. please cover what when where how why all of it",
)
print(response.text)
