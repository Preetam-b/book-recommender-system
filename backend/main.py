from fastapi import FastAPI, Query
from recommender import (
    get_top_books,
    get_all_books,
    recommend_books
)

app = FastAPI(title="Book Recommender API")


@app.get("/")
def root():
    return {"message": "Book Recommender API running"}


@app.get("/top-books")
def top_books():
    df = get_top_books()
    return df.to_dict(orient="records")


@app.get("/books")
def books():
    return get_all_books()


@app.get("/recommend")
def recommend(
    book_name: str = Query(..., description="Exact book title from /books")
):
    result = recommend_books(book_name)

    if result is None:
        return {
            "error": "Book not found or insufficient data",
            "searched_book": book_name,
            "recommended_books": []
        }

    return result
