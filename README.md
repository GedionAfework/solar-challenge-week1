# Solar Challenge Week 1

## Setup Instructions

1. Clone the repository:
   https://github.com/GedionAfework/solar-challenge-week1.git

2. Navigate into the directory:
   `cd solar-challenge-week1.git`

3. Create and activate virtual environment:
   python -m venv .venv
   .venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the Streamlit App
   streamlit run app/main.py

## Repository Structure

├── .github/
│ └── workflows/
│ └── ci.yml # GitHub Actions for CI
├── .vscode/
│ └── settings.json # Optional VSCode settings
├── app/
│ ├── init.py
│ ├── main.py # Streamlit dashboard
│ └── utils.py # Helper functions
├── data/
│ └── \*.csv # Cleaned data files (not committed)
├── notebooks/
│ ├── benin_eda.ipynb
│ ├── sierra_leone_eda.ipynb
│ ├── togo_eda.ipynb
│ └── compare_countries.ipynb # Cross-country comparison
├── scripts/
│ ├── init.py
│ └── README.md
├── tests/
│ └── init.py
├── src/
├── requirements.txt # Python dependencies
├── .gitignore
├── README.md

What Was Done
Initialized GitHub repository and configured CI/CD with GitHub Actions.

Performed detailed EDA for each country and saved the cleaned data.

Compared solar energy potential across the three countries.

Built and deployed a Streamlit dashboard for interactive data exploration.

Navigation Guide
notebooks/ contains all EDA and analysis notebooks.

data/ holds the cleaned CSVs (not committed to GitHub).

app/ contains the Streamlit dashboard files.

.github/ holds the CI workflow configuration.

requirements.txt lists all Python dependencies.
