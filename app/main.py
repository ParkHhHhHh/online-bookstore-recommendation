# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from recommender import get_recommendations

app = FastAPI()

# --------------------------
# Pydantic 모델: User Request
# --------------------------
class UserRequest(BaseModel):
    user_id: int

# --------------------------
# 추천 API 엔드포인트
# --------------------------
@app.post("/recommend")
async def recommend_books(user_request: UserRequest):
    recommended_books = get_recommendations(user_request.user_id)
    return {"recommended_books": recommended_books}
