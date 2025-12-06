# app/recommender.py
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------
# Mock 데이터: 책 정보
# --------------------------
books_data = pd.DataFrame({
    'book_id': [1, 2, 3, 4, 5],
    'title': ['Data Science 101', 'Machine Learning for Dummies', 'Introduction to AI', 
              'Deep Learning with Python', 'Python for Data Analysis'],
    'author': ['John Doe', 'Jane Smith', 'Alice Brown', 'Bob White', 'Charlie Black'],
    'genre': ['Data Science', 'Machine Learning', 'AI', 'Deep Learning', 'Data Science'],
    'description': ['Introduction to Data Science techniques', 
                    'Beginner’s guide to Machine Learning', 
                    'Fundamentals of Artificial Intelligence', 
                    'Practical deep learning with Keras and TensorFlow', 
                    'Comprehensive guide to Python for Data Analysis']
})

# --------------------------
# 간단한 추천 시스템 (코사인 유사도)
# --------------------------
def get_recommendations(user_id):
    # Mock 유저의 책 평가 (딕셔너리로 저장)
    user_ratings = {1: 5, 2: 3, 3: 4}  # 예시: 책 1, 2, 3을 평가

    # 유저가 평가하지 않은 책들만 필터링
    unrated_books = books_data[~books_data['book_id'].isin(user_ratings.keys())]

    # 책 설명을 벡터화하여 유사도 계산
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(books_data['description'])
    cosine_sim = cosine_similarity(count_matrix, count_matrix)

    # 평가된 책과 유사한 책을 추천
    similar_scores = []
    for _, row in unrated_books.iterrows():
        book_id = row['book_id']
        similarity_score = sum(cosine_sim[book_id-1, rated_book-1] for rated_book in user_ratings.keys())
        similar_scores.append((book_id, similarity_score))

    # 추천 순으로 정렬하고, 상위 3개 책 추천
    similar_scores = sorted(similar_scores, key=lambda x: x[1], reverse=True)
    recommended_books = [books_data.loc[books_data['book_id'] == book_id, 'title'].values[0] for book_id, _ in similar_scores[:3]]

    return recommended_books
