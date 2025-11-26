import joblib

model = joblib.load("model/model.pkl")

def predict_sentiment(text):
    pred = model.predict([text])[0]
    prob = model.predict_proba([text])[0]
    return pred, max(prob)
