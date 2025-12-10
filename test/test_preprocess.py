from src.preprocess import merge_data
import pandas as pd

def test_merge_data():
    books = pd.DataFrame({
        "book_id": [1],
        "title": ["Test Book"]
    })
    ratings = pd.DataFrame({
        "user_id": [1],
        "book_id": [1],
        "rating": [5]
    })

    df = merge_data(books, ratings)
    assert "title" in df.columns
    assert df.shape[0] == 1
