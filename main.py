import argparse

from apis.api_handler import API_Handler
from data.question_bank import QuestionBank
from data.output_storage import OutputStorage
from utils.custom_formatter import CustomFormatter
from analysis.output_analyzer import OutputAnalyzer
from analysis.analysis_storage import AnalysisStorage

def main():
    parser = argparse.ArgumentParser(description='Process model name.')
    parser.add_argument('--model_name', type=str, default='Model', help='The name of the model')
    args = parser.parse_args()

    api_handler = API_Handler()
    question_bank = QuestionBank()
    output_storage = OutputStorage()
    custom_formatter = CustomFormatter()
    output_analyzer = OutputAnalyzer()
    analysis_storage = AnalysisStorage()

    questions = question_bank.load_questions()

    for question in questions:
        formatted_question = custom_formatter.format_for_llm(question)

        response = api_handler.send_question(formatted_question)

        output_storage.store_result(args.model_name, question, response)

    analysis_results = output_analyzer.analyze_output(output_storage.get_all_output())

    analysis_storage.generate_html_report(analysis_results)

if __name__ == "__main__":
    main()