#!/usr/bin/claude_env python3
"""
Main application for Anthropic AI API Examples
"""

import os
import sys
from api.anthropic_client import AnthropicClient
from utils.helpers import (
    print_response,
    create_user_message,
    create_assistant_message,
    save_conversation
)
def check_docker_environment():
    """Check if running in Docker and display info"""
    if os.path.exists('/.dockerenv'):
        print("🐳 Running in Docker container")
        print(f"📁 Working directory: {os.getcwd()}")
        print(f"🐍 Python path: {os.environ.get('PYTHONPATH', 'Not set')}")
    return os.path.exists('/.dockerenv')


def interactive_chat():
    """Interactive chat with Cluade"""
    client = AnthropicClient()
    conversation = []

    print("Welcome to Claude Chat! Type 'quit' to exit, 'save' to save conversation.")
    print("-" * 60)

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        elif user_input.lower() == 'save':
            save_conversation(conversation)
            continue
        elif not user_input:
            continue

        # Add user message to conversation
        conversation.append(create_user_message(user_input))

        # Get response from Claude
        response = client.chat_conversation(conversation)

        #Add Cluade's response to conversation
        conversation.append(create_assistant_message(response))

        # Display response
        print(f"\nClaude: {response}")
    
def run_examples():
    """Run all examples scripts"""
    try:
        print("Running Simple Chat Example...")
        from examples.simple_chat import simple_chat
        simple_chat()

        print("\nRunning Text Analysis Example...")
        
        from examples.text_analysis import text_analysis
        text_analysis()

        print("\nRunning Creative Writing Example...")
        from examples.creative_writing import creative_writing
        creative_writing()
        
    except Exception as e:
        print(f"Error running examples: {e}")

def main():
    """Main application entry point"""
    is_docker = check_docker_environment()

    """Main application entry point"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == 'chat':
            interactive_chat()
        elif command == 'examples':
            run_examples()
        else:
            print("Usage: python main.py [chat|examples]")
    else:
        print("Anthropic AI API Application")
        print("Available commands:")
        print(" python main.py chat     - Start interactive chat")
        print(" python main.py examples     - Run example scrips")

if __name__ == "__main__":
    main()