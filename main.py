import os
from collections import defaultdict

# Simulated Memory
question_memory = defaultdict(lambda: {"years": set(), "frequency": 0})

# Keywords to detect questions
QUESTION_KEYWORDS = ["what", "define", "explain", "describe", "why", "how"]

def extract_questions(text):
    questions = []
    lines = text.split("\n")
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith("?") or any(line.lower().startswith(k) for k in QUESTION_KEYWORDS):
            questions.append(line)
    return questions

def process_paper(file_path, year):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    questions = extract_questions(text)
    for q in questions:
        question_memory[q]["years"].add(year)
        question_memory[q]["frequency"] += 1

def get_top_repeated_questions(top_n=5):
    repeated = {q: data for q, data in question_memory.items() if data["frequency"] > 1}
    sorted_q = sorted(repeated.items(), key=lambda x: x[1]["frequency"], reverse=True)
    return sorted_q[:top_n]

def print_results():
    top_questions = get_top_repeated_questions()
    if not top_questions:
        print("⚠️ No repeated questions found.")
        return
    print("\n📘 Top Repeated Questions:\n")
    for idx, (q, data) in enumerate(top_questions, 1):
        years = ", ".join(sorted(data["years"]))
        print(f"{idx}. {q}  \n   _[Appeared in: {years}]_\n")

# Example Simulation
if __name__ == "__main__":
    # Simulate processing 3 papers from 3 years
    sample_files = {
        "2021": "paper_2021.txt",
        "2022": "paper_2022.txt",
        "2023": "paper_2023.txt"
    }

    for year, file in sample_files.items():
        if os.path.exists(file):
            process_paper(file, year)
        else:
            print(f"⚠️ File {file} not found. Please add a text file for year {year}.")

    print_results()
