
from pathlib import Path

from analyzer.feature_extractor import extract_features

for file_path in Path("sample_codes").glob("*.py"):

    code = file_path.read_text(encoding="utf-8")

    features = extract_features(code)

    print(f"\nFile: {file_path}")
    print("-" * 40)

    for feature, value in features.items():
        print(f"{feature}: {value}")
