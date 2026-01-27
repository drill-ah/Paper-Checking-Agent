from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
import json

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Partial Marks Justification Agent in an automated paper-checking system.

Your task is ONLY to justify the marks already awarded.

Rules:
- Do NOT re-evaluate or change marks
- Do NOT suggest new scores
- Do NOT invent content not present in the student answer
- Follow the rubric strictly
- Be neutral and student-friendly
- Output must be valid JSON only
"""

class JustificationInput(BaseModel):
    question: str
    rubric: str
    student_answer: str
    marks_given: int
    total_marks: int

@app.post("/justify")
def justify(data: JustificationInput):

    user_data = {
        "question": data.question,
        "rubric": data.rubric,
        "student_answer": data.student_answer,
        "marks_given": data.marks_given,
        "total_marks": data.total_marks
    }

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(user_data)}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content.strip()

    if raw.startswith("```"):
        raw = raw.replace("```json", "").replace("```", "").strip()

    justification_json = json.loads(raw)

    return justification_json
