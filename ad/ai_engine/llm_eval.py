from transformers import pipeline
import re

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_new_tokens=60,
    do_sample=False
)

def evaluate_with_llm(teacher_answer: str, student_answer: str):
    prompt = (
        "You are a strict grader.\n"
        "Give a score from 0 to 10.\n\n"
        f"Teacher answer:\n{teacher_answer}\n\n"
        f"Student answer:\n{student_answer}\n\n"
        "Reply ONLY in this format:\n"
        "Score: <number from 0 to 10>\n"
        "Feedback: <one short sentence>"
    )

    result = llm(prompt)
    output = result[0]["generated_text"].strip()

    print("LLM OUTPUT >>>", output)

    score_match = re.search(r"Score:\s*([0-9]+(?:\.[0-9]+)?)", output, re.I)
    feedback_match = re.search(r"Feedback:\s*(.*)", output, re.I)

    if not score_match or not feedback_match:
        return {
            "llm_score": 0,
            "feedback": "Could not reliably grade the answer.",
            "tags": ["llm_format_error"]
        }

    llm_score = min(10.0, max(0.0, float(score_match.group(1))))
    feedback = feedback_match.group(1).strip()

    return {
        "llm_score": llm_score,
        "feedback": feedback,
        "tags": []
    }
