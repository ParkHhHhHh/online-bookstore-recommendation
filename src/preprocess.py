import pandas as pd

def merge_data(books: pd.DataFrame, ratings: pd.DataFrame):
    """
    Merge book metadata with user rating data.
    """
    df = ratings.merge(books, on="book_id", how="left")
    df.dropna(subset=["title"], inplace=True)
    return df
