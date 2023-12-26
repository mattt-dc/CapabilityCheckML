import json
import glob

class QuestionBank:
    def __init__(self, directory='data/questions/'):
        self.directory = directory

    def load_questions(self):
        """ Load questions from all JSON files in a directory. """
        questions = []
        for filepath in glob.glob(self.directory + '*.json'):
            try:
                with open(filepath, 'r') as file:
                    data = json.load(file)
                    questions.extend(data['questions'])
            except FileNotFoundError:
                print(f"File not found: {filepath}")
            except json.JSONDecodeError:
                print(f"Error decoding JSON from file: {filepath}")
        return questions