
from rag import search_documents
from governance import validate_output, guardrails_check

shared_memory = []

def planner_agent(query):

    if "search" in query.lower():
        return "RAG"

    return "GENERAL"


def executor_agent(query):

    task = planner_agent(query)

    shared_memory.append({
        "query": query,
        "task": task
    })

    if task == "RAG":

        docs = search_documents(query)

        return "\n".join(docs)

    return "General response"


def governance_agent(response):

    if not validate_output(response):
        return "Invalid response"

    if not guardrails_check(response):
        return "Blocked by governance"

    return response

