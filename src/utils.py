import random

def get_random_choices(correct_answer, distractors, num_choices=4):
    """Return a shuffled list of choices including the correct answer."""
    options = [correct_answer] + distractors
    random.shuffle(options)
    return options[:num_choices]
