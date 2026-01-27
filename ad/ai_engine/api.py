from fastapi import FastAPI
from pydantic import BaseModel
from .scorer import final_score
from .llm_eval import evaluate_with_llm
app = FastAPI(title="AI Paper Checking Agent")
class EvaluationRequest(BaseModel):
    student: str
    reference: str

@app.post("/evaluate")
def evaluate(data: EvaluationRequest):
    base_result = final_score(data.reference, data.student)
    llm_result = evaluate_with_llm(data.reference, data.student)

    base_score = base_result["final_score"]
    llm_score = llm_result.get("llm_score", 0)
    if llm_score > 0:
        FINAL = round(
            (0.8 * base_score) + (0.2 * llm_score),
            2
        )
    else:
        FINAL = base_score
    return {
        **base_result,
        "llm_score": llm_score,
        "final_score": FINAL,
        "feedback": llm_result.get("feedback", ""),
        "tags": llm_result.get("tags", [])
    }
