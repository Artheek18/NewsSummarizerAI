from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
model = init_chat_model(
    model="gemini-3-flash-preview",
    model_provider="google-genai",
    api_key=google_api_key)

response = model.invoke("Are dogs stronger than cats?")
print(response.content[0]['text'])