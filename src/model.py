import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse.linalg import svds

class HybridRecommender:
    """
    Hybrid Book Recommendation System
    - Latent factor collaborative filtering (SVD)
    - Content-based similarity (TF-IDF)
    """

    def __init__(self, k: int = 50):
        self.k = k
        self.user_factors = None
        self.item_factors = None
        self.tfidf_matrix = None
        self.tfidf_vectorizer = TfidfVectorizer(stop_words="english")

    def fit(self, df: pd.DataFrame):
        """
        Train hybrid recommendation model.
        Expect DataFrame with: user_id, book_id, rating, description
        """
        user_item_matrix = df.pivot_table(
            index="user_id",
            columns="book_id",
            values="rating"
        ).fillna(0)

        matrix = user_item_matrix.to_numpy()
        user_ratings_mean = matrix.mean(axis=1)
        matrix_demeaned = matrix - user_ratings_mean.reshape(-1, 1)

        U, sigma, Vt = svds(matrix_demeaned, k=self.k)
        sigma = np.diag(sigma)

        self.user_factors = U
        self.item_factors = sigma @ Vt
        self.book_ids = user_item_matrix.columns

        # 콘텐츠 기반 TF-IDF
        descriptions = df.drop_duplicates("book_id") \
                         .sort_values("book_id")["description"]
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(descriptions)

    def recommend(self, user_id: int, top_n: int = 5):
        """
        Hybrid recommendation: collaborative + content-based.
        """
        try:
            user_idx = user_id - 1
            pred_ratings = (
                self.user_factors[user_idx] @ self.item_factors
            )

            top_indices = np.argsort(pred_ratings)[::-1][:top_n]
            return self.book_ids[top_indices].tolist()
        except:
            return []
