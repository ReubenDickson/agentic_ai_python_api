# Anthropic AI Python Client

A simple Python application for making API calls to Anthropic's Claude AI. This project serves as a foundation for learning agentic AI applications and demonstrates basic API integration patterns. I built this maily for the purpose of experimenting CICD pipelines for Agentic AI Applications with Python.

## 🚀 Features

- **Simple API Integration**: Easy-to-use wrapper for Anthropic's Claude API
- **Multiple Examples**: Text analysis, creative writing, and interactive chat
- **Conversation Management**: Save and manage chat conversations
- **Modular Design**: Clean separation of concerns for easy extension
- **Interactive CLI**: Command-line interface for real-time interactions
- **Environment Configuration**: Secure API key management

## 📁 Project Structure

```
anthropic-ai-app/
│
├── .env                    # Environment variables (API key)
├── .gitignore             # Git ignore file
├── requirements.txt       # Python dependencies
├── config.py             # Configuration settings
├── main.py               # Main application entry point
├── README.md             # Project documentation
├── api/
│   ├── __init__.py
│   └── anthropic_client.py  # Anthropic API client wrapper
├── examples/
│   ├── __init__.py
│   ├── simple_chat.py      # Basic chat example
│   ├── text_analysis.py   # Text analysis example
│   └── creative_writing.py # Creative writing example
└── utils/
    ├── __init__.py
    └── helpers.py         # Utility functions
```

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- Anthropic API key (get one at [console.anthropic.com](https://console.anthropic.com/))

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/anthropic-ai-app.git
   cd anthropic-ai-app
   ```

2. **Create and activate virtual environment:**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Copy `.env.example` to `.env` (if provided) or create a new `.env` file
   - Add your Anthropic API key:
   ```
   ANTHROPIC_API_KEY=your_api_key_here
   DEFAULT_MODEL=claude-3-5-sonnet-20241022
   MAX_TOKENS=1000
   ```

## 🎯 Usage

### Interactive Chat
Start a conversation with Claude:
```bash
python main.py chat
```

### Run All Examples
Execute all example scripts:
```bash
python main.py examples
```

### Run Individual Examples
```bash
python examples/simple_chat.py
python examples/text_analysis.py
python examples/creative_writing.py
```

## 📚 Examples

### Simple Chat
```python
from api.anthropic_client import AnthropicClient

client = AnthropicClient()
response = client.send_message("Explain quantum computing in simple terms.")
print(response)
```

### Text Analysis
```python
from api.anthropic_client import AnthropicClient

client = AnthropicClient()
text = "Your text here..."
response = client.send_message(f"Analyze the sentiment of: {text}")
print(response)
```

### Conversation History
```python
from api.anthropic_client import AnthropicClient
from utils.helpers import create_user_message, create_assistant_message

client = AnthropicClient()
conversation = [
    create_user_message("Hello, how are you?"),
    create_assistant_message("I'm doing well, thank you!"),
    create_user_message("Can you help me with Python?")
]

response = client.chat_conversation(conversation)
print(response)
```

## 🔧 Configuration

The application uses environment variables for configuration:

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key | **Required** |
| `DEFAULT_MODEL` | Claude model to use | `claude-3-5-sonnet-20241022` |
| `MAX_TOKENS` | Maximum tokens in response | `1000` |

## 📊 API Client Methods

### `send_message(message, model=None, max_tokens=None, system_prompt=None)`
Send a single message to Claude.

**Parameters:**
- `message` (str): The user message
- `model` (str, optional): Model to use
- `max_tokens` (int, optional): Maximum response tokens
- `system_prompt` (str, optional): System prompt for context

### `chat_conversation(messages, model=None, max_tokens=None, system_prompt=None)`
Send a conversation history to Claude.

**Parameters:**
- `messages` (List[Dict]): List of message dictionaries
- `model` (str, optional): Model to use
- `max_tokens` (int, optional): Maximum response tokens
- `system_prompt` (str, optional): System prompt for context

## 🛡️ Error Handling

The client includes basic error handling for:
- Missing API keys
- Network issues
- API rate limits
- Invalid requests

## 📝 Logging

Conversations can be saved to files using the utility functions:
```python
from utils.helpers import save_conversation

# Save conversation to timestamped file
save_conversation(messages)

# Save to specific filename
save_conversation(messages, "my_conversation.txt")
```

## 🚧 Development

### Adding New Examples
1. Create a new file in the `examples/` directory
2. Import the `AnthropicClient` and utility functions
3. Follow the existing example patterns
4. Add your example to the main examples runner

### Extending the API Client
The `AnthropicClient` class can be extended with additional methods for specific use cases:
- Streaming responses
- Function calling
- Custom model parameters
- Response parsing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 🔒 Security

- Never commit your API keys to version control
- The `.env` file is included in `.gitignore` for security
- Use environment variables for sensitive configuration

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

**"ANTHROPIC_API_KEY not found"**
- Ensure your `.env` file exists and contains your API key
- Make sure the `.env` file is in the project root directory

**"Module not found" errors**
- Activate your virtual environment
- Install dependencies: `pip install -r requirements.txt`

**API rate limit errors**
- Check your API usage at [console.anthropic.com](https://console.anthropic.com/)
- Implement rate limiting in your application

### Getting Help

- Check the [Anthropic API documentation](https://docs.anthropic.com/)
- Review the example files for usage patterns
- Open an issue on GitHub for bugs or questions

## 🎓 Learning Resources

This project is part of a 30-day agentic AI bootcamp. Recommended next steps:

1. **Add streaming responses** for real-time chat
2. **Implement function calling** for tool use
3. **Add memory management** for longer conversations
4. **Build a web interface** with Flask/FastAPI
5. **Explore advanced prompting** techniques
6. **Add monitoring and logging** for production use

## 🏷️ Version History

- **v1.0.0** - Initial release with basic API integration and examples

---

Built with ❤️ for learning agentic AI applications