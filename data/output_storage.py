class OutputStorage:
    def __init__(self):
        self.results = []

    def store_result(self, llm_api, question, response):
        # Create a dictionary to represent this result
        result = {
            "llm_api": llm_api,
            "question": question,
            "response": response if response else None
        }
        self.results.append(result)

    def get_all_output(self):
        return self.results