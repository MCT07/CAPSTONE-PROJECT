

from fastapi import FastAPI

app = FastAPI()

enterprise_resources = {
    "policy": "Enterprise AI responses must follow governance policies.",
    "rag": "RAG retrieves enterprise context from Azure AI Search."
}

@app.get("/resource/{name}")
def get_resource(name: str):

    return {
        "resource": enterprise_resources.get(name, "Not Found")
    }

@app.get("/tool/calculator")
def calculator(expression: str):

    return {
        "result": f"Executed expression: {expression}"
    }


