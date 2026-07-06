
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AzureOpenAI

from orchestrator import executor_agent, governance_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

endpoint = "<OPENAI-ENDPOINT>"
key = "<OPENAI-KEY>"
deployment = "chat-model"

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint=endpoint,
    api_key=key,
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):

    retrieved_context = executor_agent(request.message)

    context = "\n".join(
        retrieved_context
        if isinstance(retrieved_context, list)
        else [retrieved_context]
    )

    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {
                "role": "system",
                "content": "Answer only using provided context."
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion:\n{request.message}"
            }
        ],
        max_completion_tokens=300
    )

    answer = response.choices[0].message.content

    final_answer = governance_agent(answer)

    return {
        "response": final_answer
    }

