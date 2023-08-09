from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'MMGHTY'
load_dotenv()

# Load greeting and questions from question.txt
greeting = ""
questions = []
with open("question.txt", "r") as f:
    lines = f.readlines()
    greeting = lines[0].strip().split(": ")[1]
    questions = [line.strip() for line in lines[1:]]

# Load answers from answer.txt
answers = {}
with open("answer.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        parts = line.strip().split(": ")
        if len(parts) == 2:
            answers[parts[0]] = parts[1]

# Set up Twilio API
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

# Set up OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to send a message
def sendMessage(body_mess, phone_number):
    print("BODY MESSAGE " + body_mess)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=body_mess,
        to='whatsapp:' + phone_number
    )
    print(message)

# Function to generate a response using GPT-3
def generate_gpt3_response(user_input):
    try:
        prompt = f"User: {user_input}\nAI:"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError:
        return "Sorry, I couldn't generate a response at the moment."

# Main route for handling incoming messages
@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    phone_number = request.values['WaId']

    response = MessagingResponse()

    # Handle known greetings
    if incoming_msg == "Hello" or incoming_msg == "Hi":
        all_questions = "\n".join(questions)
        response.message(f"{greeting}\n{all_questions}")
    # Handle known question numbers
    elif incoming_msg in [str(i + 1) for i in range(len(questions))]:
        question_index = int(incoming_msg) - 1
        response.message(answers.get(str(question_index + 1), "Sorry, I couldn't find an answer for that question."))
    # Handle known answers
    elif incoming_msg in answers:
        response.message(answers[incoming_msg])
        sendMessage(answers[incoming_msg], phone_number)
    # Handle "thank you" messages
    elif "thank you" in incoming_msg.lower():
        response.message("You're welcome! If you have more questions, feel free to ask.")
    # Handle unknown inputs using GPT-3
    else:
        gpt3_response = generate_gpt3_response(incoming_msg)
        if gpt3_response == "Sorry, I couldn't generate a response at the moment.":
            response.message(gpt3_response)
        else:
            response.message(gpt3_response)
            sendMessage(gpt3_response, phone_number)

    return str(response)

if __name__ == '__main__':
    app.run()
