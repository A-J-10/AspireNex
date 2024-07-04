import random

# Dictionary of predefined rules and responses
rules = {
    'greeting': ['Hello!', 'Hi there!', 'Hey!', 'Hi! How can I assist you today?'],
    'goodbye': ['Goodbye!', 'Bye!', 'Have a nice day!', 'See you later!'],
    'thank_you': ['You\'re welcome!', 'My pleasure!', 'No problem.'],
    'options': ['I can help with information, provide recommendations, or answer questions.'],
    'weather': ['The weather is sunny today.', 'It\'s raining outside.', 'Expect snow later.'],
    'time': ['It\'s currently 2:30 PM.', 'The time is 10:00 AM.', 'It\'s evening now.'],
    'joke': ['Why don\'t scientists trust atoms? Because they make up everything!',
             'Parallel lines have so much in common. It’s a shame they’ll never meet.',
             'I told my wife she should embrace her mistakes. She gave me a hug.'],
    'default': ['I\'m not sure I understand.', 'Could you please elaborate?', 'I apologize, I didn\'t get that.']
}

# Function to get response based on user input
def get_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Check for patterns in user input and respond accordingly
    if any(greeting in user_input for greeting in ['hello', 'hi', 'hey']):
        return random.choice(rules['greeting'])
    elif any(goodbye in user_input for goodbye in ['bye', 'goodbye', 'see you']):
        return random.choice(rules['goodbye'])
    elif any(thanks in user_input for thanks in ['thank you', 'thanks']):
        return random.choice(rules['thank_you'])
    elif any(weather in user_input for weather in ['weather', 'rain', 'sun', 'snow']):
        return random.choice(rules['weather'])
    elif any(time in user_input for time in ['time', 'clock']):
        return random.choice(rules['time'])
    elif any(joke in user_input for joke in ['joke', 'funny']):
        return random.choice(rules['joke'])
    elif any(option in user_input for option in ['help', 'recommendations', 'questions']):
        return random.choice(rules['options'])
    else:
        return random.choice(rules['default'])

# Function to simulate the chat interaction
def chat():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)

# Start the chatbot
chat()
