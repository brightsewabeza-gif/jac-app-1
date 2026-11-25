import anvil.server
import requests

API_BASE_URL = "https://sisters-elements-housewares-auckland.trycloudflare.com"


@anvil.server.callable
def search_web(query):
    query = str(query).strip()

    if not query:
        return {
            "engine": "JAC APP",
            "query": query,
            "total_results": 0,
            "results": []
        }

    response = requests.get(
        API_BASE_URL + "/search",
        params={"q": query},
        timeout=20
    )

    response.raise_for_status()

    return response.json()
