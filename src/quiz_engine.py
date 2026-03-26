import re
import random
from src.utils import get_random_choices

class QuizEngine:
    def __init__(self, text):
        self.text = text
        self.sentences = self._split_sentences()

    def _split_sentences(self):
        return re.split(r'(?<=[.!?]) +', self.text)

    def generate_question(self):
        """Generate a simple fill-in-the-blank style MCQ."""
        sentence = random.choice(self.sentences)
        words = sentence.split()
        if len(words) < 5:
            return None

        # Pick a random word to blank out
        answer = random.choice(words)
        distractors = random.sample([w for w in words if w != answer], min(3, len(words)-1))
        question = sentence.replace(answer, "_____", 1)
        options = get_random_choices(answer, distractors)

        return {
            "question": question,
            "options": options,
            "answer": answer
        }
