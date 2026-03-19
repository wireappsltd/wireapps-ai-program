from anthropic import Anthropic
from openai import OpenAI
from app.settings import settings
from ollama import chat

anthropic = Anthropic(api_key=settings.ANTHROPIC_API_KEY)
openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(question: str):
  response = anthropic.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
      {
        "role": "user",
        "content": question
      }
    ]
  )

  return response.content[0].text

def generate_openai_answer(question: str):
  response = openai_client.chat.completions.create(
    model="gpt-4o",
    max_tokens=1000,
    messages=[
      {
        "role": "user",
        "content": question
      }
    ]
  )

  return response.choices[0].message.content

def get_system_promot_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

def generate_ollama_answer(question: str):
    system_prompt = get_system_promot_content("app/prompts/system_prompt.md")
    
    response = chat(model="gemma3:4b", messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": question}])

    return response.message.content