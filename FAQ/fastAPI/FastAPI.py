from fastapi import FastAPI # type: ignore

from fastapi.middleware.cors import CORSMiddleware

import ast
import json
import knowledge
from knowledge import Knowledge
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],  # Allow frontend (change the origin if necessary)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
@app.get("/ask-her/") # type: ignore
async def ask_her(question: str):
    # Initialize the Knowledge object
    knowledge_obj = Knowledge()
    
    # Get the answer using the Knowledge object
    answer = knowledge_obj.getAnswer(question)
    
    # Return the response as a JSON object
    return {"answer": answer}