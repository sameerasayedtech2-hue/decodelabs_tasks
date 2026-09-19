# Tech Stack Recommender

## Overview
A content-based AI recommendation system built in Python that suggests career paths based on a user's skills. This project moves beyond simple rule-based logic (Project 1) and classification (Project 2) into recommendation systems — using mathematical similarity matching instead of hardcoded rules or labeled predictions.

## How It Works
1. User enters at least 3 skills, separated by commas
2. All skills — the user's and every job role's — are converted into TF-IDF vectors, which weigh specific/unique terms higher than common ones
3. Cosine Similarity is calculated between the user's vector and each job role's vector to measure how closely their "direction" aligns
4. Results are sorted by similarity score, and the Top 3 matching career paths are displayed with a percentage match

## Features
- Accepts flexible user input (any combination of skills)
- Uses TF-IDF + Cosine Similarity — the same core technique behind real-world recommendation engines like Netflix and Amazon
- Returns ranked results with match percentages, not just a single guess
- Reads job role data dynamically from a CSV file, so new roles can be added without changing the code

## How to Run
1. Make sure Python is installed on your system.
2. Install the required library:


pip install scikit-learn
3. Open a terminal in this folder.
4. Run the file:

python recommender.py
5. Enter at least 3 skills when prompted, for example:

Python, Cloud Computing, Automation

## Key Concepts Used
- TF-IDF (Term Frequency-Inverse Document Frequency)
- Cosine Similarity
- Content-based filtering
- Vector space modeling
- CSV data handling

## Example Interaction


## Files
- `recommender.py` — main program logic
- `raw_skills.csv` — dataset of job roles and their associated skills

Part of my AI Internship with DecodeLabs.
