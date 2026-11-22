
# AI Q&A Chatbot Using Django, Python, and ChatterBot

## Project Overview

This project implements a simple terminal-based Q&A chatbot
using Python, Django, and ChatterBot.

The chatbot is trained using predefined conversations and
provides responses to greetings and questions about Python,
Django, artificial intelligence, and machine learning.

## Technologies Used

- Python 3.12
- Django 5.2.19
- ChatterBot 1.2.17
- spaCy English Language Model
- SQLite Database
- Visual Studio Code

## Features

- Interactive terminal-based conversation
- Machine-learning-based response selection
- Training with predefined question-and-answer pairs
- Django database integration
- Handling of empty user input
- Graceful termination using exit or quit
- Basic exception handling

## Project Structure

- chatbot.py: Interactive terminal client
- train_chatbot.py: Chatbot training script
- requirements.txt: Python dependencies
- chatbot_app/training_data.py: Training conversations
- chatbot_project/settings.py: Django configuration
- manage.py: Django management utility

## Installation Instructions

### 1. Clone the repository

Clone this repository and open its directory.

### 2. Create a virtual environment

python3.12 -m venv .venv

### 3. Activate the environment

source .venv/bin/activate

### 4. Install dependencies

python -m pip install -r requirements.txt

### 5. Install the spaCy English model

python -m spacy download en_core_web_sm

### 6. Prepare the database

python manage.py makemigrations django_chatterbot

python manage.py migrate

### 7. Train the chatbot

python train_chatbot.py

### 8. Start the chatbot

python chatbot.py

## Sample Conversation

You: Hello
Bot: Hi! How can I help you?

You: What is Python?
Bot: Python is a high-level programming language.

You: What is Django?
Bot: Django is a Python web framework.

You: exit
Bot: Goodbye! Have a great day!

## Limitations

The chatbot uses a limited training dataset.

Questions that differ significantly from trained examples
may produce fallback responses.

## Future Improvements

- Expand the conversation dataset
- Improve natural-language understanding
- Add a web-based chat interface
- Develop automated chatbot tests

## Academic Purpose

Developed for Hands-On Assignment 3:
Create a Simple Q&A Chatbot with Python.

## References

Russell, S. J., & Norvig, P. (2020).
Artificial intelligence: A modern approach (4th ed.).
Pearson.

ChatterBot Documentation:
https://docs.chatterbot.us/

Django Documentation:
https://docs.djangoproject.com/
