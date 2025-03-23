# FAQ Chatbot using CrewAI

A sophisticated chatbot system designed to answer frequently asked questions using natural language processing techniques and the CrewAI framework for agent orchestration.

## Overview

This FAQ Chatbot leverages multiple AI technologies to understand user questions and provide relevant answers from a predefined FAQ database. The system uses a combination of:

- **Natural Language Processing (NLP)**: NLTK and SpaCy for text analysis
- **Agent-based Architecture**: CrewAI for creating specialized AI agents
- **Keyword Matching**: Custom keyword indexing for efficient answer retrieval

## System Architecture

### Components

1. **FAQ Database**: 
   - Structured collection of question-answer pairs
   - Keyword indexing for efficient retrieval

2. **NLP Processing Pipeline**:
   - Tokenization and part-of-speech tagging with NLTK
   - Named entity recognition with SpaCy
   - Extraction of important words (nouns, verbs, adjectives)

3. **CrewAI Agents**:
   - **NLP Processing Agent**: Specializes in analyzing user questions
   - **FAQ Answering Agent**: Matches processed questions to relevant answers

4. **Question Processing Flow**:
   - User question preprocessing
   - Keyword extraction and matching
   - Relevant FAQ identification
   - Answer retrieval and presentation

## Technical Implementation

### FAQ Data Structure

The FAQ database is structured as a list of dictionaries, each containing a question and its corresponding answer. Keywords are mapped to FAQ indices for efficient retrieval.

### NLP Processing

The system processes questions through:
1. Tokenization (breaking text into words)
2. Part-of-speech tagging (identifying nouns, verbs, etc.)
3. Named entity recognition (identifying names, organizations, etc.)
4. Extraction of important words based on their grammatical roles

### Agent Collaboration

The CrewAI framework enables the creation of specialized agents:
- The NLP agent processes and analyzes the question
- The QA agent matches the processed question to the most relevant FAQ


# **main.py file**

The chatbot will prompt you for questions. Type your question and press Enter to receive an answer. Type 'quit' to exit the program.

## Customizing the FAQ Database

You can customize the FAQ database by editing the `faq_data.py` file:

1. Add new question-answer pairs to the `FAQS` list
2. Update the `KEYWORDS` dictionary to map keywords to the indices of relevant FAQs

## Project Structure

- `main.py`: Main chatbot implementation with CrewAI agents and NLP processing
- `faq_data.py`: Sample FAQ dataset and keyword mappings
- `requirements.txt`: Project dependencies
- `.env`: Environment variables for API keys (create this file)

## Dependencies

- crewai: Framework for creating and managing AI agents
- nltk: Natural Language Toolkit for text processing
- spacy: Advanced NLP library for entity recognition
- python-dotenv: For loading environment variables
- uv: Fast Python package installer
- langchain: Optional integration for extended capabilities





