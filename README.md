# 📚 Book Recommendation System

An end-to-end **Book Recommendation System** built using **Collaborative Filtering**, with a **FastAPI backend**, **Streamlit frontend**, and a **live deployment on Hugging Face Spaces**.

This project demonstrates the complete ML lifecycle — from data processing and model building to backend integration, frontend UI, and cloud deployment.

---

## 🔗 Live Demo

👉 **Hugging Face Space:**  
https://huggingface.co/spaces/P-r-e-e-t-a-m/book-recommender

---

## 🧠 Problem Statement

Users often struggle to discover books that match their preferences due to the vast number of available titles.

This project addresses that challenge by learning from **user rating behavior** and recommending **similar books based on collective user patterns**, rather than relying only on metadata like genre or author.

---

## 🚀 Features

- ⭐ **Top 50 Popular Books**
  - Ranked using average rating and vote count
- 🔍 **Autocomplete Book Search**
- 📚 **Similar Book Recommendations**
  - Collaborative filtering using cosine similarity
- 🖼 **Book Cover & Author Display**
- 🌐 **Live Deployed Application**

---

## 🏗️ System Architecture

### Local Development
Streamlit (Frontend)
↓
FastAPI (Backend)
↓
Pickled ML Models


### Deployment (Hugging Face Spaces)
Streamlit App
↓
Pickled ML Models

> Note:  
> Hugging Face Spaces run a single application process.  
> Therefore, backend logic is merged directly into Streamlit for deployment.

---

## 📊 Dataset

- **Book-Crossing Dataset**
- Contains:
  - Users
  - Books
  - Ratings
- Highly sparse real-world dataset with missing values

---

## 🤖 Recommendation Approach

### 🔹 Popularity-Based Filtering
- Books ranked using:
  - Average rating
  - Number of ratings

### 🔹 Collaborative Filtering
- User–item rating matrix created using pivot tables
- Similarity computed between books

### 🔹 Similarity Metric
- **Cosine Similarity**
- Effective for sparse, high-dimensional matrices

---

## 🛠️ Tech Stack

### Languages & Libraries
- Python
- Pandas
- NumPy
- Scikit-learn

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Docker
- Hugging Face Spaces

---

## 📁 Project Structure

├── backend/
│ ├── main.py
│ ├── recommender.py
│ └── models/ # Generated pickle files (ignored in GitHub)
│
├── frontend/
│ └── app.py
│
├── Dockerfile
├── requirements.txt
└── README.md


---

## ▶️ Running the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/book-recommender-system.git
cd book-recommender-system

2️⃣ Generate model files

Run the Jupyter notebook to generate:

popular.pkl

pt.pkl

similarity.pkl

books.pkl

Place them inside:backend/models/

3️⃣ Start the backend
cd backend
uvicorn main:app --reload


Backend will run at:

http://127.0.0.1:8000

4️⃣ Start the frontend

Open a new terminal:

cd frontend
streamlit run app.py

⚠️ Model Files Note

Trained .pkl files are not committed to GitHub

They are generated artifacts and can be recreated

This follows standard ML project best practices

🧪 Edge Cases Handled

Missing book metadata

Sparse rating scenarios

Invalid or unmatched search queries

Safe fallbacks instead of application crashes

📌 Key Learnings

Building recommender systems on sparse real-world datasets

Collaborative filtering implementation using cosine similarity

Backend–frontend integration using FastAPI

Differences between local and cloud deployment

Docker-based ML app deployment

📈 Future Improvements

Fuzzy search (typo-tolerant recommendations)

Hybrid recommender (content + collaborative)

User login & personalization

Recommendation explanations

Enhanced UI/UX
