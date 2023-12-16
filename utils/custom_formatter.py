import json

class CustomFormatter:
    SYSTEM_MESSAGE = "Common sense questions and answers"

    def __init__(self):
        pass

    def format_for_llm(self, question, llm_api):
        formatted_prompt = f"ChatML\n\nsystem\n{CustomFormatter.SYSTEM_MESSAGE}\nuser\n{question.Content}\nassistant\n"

        json_data = {
            "prompt": formatted_prompt,
            "max_new_tokens": 128,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "repetition_penalty": 1.1
        }

        return json.dumps(json_data, indent=2)