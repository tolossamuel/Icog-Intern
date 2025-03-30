from fastapi import FastAPI ,Request, HTTPException, status
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
import ast
import json
import knowledge
import requests
from knowledge import Knowledge
app = FastAPI()
app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
def send_telegram_message(chat_id: int, answer: str):
    load_dotenv()
    api_key = os.getenv("tg_token")
    token = api_key  # Replace with your actual Telegram bot token
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": answer
    }
    response = requests.post(url, data=payload)
    return response
@app.post("/ask-hr/")
async def ask_her_post(request: Request):
    data = await request.json()
    if "message" in data and "text" in data["message"]:
        question = data["message"]["text"]
    else:
        return {"error": "Invalid request"}
    
    
    knowledge_obj = Knowledge()
    answer = knowledge_obj.getAnswer(question)
    chat_id = data["message"]["chat"]["id"]
    send_telegram_message(chat_id, answer)

    return {"status": "ok", "answer": answer}

@app.get("/ask-hr/") # type: ignore
async def ask_her(question: str):
    # Initialize the Knowledge object
    knowledge_obj = Knowledge()
    
    # Get the answer using the Knowledge object
    answer = knowledge_obj.getAnswer(question)
    
    # Return the response as a JSON object
    return {"answer": answer}