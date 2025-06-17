from api.anthropic_client import AnthropicClient
from utils.helpers import print_response

def text_analysis():
    """Text analysis example"""
    client = AnthropicClient()

    text_to_analyze = """
    Artificial intelligence is transforming how we work, learn, and interact with technology. 
    From chatbots to autonomous vehicles, AI applications are becoming increasingly sophisticated 
    and accessible to everyday users.
    """
    
    # Sentiment analysis
    message = f"Analyze the sentiment of this text: {text_to_analyze}"
    reponse = client.send_message(message)
    print_response(response, "Sentiment Analysis")

    # Summarization
    message = f"Summarize this text in one sentence: {text_to_analyze}"
    response = client.send_message(message)
    print_response(response, "Text Summarization")

    # Key points extraction
    message = f"Extract the key points from this text: {text_to_analyze}"
    response = client.send_message(message)
    print_response(response, "Key Points Extraction")

if __name__ == "__main__":
    text_analysis()