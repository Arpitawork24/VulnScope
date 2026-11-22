
# VulnScope

**ML-Based Static Code Vulnerability Analyzer**

VulnScope is a research-oriented Python static analysis prototype that explores how traditional security rules, taint analysis, and machine learning can be combined to identify potentially vulnerable code patterns.

## Current Features

- AST-based Python source code parsing
- Rule-based security pattern detection
- Basic taint analysis
- Bandit integration for baseline comparison
- AST-based feature extraction
- Random Forest classification
- Basic vulnerability prediction

## Technology Stack

- Python
- AST
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Bandit

## Project Structure

- `analyzer/` - Core analysis and ML modules
- `sample_codes/` - Safe and potentially vulnerable code examples
- `dataset/` - Initial labelled sample dataset

## Setup

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd VulnScope
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the Project

Run the comparison engine:

```bash
python test_comparison.py
```

Build the feature dataset:

```bash
python -m analyzer.dataset_builder
```

Train the initial Random Forest model:

```bash
python -m analyzer.train_model
```

Test ML predictions:

```bash
python -m analyzer.predict
```

## Research Objective

The project explores the following research question:

Can machine learning complement traditional rule-based static analysis by identifying potentially vulnerable code patterns?

## Current Limitations

- Taint analysis supports only basic data-flow patterns.
- The initial dataset is very small and manually labelled.
- ML predictions are experimental and not validated for real-world security use.
- The current classifier has not demonstrated generalization to unseen projects.

## Disclaimer

VulnScope is an experimental research prototype, not a replacement for professional security auditing tools.
