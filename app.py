from flask import Flask, request, jsonify, render_template
import json
import random
import torch
import nltk

from src.model import NeuralNet
from src.utils import (
    preprocess_user_input,
    predict, load_chat_history, save_chat_history
)

# Initialize Flask app
app = Flask(__name__, template_folder='templates')

# Download required NLTK data
nltk.download('punkt')

# Load intents file
with open(r'artifacts/intents.json', 'r') as f:
    intents = json.load(f)

# Load pre-trained model data
FILE = r"artifacts/luffy.pth"
data = torch.load(FILE, weights_only=True)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

# Set device for model
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Bot name
bot_name = "LUFFY"

# Define the home route
@app.route("/")
def home():
    return render_template("index.html")  # You'll need to create an HTML file for the interface

# Define a route for the chatbot response
@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("user_input")
    
    # If the user types 'exit', reset chat history
    if user_input.lower() == "exit":
        chat_history = []
        save_chat_history(chat_history)
        return jsonify({"bot_response": "Chat history cleared. Type a message to restart."})
    
    # Load chat history
    chat_history = load_chat_history()

    # Append user input to chat history
    chat_history.append(("You", user_input))

    # Process user input and get model prediction
    output = model(preprocess_user_input(user_input, all_words, device))
    tag, prob = predict(output, tags)

    # Check if the model's confidence is above 75%
    if prob.item() > 0.75:
        for intent in intents["intents"]:
            if tag == intent["tag"]:
                bot_response = random.choice(intent['responses'])
                chat_history.append((bot_name, bot_response))
    else:
        bot_response = "I do not understand..."
        chat_history.append((bot_name, bot_response))

    # Save chat history after response
    save_chat_history(chat_history)

    return jsonify({"bot_response": bot_response})

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
