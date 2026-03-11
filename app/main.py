from fastapi import FastAPI, Query
from app.llm import generate_answer, generate_ollama_answer

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"} # Dictionary

@app.get("/ask")
def ask(question: str = Query(...)):
    return {"answer": generate_answer(question)}

@app.get("/ollama")
def ask(question: str = Query(...)):
    return {"answer": generate_ollama_answer(question)}