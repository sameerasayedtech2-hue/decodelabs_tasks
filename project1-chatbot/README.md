# Project 1: Rule-Based AI Chatbot

## Overview
This is a simple rule-based chatbot built in Python as part of the DecodeLabs
AI Internship Training Kit. It responds to predefined user inputs using
if-elif-else logic and runs in a continuous loop until the user exits.

## Features
- Handles greetings (hello, hi, hey)
- Answers basic predefined questions (how are you, what is your name)
- Provides a fallback response for unrecognized input
- Runs in a continuous loop using `while True`
- Exits cleanly when the user types "bye" or "exit"

## How to Run
1. Make sure Python is installed on your system.
2. Open a terminal in this folder.
3. Run the file:    python chatbot.py
4. Type messages when prompted with "You: "
5. Type "bye" to exit the chatbot.

## Key Concepts Used
- Control flow (if-elif-else)
- Loops (while)
- String handling (.lower(), .strip())
- Basic decision-making logic

## Example Interaction
Bot: Hello! I am your AI Chatbot. Type 'bye' to exit.

You: hello
Bot: Hello! Nice to meet you.

You: how are you
Bot: I am doing great! Thanks for asking.

You: bye
Bot: Goodbye! Have a great day!
