from fastapi import FastAPI
from pydantic import BaseModel
from model import HybridRecommender
import pickle

app = FastAPI(title="Book Recommendation API")

class UserRequest(BaseModel):
    user_id: int

with open("model.pkl", "rb") as f:
    model: HybridRecommender = pickle.load(f)

@app.post("/recommend")
def recommend_books(request: UserRequest):
    books = model.recommend(request.user_id, top_n=5)
    return {"recommended_books": books}
