import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score, classification_report
from src.data.load_data import load_data
from src.data.preprocess import (
    split_data,
    identify_features,
    handle_missing_values,
    one_hot_encode_data,
    ordinal_encode_data,
)

def create_model():
    return AdaBoostClassifier(n_estimators=50, random_state=42)

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    print("\nAdaBoost Model Training Complete")
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print("\nAccuracy:", accuracy)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    return y_pred

def main():
    df = load_data()
    print("\nOriginal Dataset Shape:", df.shape)
    X_train, X_test, y_train, y_test = split_data(
        df,
        target_columns="PlacementStatus",
        drop_columns=["StudentID", "Salary Package", "IsAnomaly"]
    )
    numerical_features, categorical_features = identify_features(X_train)
    one_hot_features = [
        'Gender', 'City', 'Stream', 'Specialisation', 'Hostel', 'HistoryOfBacklogs'
    ]
    ordinal_features = ['CollegeTier', 'CGPA_Tier']

    X_train, X_test, imputer = handle_missing_values(X_train, X_test, numerical_features)
    X_train, X_test, one_hot_encoder = one_hot_encode_data(X_train, X_test, one_hot_features)
    X_train, X_test, ordinal_encoder = ordinal_encode_data(X_train, X_test, ordinal_features)

    model = create_model()
    model = train_model(model, X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
