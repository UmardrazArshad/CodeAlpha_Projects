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
    },
    {
        "question": "What programming languages does CrewAI support?",
        "answer": "CrewAI primarily supports Python, but it can also integrate with other languages through APIs and custom agents."
    },
    {
        "question": "Can I use CrewAI for real-time applications?",
        "answer": "Yes, CrewAI is designed to handle real-time applications, allowing agents to communicate and collaborate efficiently in dynamic environments."
    },
    {
        "question": "How does CrewAI handle agent communication?",
        "answer": "CrewAI uses a message-passing architecture that allows agents to send and receive messages, enabling them to collaborate and share information seamlessly."
    },
    {
        "question": "Is there a community or support for CrewAI users?",
        "answer": "Yes, CrewAI has an active community of users and developers. You can find support through forums, GitHub, and official documentation."
    },
    {
        "question": "What are the deployment options for applications built with CrewAI?",
        "answer": "Applications built with CrewAI can be deployed on various platforms, including cloud services, local servers, and edge devices, depending on your requirements."
    }
]

# Keywords and their associated FAQ indices
KEYWORDS = {
"crewai": [0, 1, 4],
    "uv": [2],
    "install": [1],
    "features": [3],
    "agent": [4],
    "create": [4],
    "programming": [5],
    "real-time": [6],
    "communication": [7],
    "community": [8],
    "deployment": [9],
    "what": [0, 2, 3, 5, 6, 7, 8, 9],
    "how": [1, 4],
    "python": [5],
    "pip": [1]
} 
