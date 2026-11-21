# Task 4 - Rule-Based Interactive Terminal Assistant / Chatbot
# Datheon Python Programming Internship

import re
import random
from datetime import datetime

# Intent -> Responses Dictionary
INTENTS = {
    "greeting": [
        "Hello! 👋 Main Datheon Assistant hu. Kaise madad kar sakta hu?",
        "Hi! 😊 Batao, kya jaanna hai? Business hours, price ya support?",
        "Namaste! 🙏 Aapka swagat hai. Kuch puchna hai?"
    ],
    "business_hours": [
        "🕙 Hamare business hours:\nMon - Fri: 10 AM - 7 PM\nSat: 11 AM - 4 PM\nSun: Closed",
        "Hum Monday se Friday 10 AM se 7 PM tak khule rehte hai!"
    ],
    "price": [
        "💰 Hamare plans:\nBasic: ₹499/month\nPro: ₹999/month\nPremium: ₹1999/month\nKonsa plan pasand karoge?",
        "Price list bhej du? Basic ₹499, Pro ₹999, Premium ₹1999 hai."
    ],
    "product_faq": [
        "📦 Hamara product Python me bana hai. Ye internship, courses aur projects ke liye best hai. Kya aur detail chahiye?",
        "Product ke baare me: Ye beginner-friendly hai, certificate ke saath aata hai."
    ],
    "support": [
        "🛠️ Support ke liye: support@datheon.in pe mail karo ya yahi pucho, main help kar dunga.",
        "Koi problem hai? Batao kya issue aa raha hai, main solution dunga."
    ],
    "thanks": [
        "Koi baat nahi! 😊 Aur kuch puchna hai?",
        "Welcome! ❤️ Datheon me aane ke liye thanks."
    ],
    "bye": [
        "Bye Bye! 👋 Fir milenge. Datheon yaad rakhna!",
        "Alvida! 😊 Accha laga baat karke."
    ],
    "name": [
        "Mera naam Datheon Bot hai! 🤖 Tumhara naam kya hai?",
        "Main Datheon Assistant hu, jo tumhari help ke liye bana hu."
    ],
    "how_are_you": [
        "Main ekdum mast hu! 😄 Tum batao kaise ho?",
        "Bilkul badhiya! Coding chal rahi hai?"
    ],
    "fallback": [
        "Sorry, main ye samajh nahi paya. 😅 Dobara pucho ya 'help' likho.",
        "Hmm, ye thoda mushkil hai. 'price', 'timing', 'support' me se kuch pucho.",
        "Mujhe samajh nahi aaya. Help ke liye 'help' type karo."
    ]
}

def get_intent(user_input):
    text = user_input.lower().strip()

    # Regex + Keyword based Intent Recognition
    if re.search(r'\b(hi|hello|hey|namaste|hii+)\b', text):
        return "greeting"
    elif re.search(r'\b(bye|exit|quit|alvida)\b', text):
        return "bye"
    elif re.search(r'(business|open|close|timing|hours|kab khulta|time)', text):
        return "business_hours"
    elif re.search(r'(price|cost|fees|kitna|rate|plan|package)', text):
        return "price"
    elif re.search(r'(product|course|internship|kya hai|faq)', text):
        return "product_faq"
    elif re.search(r'(support|help|problem|issue|madad|error)', text):
        return "support"
    elif re.search(r'(thank|thanks|dhanyavad|shukriya)', text):
        return "thanks"
    elif re.search(r'(tumhara naam|your name|naam kya)', text):
        return "name"
    elif re.search(r'(kaise ho|how are you|kaisa hai)', text):
        return "how_are_you"
    else:
        return "fallback"

def main():
    print("="*55)
    print("  DATHEON CHATBOT - Task 4 🤖")
    print("  Type 'bye' / 'exit' / 'quit' to stop")
    print("="*55)
    print("Bot: Hello! Main Datheon Assistant hu. 'help' likh ke dekh.")
    print("-"*55)

    while True:
        user = input("You: ").strip()
        if not user:
            continue

        intent = get_intent(user)

        if intent == "bye":
            print(f"Bot: {random.choice(INTENTS['bye'])}")
            break
        
        if user.lower() == "help":
            print("Bot: Tum ye puch sakte ho:")
            print(" - Business hours / Timing")
            print(" - Price / Plans")
            print(" - Product / Course info")
            print(" - Support / Help")
            continue

        response = random.choice(INTENTS[intent])
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()
