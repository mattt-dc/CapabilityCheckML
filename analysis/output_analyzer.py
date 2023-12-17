class OutputAnalyzer:
    def analyze_output(self, outputs):
        analysis_summary = {
            "total": 0,
            "correct": 0,
            "incorrect": 0,
            "correct_responses": [],
            "incorrect_responses": []
        }

        for output in outputs:
            analysis_summary["total"] += 1
            question = output["question"]
            response = output["response"]

            # Check if the response is correct based on the answer logic
            if self.is_correct(response, question["answer"], question["answer_logic"]):
                analysis_summary["correct"] += 1
                analysis_summary["correct_responses"].append(output)
            else:
                analysis_summary["incorrect"] += 1
                analysis_summary["incorrect_responses"].append(output)

        return analysis_summary

    def is_correct(self, response, expected_answer, answer_logic):
        if answer_logic == "Contains":
            return expected_answer in response

        return False