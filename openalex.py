import requests
import time

def fetch_openalex_papers(query: str, max_count: int = 10, timeout: int = 10, retries: int = 3):
    """
    Fetches top papers from OpenAlex based on a query.
    Returns a list of dicts with title, abstract (reconstructed), authors, year.
    """
    url = "https://api.openalex.org/works"
    params = {
        "search": query,
        "per-page": max_count,
        "sort": "relevance_score:desc",
    }
    headers = {
        "User-Agent": "YourAppName/1.0 (your-email@example.com)"  # OpenAlex requires this
    }

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            break
        except Exception as e:
            print(f"OpenAlex API error on attempt {attempt+1}: {e}")
            time.sleep(2)
    else:
        return []

    papers = []
    for item in data.get("results", []):
        # Reconstruct abstract if available
        abstract_idx = item.get("abstract_inverted_index")
        if abstract_idx:
            words = [""] * (max(pos for positions in abstract_idx.values() for pos in positions) + 1)
            for word, positions in abstract_idx.items():
                for pos in positions:
                    words[pos] = word
            abstract = " ".join(words)
        else:
            abstract = item.get("abstract") or ""

        authors_list = item.get("authorships", [])
        authors = ", ".join(a["author"]["display_name"] for a in authors_list) if authors_list else "Unknown"

        papers.append({
            "title": item.get("title", "No title"),
            "abstract": abstract,
            "authors": authors,
            "year": item.get("publication_year", "Unknown"),
        })

    return papers
