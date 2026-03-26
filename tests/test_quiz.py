import pytest
from src.quiz_engine import QuizEngine

def test_generate_question():
    text = "Python is a programming language. It is popular."
    engine = QuizEngine(text)
    q = engine.generate_question()
    assert "question" in q
    assert "options" in q
    assert "answer" in q
    assert len(q["options"]) >= 2
