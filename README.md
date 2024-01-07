# CapabilityCheckML

## Overview
CapabilityCheckML is a Python project designed for benchmarking various machine learning (ML) models, with a particular focus on large language models (LLMs). The primary objective is to assess and compare the capabilities of different ML models by testing them against a range of prompts.

## Planned Features
- **Support for Various APIs:** The project is built to interface with multiple APIs, including the OpenAI APIs, allowing for a broad evaluation of different ML models.
- **Customizable Prompt Formats:** To cater to the specific requirements of different models, the project supports customization of prompt formats.
- **Output Storage:** All responses from the ML models are stored systematically for further analysis.
- **Comprehensive Analysis:** The project includes tools for analyzing the responses, comparing them against expected outputs to evaluate the accuracy and efficiency of the ML models.

## Getting Started
1. If using pip, install dependencies by running: ```pip install -r requirements.txt```
2. If using text-generation-webui, use the --api flag to start with api support. e.g add to cmd_linux.sh for linux.
3. Then run with:
```python main.py```

## Project Structure
- `apis/`: Module for handling API interactions.
- `data/`: Module for managing question data and result storage.
- `utils/`: Utility scripts for prompt formatting and other functions.
- `analysis/`: Tools for analyzing the results from ML models.
