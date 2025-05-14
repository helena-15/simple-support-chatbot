def get_response(user_input):
    user_input = user_input.lower()

    responses = {
        "hello": "Hi there! How can I assist you today?",
        "hi": "Hello! How can I help you?",

        # App-specific queries:
        "what are your hours": "We are open 24/7!",
        "when are you open": "We are open 24/7!",
        "how can i track my order": "You can track your order by visiting your account > orders > track.",
        "where is my order": "You can track your order by visiting your account > orders > track.",
        "i want to return my order": "To return an order, go to your account > orders > return.",
        "how do i return something": "To return an order, go to your account > orders > return.",
        "how can i contact support": "You can contact support via email at support@example.com.",
        "email support": "You can contact support via email at support@example.com.",
        "what is your phone number": "You can call us at 1-800-123-4567.",
        "do you offer free shipping": "Yes, we offer free shipping on orders over $50.",
        "how long does shipping take": "Shipping usually takes 3-5 business days.",
        "what is your return policy": "Our return policy allows returns within 30 days of purchase with a receipt.",
        "how do i change my password": "To change your password, go to your account settings and click on 'Change Password'.",
        "how can i update my address": "You can update your shipping address in your account settings under 'Addresses'.",
        "do you ship internationally": "Yes, we offer international shipping to select countries.",
        "what payment methods do you accept": "We accept major credit cards, PayPal, and Apple Pay.",
        "how do I cancel my order": "To cancel an order, please contact us within 24 hours of placing the order.",

        # General conversational queries:
        "how are you": "I'm doing well, thank you for asking!",
        "what is your name": "I am a chatbot.",
        "what can you do": "I can answer your questions and have a conversation with you.",
        "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "how's the weather": "I don't have access to real-time weather information, but you can check a weather website or app.",
        "what time is it": "I don't have access to real-time time information.",
        "what is your favorite color": "I don't have personal preferences like a favorite color.",

        # Exit queries:
        "bye": "Thank you for chatting with me! Have a great day!",
        "goodbye": "Thank you for chatting with me! Have a great day!",
        "see you later": "Goodbye! Come back anytime."
    }

    for key in responses:
        if key in user_input:
            return responses[key]

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

print("""Chatbot: Hello! I'm here to help you with both app-specific and general questions. (Type 'bye' to exit)""")

while True:
    user = input("You: ")
    if "bye" in user.lower():
        print("Chatbot:", get_response("bye"))
        break
    else:
        print("Chatbot:", get_response(user))
