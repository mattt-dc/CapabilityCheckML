from airium import Airium

class AnalysisStorage:

    def generate_html_report(self, analysis_summary):
        a = Airium()

        a('<!DOCTYPE html>')
        with a.html(lang='en'):
            with a.head():
                a.title(_t='Analysis Summary')
            with a.body():
                a.h1(_t='Analysis Summary')

                # Add total, correct, incorrect to the report
                a.p(_t=f'Total: {analysis_summary["total"]}')
                a.p(_t=f'Correct: {analysis_summary["correct"]}')
                a.p(_t=f'Incorrect: {analysis_summary["incorrect"]}')

                # Add correct responses
                a.h2(_t='Correct Responses')
                for response in analysis_summary["correct_responses"]:
                    a.p(_t=str(response))

                # Add incorrect responses
                a.h2(_t='Incorrect Responses')
                for response in analysis_summary["incorrect_responses"]:
                    a.p(_t=str(response))

        # Write to an HTML file
        with open('report.html', 'wb') as f:
            f.write(bytes(a))