import requests
import json

class API_Handler:
    def __init__(self, base_url="http://127.0.0.1:5000/v1/completions"):
        self.base_url = base_url

    def send_question(self, json_data):
        try:
            response = requests.post(self.base_url, json=json_data)
            response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            response_data = json.loads(response.text)
            return response_data['choices'][0]['text'].strip()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None