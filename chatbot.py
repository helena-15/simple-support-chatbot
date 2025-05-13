def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",
        "what are your hours": "We are open 24/7!",
        "how can i track my order": "You can track your order by visiting your account > orders > track.",
        "i want to return my order": "To return an order, go to your account > orders > return.",
        "how can i contact support": "You can contact support via email at support@example.com.",
        "bye": "Thank you for visiting! Have a great day!"
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

print("""SupportBot: Hello! I'm here to help you. (Type 'bye' to exit)""")

while True:
    user = input("You: ")
    if "bye" in user.lower():
        print("SupportBot:", get_response("bye"))
        break
    else:
        print("SupportBot:", get_response(user))
