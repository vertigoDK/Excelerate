from langchain_google_genai import GoogleGenerativeAI
from app.core.config import settings


class BaseLLM:
    def __init__(self):
        self.llm = GoogleGenerativeAI(model=settings.GOOGLE_GENAI_MODEL, api_key=settings.GOOGLE_API_KEY)

    def generate_response(self, prompt):
        return self.llm.invoke(prompt)