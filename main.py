from chatbot.order_status import get_order_status
from chatbot.human_representative import request_human_representative
from chatbot.return_policies import get_return_policy
from chatbot.conversation_handler import handle_conversation

def chatbot(user_input):
    if "order status" in user_input.lower():
        order_id = input("Please provide your order ID: ")
        return get_order_status(order_id)
    elif "speak to human" in user_input.lower() or "human representative" in user_input.lower():
        full_name = input("Please provide your full name: ")
        email = input("Please provide your email: ")
        phone = input("Please provide your phone number: ")
        return request_human_representative(full_name, email, phone)
    elif "return policy" in user_input.lower():
        return get_return_policy(user_input.lower())
    else:
        return handle_conversation(user_input)

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        response = chatbot(user_input)
        print(f"Chatbot: {response}")
