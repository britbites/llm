#!/usr/bin/env python3
"""
Simple LLM CLI for a-Shell on iPhone
Compatible with devices that don't support all llm dependencies

Usage:
    python llm_simple.py "Your prompt here"
    python llm_simple.py -m gpt-4o "Your prompt here"

Environment Variables:
    OPENAI_API_KEY - Your OpenAI API key (required)
"""

import sys
import os
from openai import OpenAI


def print_help():
    """Print help message"""
    print(__doc__)


def main():
    # Check for help flag
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        print_help()
        return

    # Get API key from environment
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Set it with: export OPENAI_API_KEY='sk-your-key-here'")
        print("Or add to ~/.profile for persistence")
        return 1

    # Parse arguments
    model = "gpt-4o-mini"  # Default model
    prompt_args = sys.argv[1:]

    # Check for model flag
    if len(sys.argv) > 2 and sys.argv[1] in ['-m', '--model']:
        model = sys.argv[2]
        prompt_args = sys.argv[3:]

    # Get prompt from remaining args
    if not prompt_args:
        print("Error: No prompt provided")
        print_help()
        return 1

    prompt = ' '.join(prompt_args)

    try:
        # Create OpenAI client
        client = OpenAI(api_key=api_key)

        # Send request
        print(f"Prompting {model}...")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        # Print response
        print("\n" + "=" * 60)
        print(response.choices[0].message.content)
        print("=" * 60 + "\n")

        return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    exit(main() or 0)
