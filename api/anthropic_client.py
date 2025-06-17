import anthropic
from typing import List, Dict, Optional
from config import Config

class AnthropicClient:
    def __inti__(self):
        Config.validate()
        self.client = anthropic.Anthropic(api_key=Config.ANTHROPIC_API_KEY)
        self.default_model = Config.DEFAULT_MODEL
        self.max_tokens = config.MAX_TOKENS

    def send_message(
        self,
        message: str,
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """Send a single message to Claude and get a response"""
        try:
            messages = [{"role": "user", "content": message}]

            kwargs = {
                "model": model or self.default_model,
                "max_tokens": max_tokens or self.max_tokens,
                "messages": messages
            }

            if system_prompt:
                kwargs["system"] = system_prompt

            response = self.client.messages.create(**kwargs)
            return response.content[0].text

        except Exception as e:
            return f"Error: {str(e)}"
            

    def chat_conversation(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> str:
        """Send a conversation history to Claude"""
        try:
            kwargs = {
                "model": model or self.default_model,
                "max_tokens": max_tokens or self.max_tokens,
                "messages": messages
            }

            if system_prompt:
                kwargs["system"] = system_prompt

            response = self.client.messages.create(**kwargs)
            return response.content[0].text
        
        except Exception as e:
            return f"Error: {str(e)}"