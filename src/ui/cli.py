import argparse

from ..agents.basic_agent import ChatAgent

def main():
    parser = argparse.ArgumentParser(description='Run the Chat Agent')
    parser.add_argument('--model', type=str, default='gpt-3.5-turbo', help='Model to use for the chat agent')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('--base-url', type=str, default=None, help='Base URL for the model API endpoint')
    args = parser.parse_args()
    
    # Initialize and run the chat agent
    agent = ChatAgent(model=args.model, verbose=args.verbose)
    agent.run()

if __name__ == '__main__':
    main()