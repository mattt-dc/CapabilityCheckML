import spacy

class OutputAnalyzer:
    def __init__(self):
            self.nlp = spacy.load("en_core_web_sm")

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
            doc_response = self.nlp(response)
            doc_expected_answer = self.nlp(expected_answer)
            
            # Iterate over each token in the expected answer
            for token1 in doc_expected_answer:
                # Iterate over each token in the response
                found_match = False
                for token2 in doc_response:
                    similarity_score = token1.similarity(token2)
                    
                    if similarity_score > 0.8:
                        found_match = True
                        break
                
                if not found_match:
                    return False
            
            # If all tokens in the expected answer have a match, return True
            return True

        return False