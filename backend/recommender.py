import pickle
import numpy as np

popular_df = pickle.load(open("models/popular.pkl", "rb"))
pt = pickle.load(open("models/pt.pkl", "rb"))
similarity_scores = pickle.load(open("models/similarity.pkl", "rb"))
books = pickle.load(open("models/books.pkl", "rb"))

def get_top_books(n=50):
    return popular_df.head(n)

def get_all_books():
    return list(pt.index)

def recommend_books(book_name,n=5):
    if book_name not in pt.index:
        return None
    searched_df=books[books["Book-Title"]==book_name]
    if searched_df.empty:
        return None
    searched=searched_df.iloc[0]
    searched_book={
        "title":searched["Book-Title"],
        "author":searched["Book-Author"],
        "image":searched["Image-URL-M"]
    }
    idx=pt.index.get_loc(book_name)
    similar_items=sorted(list(enumerate(similarity_scores[idx])),key=lambda x:x[1],reverse=True)[1:n+1]

    recommendations=[]
    for i in similar_items:
        title = pt.index[i[0]]             
        temp_df = books[books["Book-Title"] == title]

        if temp_df.empty:
            continue

        temp = temp_df.iloc[0]

        recommendations.append({
            "title": temp["Book-Title"],
            "author": temp["Book-Author"],
            "image": temp["Image-URL-M"]
        })

    return {
        "searched_book": searched_book,
        "recommended_books": recommendations
    }