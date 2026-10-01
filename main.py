from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from google import genai
import json

app = FastAPI()

class WritingRequest(BaseModel):
    topic: str
    essay: str
    api_key: str
    cefr: str


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)



@app.get("/")
def home():
    return FileResponse("templates/writing.html")


@app.post("/submit")
def submit(request: WritingRequest):

    client = genai.Client(
        api_key=request.api_key
    )

    prompt = f"""
You are an English writing evaluator and correction assistant.

The student's target CEFR level is {request.cefr}.

Evaluate the student's English writing relative to the target CEFR level.

Topic:
{request.topic}

Essay:
{request.essay}

Return valid JSON only with exactly this structure:

{{
  "essay": "The student's original essay",
  "language": {{
    "score": 0,
    "corrected_essay": "Fully corrected version",
    "feedback": "Overall language feedback",
    "changes": [
      {{
        "category": "grammar",
        "subcategory": "specific type",
        "before": "original",
        "after": "corrected",
        "explanation": "Explanation"
      }}
    ]
  }},
  "writing": {{
    "overall_score": 0,
    "task": {{
      "score": 0,
      "feedback": "Task relevance"
    }},
    "structure": {{
      "score": 0,
      "components": [],
      "issues": []
    }},
    "logic": {{
      "score": 0,
      "relations": [],
      "issues": []
    }},
    "coherence": {{
      "score": 0,
      "feedback": "Coherence feedback",
      "issues": []
    }},
    "development": {{
      "score": 0,
      "feedback": "Development feedback",
      "issues": []
    }}
  }}
}}

Language Analysis:
- Identify meaningful grammar errors and unnatural expressions.
- Include useful word-choice and sentence-construction corrections.
- Preserve the student's original meaning.
- Do not treat every stylistic difference as an error.
- Do not make unnecessary corrections.
- "category" must be either "grammar" or "unnatural".
- If there are no meaningful language errors, return an empty "changes" array.

Writing Analysis:
- Evaluate task relevance, structure, logic, coherence, and development.
- Identify claims, reasons, examples, explanations, and conclusions when present.
- Identify logical relationships between ideas.
- For logic strength, use only "strong", "moderate", or "weak".
- Do not judge whether the student's opinion is correct.
- Do not invent information.
- Do not force components that are not present.
- Evaluate performance relative to the target CEFR level.

Scoring:
- All scores must be integers from 0 to 4.
- 0 = very weak or not demonstrated.
- 1 = limited.
- 2 = developing.
- 3 = adequate.
- 4 = strong.

Output Requirements:
- Return JSON only.
- Do not include Markdown.
- Do not include ```json.
- Do not include explanations outside the JSON.
- Follow the exact JSON structure provided above.
- Ensure the returned content is valid JSON.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    result = json.loads(response.text)

    return result