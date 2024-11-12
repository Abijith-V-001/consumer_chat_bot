# Consumer Chatbot

Welcome to the Consumer Chatbot repository! This chatbot is designed to assist users with e-commerce-related tasks such as returns, refunds, replacements, and general customer support queries. Below are instructions on how to set up and run the chatbot.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

Make sure you have all the necessary Python packages, including Flask, NLTK, and PyTorch.

## Running the Chatbot

Once the dependencies are installed, you can run the Flask app by executing the following command:

```bash
python app.py
```

This will start the chatbot on a local server (usually at `http://127.0.0.1:5000/`), where users can interact with the chatbot via a web interface.

## Project Structure

- **app.py**: The main Flask application that runs the chatbot and handles user input and model predictions.
  
- **templates/index.html**: The HTML template for rendering the chatbot's interface where users can type their queries.

- **src/model.py**: Contains the implementation of the neural network model used for processing and predicting user queries.

- **src/utils.py**: Provides utilities for preprocessing user input, predicting responses, and managing chat history.

- **training/train.py**: The file responsible for training the chatbot's machine learning model.

- **artifacts/intents.json**: A JSON file containing all the intents the model has been trained on, including returns, refunds, replacements, and general queries.

- **artifacts/luffy.pth**: The file that stores the trained model's weights and configuration.

- **artifacts/chat_history.json**: A JSON file used for storing the chat history, including past user queries and bot responses.

## Usage

The Consumer Chatbot can answer various e-commerce-related queries such as order status, returns, refunds, product replacements, and general support inquiries. Users can interact with the chatbot by typing messages into the chat interface, and the bot will respond based on its training and intent mapping.

## Contributors

- ABIJITH V

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use it according to your needs.

If you have any questions or issues, please feel free to contact me at abivandiyil001@gmail.com. Thank you for using the Consumer Chatbot!
