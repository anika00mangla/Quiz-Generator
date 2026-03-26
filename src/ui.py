from src.quiz_engine import QuizEngine

def run_quiz(text, num_questions=5):
    engine = QuizEngine(text)
    score = 0

    for i in range(num_questions):
        q = engine.generate_question()
        if not q:
            continue

        print(f"\nQ{i+1}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"{idx+1}. {opt}")

        choice = input("Your answer (number): ")
        try:
            if q['options'][int(choice)-1] == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {q['answer']}")
        except:
            print("Invalid input.")

    print(f"\nFinal Score: {score}/{num_questions}")
