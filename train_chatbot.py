
"""Train the AI Q&A Chatbot using predefined conversations."""

import os

# Configure Django before importing models or ChatterBot.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "chatbot_project.settings",
)

import django

django.setup()

from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

from chatbot_app.training_data import TRAINING_CONVERSATIONS


def main():
    """Train the chatbot and save conversations to the database."""

    print("Initializing AI Q&A Chatbot...")

    # Reuse the project's Django and ChatterBot configuration.
    chatbot = ChatBot(
        **{
            **settings.CHATTERBOT,
            "read_only": False,
        }
    )

    # Create a trainer for predefined conversation pairs.
    trainer = ListTrainer(chatbot)

    print("Training started...")

    for conversation in TRAINING_CONVERSATIONS:
        trainer.train(conversation)

    print("Training completed successfully!")
    print(f"Trained {len(TRAINING_CONVERSATIONS)} conversations.")


if __name__ == "__main__":
    main()
