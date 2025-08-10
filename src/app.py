from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from agent import agent

app = FastAPI(title="AI Research Assistant Agent API")

class ResearchRequest(BaseModel):
    domain_name: str
    experience_level: str = "expert"

@app.post("/research-ideas")
async def get_research_ideas(req: ResearchRequest):
    domain_name = req.domain_name.strip()
    experience_level = req.experience_level.strip() or "expert"

    if not domain_name:
        raise HTTPException(status_code=400, detail="domain_name is required")

    query = f"""Fetch Recent Papers on Openalex about {domain_name}, find research gaps in the current workflow and generate novel research ideas for a {experience_level} researcher
            The output should have the following format:
                1. Novel Research Idea 1
                   1.2 description about the ideas:
                   1.3 skills required:
                2. Novel Research Idea 2
                     2.2 description about the ideas:
                     2.3 skills required:
                3. Novel Research Idea 3
                     3.2 description about the ideas:
                     3.3 skills required:

                Research Gaps:
                1. Gap 1
                2. Gap 2
                3. Gap 3
            """

    try:
        response = agent.run(query)
        return {"result": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")

