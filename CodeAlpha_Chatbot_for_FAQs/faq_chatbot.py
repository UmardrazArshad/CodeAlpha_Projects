import nltk
import spacy
from typing import List, Dict
from faq_data import FAQS, KEYWORDS

# Download required NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

class FAQChatbot:
    def __init__(self):
        self.faqs = FAQS
        self.keywords = KEYWORDS
        
    def preprocess_question(self, question: str) -> List[str]:
        """Preprocess the question using NLTK and SpaCy."""
        # Tokenize the question
        tokens = nltk.word_tokenize(question.lower())
        
        # Get POS tags
        pos_tags = nltk.pos_tag(tokens)
        
        # Extract important words (nouns, verbs, adjectives)
        important_words = [word for word, tag in pos_tags 
                         if tag.startswith(('NN', 'VB', 'JJ'))]
        
        # Add SpaCy named entities
        doc = nlp(question)
        entities = [ent.text.lower() for ent in doc.ents]
        
        return list(set(important_words + entities))

    def find_relevant_faqs(self, processed_question: List[str]) -> List[Dict]:
        """Find relevant FAQs based on processed question."""
        relevant_indices = set()
        
        # Find matching keywords
        for word in processed_question:
            if word in self.keywords:
                relevant_indices.update(self.keywords[word])
        
        # Return relevant FAQs
        return [self.faqs[i] for i in relevant_indices]

    def get_answer(self, question: str) -> str:
        """Get answer for the user's question."""
        # Process the question
        processed_question = self.preprocess_question(question)
        
        # Find relevant FAQs
        relevant_faqs = self.find_relevant_faqs(processed_question)
        
        if not relevant_faqs:
            return "I'm sorry, I couldn't find a relevant answer to your question. Please try rephrasing it."
        
        # Return the most relevant answer
        return relevant_faqs[0]["answer"] 