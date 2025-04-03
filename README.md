🎬 Movie Recommender System
 
A **content-based Movie Recommendation System** built using **Python, Pandas, Scikit-learn, and Streamlit**. It suggests movies similar to the selected one based on cosine similarity.

## 🚀 Live Demo
🔗 **Try it here:** [Movie Recommender System](https://movie-recommender-system-reybmtyzx2vpqjp65g4wgt.streamlit.app/)

## 📌 Features
✅ **Movie Recommendations** – Get 5 similar movies based on your selection.  
✅ **Poster Display** – Shows movie posters along with recommendations.  
✅ **Streamlit UI** – A clean and interactive web interface.  

## 🛠️ Technologies Used
- **Python** 🐍
- **Pandas** (for data manipulation)
- **Scikit-learn** (cosine similarity for recommendations)
- **TMDb API** (for fetching movie posters)
- **Streamlit** (for building the web app)

## ⚡ Installation & Running Locally
1. **Clone the repository:**
   git clone https://github.com/PrasadHiremath1/Movie-Recommender-System.git
   cd Movie-Recommender-System
   
2. Install dependencies:
  pip install -r requirements.txt
  Run the app:

3. Run the app
  streamlit run app.py

-> How It Works
The app loads movie data and computes cosine similarity.

When a user selects a movie, the system finds 5 similar movies.

Posters are fetched from TMDb API and displayed.
