from fastapi import FastAPI # type: ignore

from fastapi.middleware.cors import CORSMiddleware

import ast
import json
import knowledge
from knowledge import Knowledge
app = FastAPI()
app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],  # Allows all domains
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
@app.get("/ask-hr/") # type: ignore
async def ask_her(question: str):
    # Initialize the Knowledge object
    knowledge_obj = Knowledge()
    
    # Get the answer using the Knowledge object
    answer = knowledge_obj.getAnswer(question)
    
    # Return the response as a JSON object
    return {"answer": answer}