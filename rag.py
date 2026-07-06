
import requests

search_endpoint = "<SEARCH-ENDPOINT>"
search_key = "<SEARCH-KEY>"
index_name = "<search-1783358606507"

def search_documents(query):


    url = f"{search_endpoint}/indexes/{index_name}/docs/search?api-version=2024-07-01-Preview"

    headers = {
        "Content-Type": "application/json",
        "api-key": search_key
    }

    data = {
        "search": query,
        "top": 3
    }

    response = requests.post(
        url,
        headers=headers,
        json=data
    )

    results = response.json()

    if "value" not in results:
        return []

    return [doc.get("chunk", "") for doc in results["value"]]
