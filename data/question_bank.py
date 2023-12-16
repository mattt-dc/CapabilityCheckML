import json

class QuestionBank:
    def __init__(self, filepath='questions/questions.json'):
        self.filepath = filepath

    def load_questions(self):
        """ Load questions from a JSON file. """
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return data['questions']
        except FileNotFoundError:
            print(f"File not found: {self.filepath}")
            return []
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.filepath}")
            return []