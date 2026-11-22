
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


data = pd.read_csv("dataset/features.csv")

X = data.drop("label", axis=1)
y = data["label"]

# This is only a pipeline smoke test.
# Six samples are far too few for meaningful evaluation.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.33,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("\nVULNSCOPE RANDOM FOREST RESULTS")
print("=" * 45)

print(classification_report(
    y_test,
    predictions,
    zero_division=0
))

joblib.dump(model, "dataset/vulnscope_model.pkl")

print("Model saved successfully!")
