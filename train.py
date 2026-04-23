import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

def train():
    X, y = load_iris(return_X_y=True)
    
    model = LogisticRegression(max_iter=200)

    with mlflow.start_run():
        model.fit(X, y)
        acc = model.score(X, y)

        mlflow.log_param("model", "logistic_regression")
        mlflow.log_metric("accuracy", acc)

    print("Training complete")

if __name__ == "__main__":
    train()