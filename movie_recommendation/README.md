# Netflix Movie Recommender System

This project implements a basic content-based movie recommender system using a Netflix movie dataset. The goal is to recommend similar movies based on genres, cast, director, and keywords using text similarity techniques.

## 🎯 Objective

- Build a movie recommendation engine.
- Use content-based filtering with textual metadata.
- Provide top similar movies based on a given input title.

## 📁 Files

- `netflix_movie_recom.ipynb`: Jupyter notebook containing all code, data processing, feature engineering, and recommendation logic.

## 🧰 Tools Used

- Python
- Pandas
- Scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
- Numpy

## 🛠️ Features

- Processes movie metadata like **title, genre, cast, director, and description**.
- Combines text features to compute similarity using **TF-IDF** and **cosine similarity**.
- Provides **top-N recommendations** for any input movie title.

## 🔍 How It Works

1. Combine selected features into a single string per movie.
2. Convert text data into numerical vectors using TF-IDF.
3. Calculate cosine similarity between all movie pairs.
4. Recommend top similar movies for a user-provided movie.

## 💻 How to Run

1. Install required libraries:
    ```bash
    pip install pandas scikit-learn numpy
    ```

2. Launch the notebook:
    ```bash
    jupyter notebook netflix_movie_recom.ipynb
    ```

3. Run the cells sequentially. Input a movie title in the specified cell to get recommendations.

## ✅ Example Output

If you input a movie like `"Inception"`, the model returns a list of similar movies based on content features.

## 🔮 Possible Improvements

- Use NLP on descriptions for deeper semantic similarity.
- Integrate collaborative filtering for hybrid recommendations.
- Add a web interface using Streamlit or Flask.

## 📌 Notes

- Ensure that the dataset used inside the notebook is accessible if separated.
- Handles basic errors for missing titles or sparse data.

