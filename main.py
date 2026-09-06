from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from google import genai
import json
import os

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

client = genai.Client(
    api_key="API-Key"
)


@app.get("/")
def home():
    return FileResponse("templates/writing.html")


@app.post("/submit")
def submit(essay: str = Form(...)):

    prompt = f"""
You are an English writing evaluator and correction assistant.

Analyze the student's English essay.

Return the result as valid JSON only.

The JSON must have exactly this structure:

{{
  "essay": "The student's original essay",
  "score": 0,
  "corrected_essay": "A fully corrected version",
  "errors": [
    {{
      "category": "grammar",
      "subcategory": "tense",
      "original": "incorrect expression",
      "corrected": "correct expression",
      "explanation": "Explanation of the error."
    }}
  ]
}}

Rules:

- Keep the original essay unchanged in "essay".
- Give a score from 0 to 100.
- Correct the entire essay in "corrected_essay".
- Identify meaningful errors.
- Do not invent errors.
- Return JSON only.
- Do not use Markdown.
- Do not include ```json.

Student essay:

{essay}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt,
        config={
            "response_mime_type": "application/json"
        }
    )

    result = json.loads(response.text)

    return result