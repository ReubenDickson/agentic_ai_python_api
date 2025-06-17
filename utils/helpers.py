from datetime import datetime
from typing import List, Dict


def format_timestamps() -> str:
    """Return formatted timestamp"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def create_user_message(content: str) -> Dict[str, str]:
    """Create a user message dictionary"""
    return {"role": "user", "content": content}

    
def create_assistant_message(content: str) -> Dict[str, str]:
    """Create an assistant message dictionary"""
    return {"role": "assistant", "content": content}

def print_response(response: str, title: str = "Claude Response"):
    """Pretty print API response"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(response)
    print(f"{'='*50}\n")

def save_conversation(messages: List[Dict[str, str]], filename: str = None):
    """Save conversation to file"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"conversation_{timestamp}.txt"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write("="*50 + "\n\n")

        for message in messages:
            role = message['role'].upper()
            content = message['content']
            f.write(f"{role}: {content}\n\n")

    print(f"Conversation saved to {filename}")