import pandas as pd
from pathlib import Path

def load_data(data_dir: str = "data"):
    """Load book, rating, and user data."""
    data_path = Path(data_dir)

    books = pd.read_csv(data_path / "books.csv")
    ratings = pd.read_csv(data_path / "ratings.csv")
    users = pd.read_csv(data_path / "users.csv")

    return books, ratings, users
