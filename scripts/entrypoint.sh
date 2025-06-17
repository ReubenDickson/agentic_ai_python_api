#!/bin/bash
set -e

# Function to check if API key is set
check_api_key() {
    if [ -z "$ANTHROPIC_API_KEY" ]; then
        echo "Error: ANTHROPIC_API_KEY environment variable is not set"
        echo "Please set your Anthropic API key in the environment"
        exit 1
    fi
}

# Function to run health check
health_check() {
    echo "Running health check..."
    python -c "
from api.anthropic_client import AnthropicClient
try:
    client = AnthropicClient()
    print('✅ API client initialized successfully')
except Exception as e:
    print(f'❌ Health check failed: {e}')
    exit(1)
"
}

# Main execution
main() {
    echo "🚀 Starting Anthropic AI Application..."
    
    # Check API key
    check_api_key
    
    # Run health check
    health_check
    
    # Execute the main command
    echo "📋 Executing command: $@"
    exec "$@"
}

# Run main function with all arguments
main "$@"