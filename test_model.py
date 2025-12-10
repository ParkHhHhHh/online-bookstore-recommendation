import pytest
import numpy as np
import pandas as pd
from src.model import HybridRecommender
from src.data_loader import load_data
from src.preprocess import merge_data

@pytest.fixture(scope="module")
def data():
    books, ratings, users = load_data()
    df = merge_data(books, ratings)
    return df

@pytest.fixture(scope="module")
def recommender(data):
    model = HybridRecommender(k=50)
    model.fit(data)
    return model

def test_model_initialization(recommender):
    assert recommender is not None, "Model should be initialized"
    assert isinstance(recommender, HybridRecommender), "Should be instance of HybridRecommender"

def test_recommendations_length(recommender):
    # Test that recommendation list has the expected length (e.g., top 5)
    recommendations = recommender.recommend(user_id=1, top_n=5)
    assert len(recommendations) == 5, "Recommendation list should have 5 items"

def test_rmse_calculation(data, recommender):
    from src.evaluation import rmse
    true_ratings = data['rating'].values
    predicted_ratings = recommender.user_factors @ recommender.item_factors
    predicted_ratings = predicted_ratings.flatten()  # Flatten into a single vector
    score = rmse(true_ratings, predicted_ratings)
    assert score < 1.0, f"RMSE score is too high: {score:.4f}"
