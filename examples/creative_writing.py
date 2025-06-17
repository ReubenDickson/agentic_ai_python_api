from api.anthropic_client import AnthropicClient
from utils.helpers import print_response

def creative_writing():
    """Creative writing example"""
    client = AnthropicClient()
    
    # Story generation
    prompt = "Write a short story about a robot who discovers they can dream."
    response = client.send_message(
        message=prompt,
        max_tokens=500
    )
    print_response(response, "Creative Story")
    
    # Poetry
    prompt = "Write a haiku about programming."
    response = client.send_message(message=prompt)
    print_response(response, "Programming Haiku")
    
    # Character creation
    system_prompt = "You are a creative writing assistant specialized in character development."
    prompt = "Create a detailed character profile for a cyberpunk detective."
    response = client.send_message(
        message=prompt,
        system_prompt=system_prompt
    )
    print_response(response, "Character Profile")

if __name__ == "__main__":
    creative_writing()