# FAQ Chatbot using CrewAI

This project implements a chatbot that can answer frequently asked questions (FAQs) using natural language processing techniques and CrewAI framework.

## Features

- Natural language understanding using NLTK and SpaCy
- CrewAI-based task management and orchestration
- Pre-trained models for question answering
- Easy-to-use interface for FAQ management

## Setup

1. Install UV (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies:
```bash
uv pip install -r requirements.txt
```

4. Download required NLTK data:
```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('averaged_perceptron_tagger')"
```

5. Download SpaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

Run the chatbot:
```bash
python main.py
```

## Project Structure

- `main.py`: Main chatbot implementation
- `faq_data.py`: Sample FAQ dataset
- `requirements.txt`: Project dependencies
- `.env`: Environment variables (create this file with your API keys)

## Contributing

Feel free to submit issues and enhancement requests! 