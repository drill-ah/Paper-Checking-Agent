import os

# Must be set BEFORE importing sentence-transformers / transformers
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TF"] = "0"

from sentence_transformers import SentenceTransformer, util

# Load model once (fast)
try:
    model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    raise Exception("Install: pip install sentence-transformers") from e


def semantic_similarity_score(correct_answer: str, student_answer: str):
    """
    Returns (score_out_of_10, raw_cosine_similarity)
    """
    emb1 = model.encode(correct_answer, convert_to_tensor=True)
    emb2 = model.encode(student_answer, convert_to_tensor=True)

    similarity = util.cos_sim(emb1, emb2).item()  # 0–1
    score_10 = round(similarity * 10, 2)

    return score_10, similarity
