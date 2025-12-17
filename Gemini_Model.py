import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")

prompt = input("Ask Gemini something: ")

response = model.generate_content(prompt)

print("\n🤖 Gemini Response:")
print(response.text)
