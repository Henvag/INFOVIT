from dataclasses import dataclass
from typing import List
import json
import random
import os
import sys

@dataclass
class Question:
    question: str
    options: List[str]
    correct: int
    topic: str

    @classmethod
    def from_dict(cls, data):
        question = data.get('question') or data.get('text')
        if not question:
            raise ValueError(f"No question field found in data: {data}")

        return cls(
            question=question,
            options=data.get('options', []),
            correct=data.get('correct', data.get('correct_index', 0)),
            topic=data.get('topic', 'Unknown')
        )

    def shuffle_options(self):
        options_with_index = list(enumerate(self.options))
        random.shuffle(options_with_index)
        self.options = [option for index, option in options_with_index]
        self.correct = next(index for index, (original_index, _) in enumerate(options_with_index) if original_index == self.correct)

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        # Running in a bundle
        base_path = sys._MEIPASS
    else:
        # Running in normal Python environment
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

class QuizManager:
    def __init__(self, filename='info216_2023exam_questions.json'):
        self.filename = resource_path(filename)
        self.questions = []
        self.load_questions()

    def load_questions(self, filename=None):
        if filename:
            self.filename = filename
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.questions = [Question.from_dict(q) for q in data]
                print(f"Successfully loaded {len(self.questions)} questions")
        except FileNotFoundError:
            print(f"Error: File {self.filename} not found")
            raise
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {self.filename}: {e}")
            raise
        except Exception as e:
            print(f"Error loading questions: {e}")
            raise

    def shuffle_questions(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.shuffle_options()