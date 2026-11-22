
"""Interactive terminal client for the AI Q&A Chatbot."""

import os

# Configure Django before using the chatbot database.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "chatbot_project.settings",
)

import django

django.setup()

from chatterbot import ChatBot
from django.conf import settings


def create_chatbot():
    """Initialize ChatterBot using Django project settings."""
    return ChatBot(**settings.CHATTERBOT)


def start_chat():
    """Start an interactive conversation in the terminal."""
    print("=" * 50)
    print("        Welcome to the AI Q&A Chatbot!")
    print("=" * 50)
    print("Type 'exit' to end the conversation.\n")

    try:
        chatbot = create_chatbot()
    except Exception as error:
        print(f"Unable to initialize chatbot: {error}")
        return

    while True:
        try:
            user_input = input("You: ").strip()

            # Ignore empty messages.
            if not user_input:
                print("Bot: Please enter a question.")
                continue

            # Allow the user to end the conversation.
            if user_input.lower() in ("exit", "quit"):
                print("Bot: Goodbye! Have a great day!")
                break

            # Generate a response using the trained chatbot.
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! Have a great day!")
            break

        except Exception as error:
            print(f"Bot: An error occurred: {error}")


if __name__ == "__main__":
    start_chat()
