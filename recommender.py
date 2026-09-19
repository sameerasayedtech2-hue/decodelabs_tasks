from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv

# Step 1: Load the dataset (Ingestion)
job_roles = []
job_skills = []

with open("raw_skills.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        job_roles.append(row["Job Role"])
        job_skills.append(row["Skills"])

# Step 2: Get user input (minimum 3 skills)
print("Tech Stack Recommender")
print("Enter at least 3 skills you know, separated by commas.")
user_input = input("Your skills: ")

user_skills = [skill.strip() for skill in user_input.split(",")]
user_profile = " ".join(user_skills)

# Step 3: Build TF-IDF vectors (Process)
all_documents = job_skills + [user_profile]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_documents)

# Step 4: Calculate Cosine Similarity (Scoring)
user_vector = tfidf_matrix[-1]
job_vectors = tfidf_matrix[:-1]
similarity_scores = cosine_similarity(user_vector, job_vectors)[0]

# Step 5: Sort and get Top 3 (Sorting + Filtering)
results = list(zip(job_roles, similarity_scores))
results.sort(key=lambda x: x[1], reverse=True)

top_3 = results[:3]

# Step 6: Display recommendations (Output)
print("\nTop 3 Recommended Career Paths:")
for i, (role, score) in enumerate(top_3, start=1):
    print(f"{i}. {role} (Match Score: {round(score * 100, 2)}%)")