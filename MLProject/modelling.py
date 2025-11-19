import os
import argparse
import mlflow
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def run_autolog(test_size, n_estimators, max_depth, data_dir):
    uri = os.getenv("MLFLOW_TRACKING_URI", "file:./mlruns")
    mlflow.set_tracking_uri(uri)

    # MLflow runs from MLProject/ directory, so data_dir is relative to that
    data_path = os.path.join(data_dir, "insurance_train_preprocessed.csv")
    print(f"Loading data from: {data_path}")
    df = pd.read_csv(data_path)

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop("target", axis=1),
        df["target"],
        test_size=test_size,
        random_state=42
    )

    # Manual logging instead of autolog to avoid compatibility issues
    with mlflow.start_run():
        mlflow.log_param("test_size", test_size)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        
        model = RandomForestRegressor(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)
        
        mlflow.log_metric("r2_score", score)
        mlflow.sklearn.log_model(model, "model")
        
        print("Model training completed.")
        print(f"R² Score: {score:.4f}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--test_size", type=float, default=0.2)
    p.add_argument("--n_estimators", type=int, default=100)
    p.add_argument("--max_depth", type=int, default=5)
    p.add_argument("--data_dir", type=str, default="insurance_preprocessing")
    a = p.parse_args()
    run_autolog(a.test_size, a.n_estimators, a.max_depth, a.data_dir)