import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

import os

def test_preprocessed_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    train_path = os.path.join(base_dir, "Data", "preprocessed_train.csv")
    test_path = os.path.join(base_dir, "Data", "preprocessed_test.csv")
    train_df = pd.read_csv(train_path)
    test_df = pd.read_csv(test_path)
    return train_df, test_df

def split_features_target(train_data, test_data):
    X_train = train_data.drop(columns="PlacementStatus")
    Y_train = train_data["PlacementStatus"]
    X_test = test_data.drop(columns="PlacementStatus")
    Y_test = test_data["PlacementStatus"]
    return X_train, Y_train, X_test, Y_test

def create_model():
    Model = LogisticRegression(
        max_iter=1000,
        random_state=42,
    )
    return Model

def train_model(model, X_train, Y_train):
    model.fit(X_train, Y_train)
    return model

def evaluate_model(model, X_test, Y_test):
    y_pred = model.predict(X_test)
    print("\nAccuracy:")
    print(model.score(X_test, Y_test))
    print("\nClassification Report:")
    print(classification_report(y_pred, Y_test))

def save_model(model):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    models_dir = os.path.join(base_dir, "Models")
    os.makedirs(models_dir, exist_ok=True)
    model_path = os.path.join(models_dir, "logistic_regression.pkl")
    joblib.dump(
        model,
        model_path
    )
    print("\nModel saved successfully")
    print(model_path)

if __name__ == "__main__":
    train_data, test_data = test_preprocessed_data()
    print("\nTrain data shape:")
    print(train_data.shape)
    print("\nTest data shape:")
    print(test_data.shape)
    X_train, Y_train, X_test, Y_test = split_features_target(
        train_data,
        test_data
    )
    print("\nTrain data shape:")
    print(X_train.shape)

    model = create_model()

    print("\nLogistic regression models created.")

    model = train_model(
        model,
        X_train,
        Y_train
    )

    print("\nLogistic regression models trained.")

    evaluate_model(
        model,
        X_test,
        Y_test
    )

    save_model(model)
