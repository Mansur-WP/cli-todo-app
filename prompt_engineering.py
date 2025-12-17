import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    system_instruction="""
Convert user text into a task title.

Examples:
Input: buy food tomorrow
Output: Buy food

Input: finish python assignment tonight
Output: Finish Python Assignment

Input: call the lecturer in the morning
Output:
"""
)

prompt = input("Ask Gemini: ")
response = model.generate_content(prompt)

print("\n🤖 Gemini:")
print(response.text)
