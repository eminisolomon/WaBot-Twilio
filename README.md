# WhatsApp Chatbot with Flask and OpenAI GPT-3 Integration

This is a simple WhatsApp chatbot built using Flask that responds to user messages, provides answers to predefined questions, and uses OpenAI's GPT-3 for generating responses to unrecognized questions.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contact](#contact)

## Prerequisites

- Python (>=3.6)
- Twilio Account SID and Auth Token (for sending WhatsApp messages)
- OpenAI API Key (for using GPT-3)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Bettcom/Bettcom-gmail.com.git
   cd whatsapp-chatbot

   ```

2. Create and activate a virtual environment:

   On Windows:
   python -m venv venv
   venv\Scripts\activate

   On Linux:
   python3 -m venv venv
   source venv/bin/activate

3. Install the required Python packages:
   pip install -r requirements.txt

4. Create a Twilio account and obtain your Account SID and Auth Token. Set them in the .env file by cpying from .env.example:
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   OPENAI_API_KEY=your_openai_api_key

5. Create your list of questions in question.txt and their corresponding answers in answer.txt.

## Usage

1. NGROK Local Deployment:

   Now download ngrok

    https://ngrok.com/download
    Extract the zip and add the folder to the environment variables
    Login to ngrok website: https://dashboard.ngrok.com/get-started/setup

    run ngrok config add-authtoken in terminal
    run ngrok http 5000
    The output should be like
    


2. Run the Flask application:

   python main.py

   Your Flask app will be available at http://localhost:5000.

3. Configuration

   - main.py: This is the main Flask application file that handles incoming WhatsApp messages, predefined questions, and GPT-3 integration.

   - answer.txt: List of predefined answers to questions in the format <question_number>: <answer>, one answer per line.

   - question.txt: List of predefined questions in the format <question_number>: <question>, one question per line. The first line should contain the greeting.

   - .env: Environment variables file containing Twilio and OpenAI API keys.

   - requirements.txt: List of Python packages required for the project.
