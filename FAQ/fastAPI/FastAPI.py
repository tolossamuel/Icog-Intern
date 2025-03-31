from fastapi import FastAPI ,Request, HTTPException, status
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import os
import ast
import json
import knowledge
import requests
from hyperon import *
from knowledge import Knowledge
from metta_knowledge import metta_knowledge
app = FastAPI()
metta  = MeTTa()
mettaKnowledge = metta.run( # type: ignore
            metta_knowledge
        )
global admin_state
admin_state = 0
global graph
graph = ["CV", "Greeting","Meeting", "Responsibility","Mentor","Mentor-Change",
        "Training","Performance-Evaluation","Communication","Key-Contacts", "Work-Ethics","Leave-Policy","Internship-Completion",
        "Hello","Goodbye","help","HR-Query","HR-Response","start","contact","Apply-Internship","Working-Hours",
        "Office-Hours","Icong-Lab-Location","Internship-Opportunity","Internship-Feedback","Internship-Training",
        "Evaluation","Evaluation-Grouping"]
global knowledge_obj
knowledge_obj = Knowledge(graph)
app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
def send_telegram_message(chat_id: int, answer: str, admin=False):
    global knowledge_obj
    load_dotenv()
    api_key = os.getenv("tg_token")
    
    token = api_key 
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    if admin and admin_state == 0:
            keyboard = {
                "inline_keyboard": [
                    [{"text": "➕ Add Knowledge", "callback_data": "add_knowledge"}],
                    [{"text": "❌ Remove Knowledge", "callback_data": "remove_knowledge"}]
                ]
            }
            payload = {
                "chat_id": chat_id,
                "text": answer,
                "reply_markup": json.dumps(keyboard)
            }
            response = requests.post(url, data=payload)
            return response
        
    
    payload = {
        "chat_id": chat_id,
        "text": answer
    }
    response = requests.post(url, data=payload)
    return response
async def adminFunction(datas):
    global knowledge_obj
    global admin_state
    userId = datas['from']['id']
    text = datas.get('data','')
    chatId = datas["message"]["chat"]["id"]
    if (text == "add_knowledge"):
        if admin_state == 0:
            admin_state = 1
            message = "Send the key word for the knowlege"
            
            send_telegram_message(chat_id=chatId,answer = message,admin=True)
        elif admin_state == 1:
            admin_state = 2
            message = "send the detail description based on ICOG-Lab domain knowledge"
            send_telegram_message(chat_id=chatId,answer=message, admin=True)
    else:
        message = "comming soon"
        send_telegram_message(chat_id=chatId, answer= message, admin=True)
    return datas
   
@app.post("/ask-hr/")
async def ask_her_post(request: Request):
    global admin_state
    global knowledge_obj
    global graph
    load_dotenv()
    tg_admin_id = os.getenv("tg_admin_id")
    
    data = await request.json()
  
    if ("callback_query" in data):
        await adminFunction(data["callback_query"])  # Awaiting the async admin function to avoid warnings
        return {"status": "ok"}
    
    userId = data["message"]["from"]["id"]
    if "message" in data and "text" in data["message"]:
        question = data["message"]["text"]
    else:
        return {"error": "Invalid request"}
    chat_id = data["message"]["chat"]["id"]
   
    question = data.get("message", {}).get("text")
    
    if not question:
        return {"error": "Invalid request, no text in message"}
    if str(userId) == str(tg_admin_id):
        if question == "/start":
            answer = "Hello Icog-Lab HR, what can I help you with?"
            send_telegram_message(chat_id, answer, admin=True) 
            
        else:
            val = knowledge_obj.extractAndAddKnowledge(question)
            
            send_telegram_message(chat_id, val, admin=True)
        return {"status": "ok"}
    
    answer = knowledge_obj.getAnswer(question)
   
    
    
    send_telegram_message(chat_id, answer)

    return {"status": "ok", "answer": answer}

@app.get("/ask-hr/") # type: ignore
async def ask_her(question: str):
    # Initialize the Knowledge object
    knowledge_obj = Knowledge(graph)
    
    # Get the answer using the Knowledge object
    answer = knowledge_obj.getAnswer(question)
    
    # Return the response as a JSON object
    return {"answer": answer}