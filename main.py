import os
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents = 'Why does the universe keep expanding and what will happen in the future? 2 paragraphs.'
)

print(response.text)