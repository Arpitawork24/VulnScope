
import pandas as pd

from analyzer.feature_extractor import extract_features


def build_dataset(input_path, output_path):

    data = pd.read_csv(input_path)

    feature_rows = []

    for _, row in data.iterrows():

        features = extract_features(row["code"])

        features["label"] = int(row["label"])

        feature_rows.append(features)

    feature_df = pd.DataFrame(feature_rows)

    feature_df.to_csv(output_path, index=False)

    print("\nML DATASET CREATED")
    print("=" * 40)
    print(feature_df)

    print("\nDataset shape:", feature_df.shape)
    print("\nLabel distribution:")
    print(feature_df["label"].value_counts())


if __name__ == "__main__":

    build_dataset(
        "dataset/examples.csv",
        "dataset/features.csv"
    )
