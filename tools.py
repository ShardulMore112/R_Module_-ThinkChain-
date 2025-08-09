from langchain.tools import Tool
from openalex import fetch_openalex_papers  # import your fetch function

def openalex_tool_func(query: str) -> str:
    papers = fetch_openalex_papers(query, max_count=10)
    if not papers:
        return "No papers found or error occurred."

    output_lines = []
    for i, p in enumerate(papers, 1):
        output_lines.append(
            f"{i}. {p['title']} ({p['year']})\n"
            f"Authors: {p['authors']}\n"
            f"Abstract: {p['abstract']}\n"
        )
    return "\n".join(output_lines).strip()

openalex_tool = Tool(
    name="OpenAlexPaperFetcher",
    func=openalex_tool_func,
    description="Fetches top research papers from OpenAlex by keyword, returns titles, authors, years, and abstracts.",
)
