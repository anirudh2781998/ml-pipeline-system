from fastapi import FastAPI
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

app = FastAPI()

X, y = load_iris(return_X_y=True)
model = LogisticRegression(max_iter=200)
model.fit(X, y)

@app.get("/predict")
def predict():
    pred = model.predict([X[0]])
    return {"prediction": int(pred[0])}