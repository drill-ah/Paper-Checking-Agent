from .keywords import extract_keywords
from .similarity import semantic_similarity_score
def keyword_score(correct_answer: str, student_answer: str):
    teacher_keywords = set(extract_keywords(correct_answer))
    student_keywords = set(extract_keywords(student_answer))
    if not teacher_keywords:
        return 0.0, [], []
    matched = teacher_keywords & student_keywords
    missing = teacher_keywords - student_keywords
    score = (len(matched) / len(teacher_keywords)) * 10
    return round(score, 2), list(matched), list(missing)

def final_score(correct_answer: str, student_answer: str):
    """
    Combines keyword + semantic score
    """
    key_score, matched, missing = keyword_score(correct_answer, student_answer)
    sim_score, raw_similarity = semantic_similarity_score(correct_answer, student_answer)
    FINAL = round((0.2 * key_score) + (0.8 * sim_score), 2)
    return {
        "keyword_score": key_score,
        "semantic_score": sim_score,
        "final_score": FINAL,
        "matched_keywords": matched,
        "missing_keywords": missing,
        "raw_similarity": raw_similarity
    }