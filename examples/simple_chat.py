from api.anthropic_client import anthropicClent
from utils.helpers import print response

def simple_chat():
    """Basic single messages"""
    client = AnthropicClient()

    # Simple question
    message = "Explain what artificial intelligence is in simple terms."
    response = client.send_messages(message)
    print_response(response, "Simple Chat Example")

    # With system prompt
    system_prompt = "You are a helpful coding assistant"
    message = "Write a simple Python function to calculate factorial"
    response = client.send_message(
        message=message,
        system_prompt=system_prompt
    )
    print_response(response, "Coding Assistant Example")

if __name__ == "__main__":
    simple_chat()