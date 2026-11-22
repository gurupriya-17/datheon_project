
import re
import random

# Chatbot response dictionary
responses = {

    "greeting": [
        "Hello! Welcome to Customer Support.",
        "Hi! How can I help you today?",
        "Welcome! What can I do for you?"
    ],

    "hours": [
        "Our business hours are Monday to Saturday, 9 AM to 6 PM."
    ],

    "products": [
        "We offer laptops, mobile phones and accessories."
    ],

    "price": [
        "Our product prices depend on the model you choose."
    ],

    "delivery": [
        "Delivery usually takes 3 to 5 business days."
    ],

    "payment": [
        "We accept UPI, credit cards, debit cards and cash on delivery."
    ],

    "return": [
        "Products can be returned within 7 days of delivery."
    ],

    "contact": [
        "You can contact our support team at support@example.com."
    ],

    "thanks": [
        "You're welcome! Happy to help.",
        "Thank you for contacting us!",
        "Glad I could help!"
    ]
}


# Keyword and regular expression patterns
patterns = {

    "greeting": r"\b(hello|hi|hey|good morning|good evening)\b",

    "hours": r"\b(hours|timing|open|close|working time)\b",

    "products": r"\b(product|products|laptop|mobile|phone|accessories)\b",

    "price": r"\b(price|cost|rate|amount|expensive)\b",

    "delivery": r"\b(delivery|shipping|shipment|order status)\b",

    "payment": r"\b(payment|pay|upi|cash|card)\b",

    "return": r"\b(return|refund|exchange|replace)\b",

    "contact": r"\b(contact|email|support|phone number)\b",

    "thanks": r"\b(thank you|thanks|thank)\b"
}


def get_response(user_input):

    # Normalize input
    text = user_input.lower().strip()

    # Check for empty input
    if not text:
        return "Please enter your question."

    # Identify intent
    for intent, pattern in patterns.items():

        if re.search(pattern, text):

            return random.choice(responses[intent])

    # Fallback response
    return (
        "Sorry, I didn't understand your question. "
        "Please ask about products, prices, delivery, "
        "business hours or payments."
    )


def chatbot():

    print("\n===================================")
    print("   CUSTOMER SUPPORT CHATBOT")
    print("===================================")

    print("Bot: Hello! Welcome to our support service.")
    print("Bot: How can I help you today?")
    print("Bot: Type 'bye' or 'exit' to end the chat.")

    while True:

        user_input = input("\nYou: ").strip()

        # Exit commands
        if re.fullmatch(r"(bye|exit|quit)", user_input, re.IGNORECASE):

            print("Bot: Thank you for visiting. Goodbye!")
            break

        # Generate response
        answer = get_response(user_input)

        print("Bot:", answer)


# Start chatbot
if __name__ == "__main__":
    chatbot()
