import google.genai as genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

class AIEngine:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is not found in the environment")
        self.client = genai.Client(api_key=api_key)

    async def generate_solution(self, prompt:str):
        try:
            response = self.client.models.generate_content(model="gemini-2.5-flash-lite",contents=types.Part.from_text(text=prompt))
            return response
        
        except Exception as e:
            print(f"Error: {e}")
            raise e
        
    def list_models(self):
        return self.client.models.list()
    
ai_engine = AIEngine()