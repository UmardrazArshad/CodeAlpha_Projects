import os
from typing import List, Dict
import nltk
import spacy
from crewai import Agent, Task, Crew
from dotenv import load_dotenv
from faq_data import FAQS, KEYWORDS
import chainlit as cl
from faq_chatbot import FAQChatbot

# Load environment variables
load_dotenv()

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

class FAQChatbot:
    def __init__(self):
        self.faqs = FAQS
        self.keywords = KEYWORDS
        
        # Create CrewAI agents
        self.qa_agent = Agent(
            role='FAQ Answering Agent',
            goal='Provide accurate and helpful answers to user questions',
            backstory="""You are an expert at understanding questions and providing 
            accurate answers from the FAQ database. You use NLP techniques to match 
            questions with the most relevant answers.""",
            verbose=True
        )
        
        self.nlp_agent = Agent(
            role='NLP Processing Agent',
            goal='Process and analyze user questions using NLP techniques',
            backstory="""You are specialized in natural language processing. 
            You help identify key terms and match questions with relevant FAQ entries.""",
            verbose=True
        )

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
        # Create tasks for the crew
        nlp_task = Task(
            description=f"Process the question: '{question}' using NLP techniques",
            expected_output="The most relevant FAQ answer to the user's question.",
            agent=self.nlp_agent
        )
        
        qa_task = Task(
            description=f"Find and provide the most relevant answer for: '{question}'",
            expected_output="A clear and concise answer from the FAQ database.",
            agent=self.qa_agent
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[self.nlp_agent, self.qa_agent],
            tasks=[nlp_task, qa_task],
            verbose=True
        )
        
        # Process the question
        processed_question = self.preprocess_question(question)
        
        # Find relevant FAQs
        relevant_faqs = self.find_relevant_faqs(processed_question)
        
        if not relevant_faqs:
            return "I'm sorry, I couldn't find a relevant answer to your question. Please try rephrasing it."
        
        # Return the most relevant answer
        return relevant_faqs[0]["answer"]

def main():
    chatbot = FAQChatbot()
    print("FAQ Chatbot (Type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        question = input("\nYour question: ").strip()
        if question.lower() == 'quit':
            break
            
        answer = chatbot.get_answer(question)
        print("\nAnswer:", answer)
        print("-" * 50)

if __name__ == "__main__":
    main() 

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="I am your intelligent Chatbot_for_FAQs about CrewAI. How can I assist you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history") or []
    history.append({"role": "user", "content": message.content})

    
    # Create an instance of the FAQChatbot
    chatbot = FAQChatbot()  # Ensure you have imported this class

    # Get the answer from the chatbot
    answer = chatbot.get_answer(message.content)

    # Send the answer back to the user
    await cl.Message(content=answer).send()  # Correctly send the answer

    # Correctly format assistant's response in history
    history.append({"role": "assistant", "content": answer})
    
    cl.user_session.set("history", history)