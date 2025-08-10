import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.tools import Tool
from openalex import fetch_openalex_papers

load_dotenv()


llama_llm = ChatGroq(
    model="llama3-8b-8192",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.7
)




# Tool no. 1 : OpenAlex Paper Fetcher
openalex_tool = Tool(
    name="OpenAlexPaperFetcher",
    func=lambda q: fetch_openalex_papers(q, max_count=5),
    description="Fetches top relevant academic papers from OpenAlex for a given topic."
)







idea_prompt = ChatPromptTemplate.from_template("""
You are an AI research advisor.
Based on the following recent papers in {field}, do the following:
1. Identify emerging trends and gaps.
2. Suggest 3 innovative, feasible research ideas for a(n) {experience_level} researcher.
3. For each idea, include:
- Title
- Rationale
- Skills/knowledge required

Recent Papers:
{paper_list}
""")

idea_chain = LLMChain(llm=llama_llm, prompt=idea_prompt)

def generate_ideas_with_papers(field, experience_level="expert"):
    papers = fetch_openalex_papers(field, max_count=5)
    if not papers:
        return "No relevant recent papers found."
    paper_list = "\n".join(
        f"{i+1}. {p['title']} - {p['authors']} ({p['year']})\nAbstract: {p['abstract']}"
        for i, p in enumerate(papers)
    )
    return idea_chain.run(field=field, experience_level=experience_level, paper_list=paper_list)






# Tool no. 2 : Research Idea Generator
idea_tool = Tool(
    name="ResearchIdeaGenerator",
    func=lambda q: generate_ideas_with_papers(q, "expert"),
    description="Generates novel, grounded research ideas in a field using recent papers."
)








gap_prompt = ChatPromptTemplate.from_template("""
You are an experienced research analyst.
You will be given recent papers in the field {field}.
From these, extract:
1. Key emerging concepts and trends
2. Major research gaps or underexplored areas
3. Potential directions for further investigation

Papers:
{paper_list}

Answer in an academic tone.
""")



gap_chain = LLMChain(llm=llama_llm, prompt=gap_prompt)

def analyze_research_gaps(field):
    papers = fetch_openalex_papers(field, max_count=5)
    if not papers:
        return "No relevant papers found."
    paper_list = "\n".join(
        f"{i+1}. {p['title']} - {p['authors']} ({p['year']})\nAbstract: {p['abstract']}"
        for i, p in enumerate(papers)
    )
    return gap_chain.run(field=field, paper_list=paper_list)



# Tool no. 3 : Research Gap Analyzer
gap_analysis_tool = Tool(
    name="ResearchGapAnalyzer",
    func=lambda q: analyze_research_gaps(q),
    description="Analyzes recent papers in a field to find trends and research gaps."
)







# Tool no. 4 : Key Phrase Extractor

phrase_prompt = ChatPromptTemplate.from_template("""
Extract the most relevant key phrases, technical terms, and named entities
from the following research paper abstracts:

{paper_list}

Only output comma-separated phrases.
""")

phrase_chain = LLMChain(llm=llama_llm, prompt=phrase_prompt)

def extract_key_phrases(field):
    papers = fetch_openalex_papers(field, max_count=5)
    if not papers:
        return "No relevant papers found."
    paper_list = "\n".join(f"{p['title']}\nAbstract: {p['abstract']}" for p in papers)
    return phrase_chain.run(paper_list=paper_list)

phrase_extractor_tool = Tool(
    name="KeyPhraseExtractor",
    func=lambda q: extract_key_phrases(q),
    description="Extracts key phrases from recent papers in a given research field."
)
