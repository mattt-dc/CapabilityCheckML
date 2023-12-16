from apis.llm_api_handler import LLM_API_Handler
from data.question_bank import QuestionBank
from data.output_storage import OutputStorage
from utils.custom_formatter import CustomFormatter
from analysis.output_analyzer import OutputAnalyzer

def main():
    api_handler = LLM_API_Handler()
    question_bank = QuestionBank()
    output_storage = OutputStorage()
    custom_formatter = CustomFormatter()
    output_analyzer = OutputAnalyzer()

    questions = question_bank.load_questions()

    for question in questions:
        formatted_question = custom_formatter.format_for_llm(question, llm_api)

        response = api_handler.send_question(formatted_question, llm_api)

        output_storage.store_result(llm_api, question, response)

    analysis_results = output_analyzer.analyze_output(output_storage.get_all_output())

if __name__ == "__main__":
    main()