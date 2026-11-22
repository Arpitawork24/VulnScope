
import joblib
import pandas as pd

from analyzer.feature_extractor import extract_features


model = joblib.load("dataset/vulnscope_model.pkl")


def predict_code(source_code):

    features = extract_features(source_code)

    input_data = pd.DataFrame([features])

    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    return {
        "prediction": int(prediction),
        "confidence": float(max(probabilities)),
        "features": features
    }


if __name__ == "__main__":

    test_cases = {
        "Safe code": """
name = input("Enter your name: ")
print("Hello", name)
""",

        "Potentially vulnerable code": """
user_input = input("Enter value: ")
eval(user_input)
"""
    }

    for name, code in test_cases.items():

        result = predict_code(code)

        print(f"\n{name}")
        print("-" * 40)

        print("Prediction:", result["prediction"])
        print(
            "Confidence:",
            round(result["confidence"] * 100, 2),
            "%"
        )

        if result["prediction"] == 1:
            print("Result: Potentially vulnerable code")
        else:
            print("Result: Classified as safe")
