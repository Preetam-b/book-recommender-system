import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")
menu = st.sidebar.selectbox("Menu", ["Home", "Recommend"])


@st.cache_data
def get_top_books():
    return requests.get(f"{API_URL}/top-books").json()


@st.cache_data
def get_all_books():
    return requests.get(f"{API_URL}/books").json()


# ---------------- HOME ----------------
if menu == "Home":
    st.title("Top 50 Books")

    data = get_top_books()
    cols = st.columns(5)

    for i, book in enumerate(data):
        with cols[i % 5]:
            st.image(book["Image-URL-M"])
            st.text(book["Book-Title"])
            st.text(book["Book-Author"])
            st.caption(f"🗳 {book['num_ratings']}")
            st.caption(f"⭐ {round(book['avg_ratings'], 2)}")


# ---------------- RECOMMEND ----------------
if menu == "Recommend":
    st.title("Recommend Similar Books")

    if "books" not in st.session_state:
        st.session_state.books = get_all_books()

    user_input = st.text_input("Search a book")

    suggestions = []
    if user_input:
        suggestions = [
            b for b in st.session_state.books
            if user_input.lower() in b.lower()
        ][:10]

    selected_book = st.selectbox(
        "Suggestions",
        suggestions if suggestions else ["No matches found"]
    )

    if st.button("Recommend", disabled=selected_book == "No matches found"):
        res = requests.get(
            f"{API_URL}/recommend",
            params={"book_name": selected_book}
        ).json()

        if "error" in res:
            st.error(res["error"])
        else:
            st.subheader("You searched for")
            col = st.columns(5)
            with col[0]:
                st.image(res["searched_book"]["image"])
                st.text(res["searched_book"]["title"])
                st.text(res["searched_book"]["author"])

            st.subheader("Similar Books")
            cols = st.columns(5)
            for i, book in enumerate(res["recommended_books"]):
                with cols[i]:
                    st.image(book["image"])
                    st.text(book["title"])
                    st.text(book["author"])
