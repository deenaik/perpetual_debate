# Introduction:
This web app is called "perpetual_debate". 

# Description:
This app will display live conversation between two bots. 
User can give a topic as an input and then two ai agents (bots) one with positive and one another with negative perspective will discuss the topic with each others. 
The user can stop the discussion by pressing a button. 

# Tech stack: 
Python as a backend, 
React as a frontend.

# Model:
It use API of already running local model on Ollama which is available on "http://localhost:11434/api" 
The API doc for the same is here: https://github.com/ollama/ollama/blob/main/docs/api.md

# Steps to develop the app:

## Backend development:

 1. Create a Python Flask app: This will serve as the backend for web app.
 2. Import the Ollama API: This will allow to access the Ollama model and generate text responses.
 3. Define the routes for app: Need to define routes for the user to input a topic and start the debate, as well as a route to stop the debate.
 4. Handle the user input: When the user inputs a topic, store it in a variable and pass it to the Ollama model.
 5. Generate text responses using the Ollama model: The Ollama model will generate text responses for both the positive and negative bots based on the input topic.
 6. Display the text responses to the user: Display the text responses from the Ollama model to the user in real time.
 7. Handle the stop button: When the user presses the stop button, stop the debate and clear the input field.

## Frontend development:

 1. Create a React app: This will serve as the frontend for web app.
 2. Import the React components needed: Import components for displaying the text responses from the Ollama model, as well as a component for the stop button.
 3. Render the React components: Render the React components in the appropriate places in app.
 4. Handle the user input: Need to handle the user input for the topic and the stop button.
 5. Communicate with the backend: Need to communicate with the backend to get the text responses from the Ollama model and to stop the debate.

## Additional considerations:

 1. Handle errors and exceptions that may occur during the development and execution of app.
 2. Add additional features to app, such as the ability to save debates or to change the length of the debate.
