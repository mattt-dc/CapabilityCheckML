class CustomFormatter:
    SYSTEM_MESSAGE = "Common sense questions and answers"

    def __init__(self):
        pass

    def format_for_llm(self, question):
        formatted_prompt = f"ChatML\n\nsystem\n{CustomFormatter.SYSTEM_MESSAGE}\nuser\n{question['content']}\nassistant\n"

        json_data = {
            "prompt": formatted_prompt,
            "max_tokens": 4096,
            "do_sample": True,
            "temperature": 0.7,
            "top_p": 0.95,
            "top_k": 40,
            "repetition_penalty": 1.1
        }

        return json_data