"""
Sample FAQ dataset for the chatbot.
This can be replaced with your own FAQ data.
"""

FAQS = [
    {
        "question": "What is CrewAI?",
        "answer": "CrewAI is a framework for creating and managing AI agents that can work together to accomplish complex tasks. It allows you to create specialized agents with different roles and capabilities."
    },
    {
        "question": "How do I install CrewAI?",
        "answer": "You can install CrewAI using pip: 'pip install crewai' or using UV: 'uv pip install crewai'."
    },
    {
        "question": "What is UV?",
        "answer": "UV is a fast Python package installer and resolver, written in Rust. It's designed to be a drop-in replacement for pip with better performance."
    },
    {
        "question": "What are the main features of CrewAI?",
        "answer": "CrewAI features include agent creation and management, task delegation, role-based agent specialization, and seamless integration with various AI models and tools."
    },
    {
        "question": "How do I create a new agent in CrewAI?",
        "answer": "You can create a new agent in CrewAI by defining its role, goal, and backstory, then instantiating it using the Agent class from the crewai package."
    }
]

# Keywords and their associated FAQ indices
KEYWORDS = {
    "crewai": [0, 1, 4],
    "uv": [2],
    "install": [1, 2],
    "features": [3],
    "agent": [4],
    "create": [4],
    "what": [0, 2, 3],
    "how": [1, 4],
    "python": [2],
    "environment": [],
    "pip": [1, 2],
    "fix": []
} 