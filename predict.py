from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

def predict():
    X, y = load_iris(return_X_y=True)

    model = LogisticRegression(max_iter=200)
    model.fit(X, y)

    preds = model.predict(X[:5])
    print(preds)

if __name__ == "__main__":
    predict()