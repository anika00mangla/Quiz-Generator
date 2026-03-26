from src.ui import run_quiz

if __name__ == "__main__":
    with open("data/sample_notes.txt", "r") as f:
        text = f.read()

    print("🎓 Welcome to the Interactive Quiz Generator!")
    run_quiz(text, num_questions=5)
