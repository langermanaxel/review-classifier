import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

def train():
    df = pd.read_csv("data/reviews.csv")

    X = df["text"]
    y = df["label"]

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words=stopwords.words("spanish"))),
        ("clf", MultinomialNB())
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline.fit(X_train, y_train)

    preds = pipeline.predict(X_test)
    print(classification_report(y_test, preds))

    joblib.dump(pipeline, "model/model.pkl")
    print("Modelo guardado en model/model.pkl")

if __name__ == "__main__":
    train()
