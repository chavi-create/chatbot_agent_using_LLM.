return_policies = {
    "general_policy": "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.",
    "non_returnable_items": "Certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.",
    "refund_method": "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund."
}

def get_return_policy(query):
    if "items purchased" in query:
        return return_policies["general_policy"]
    elif "non-returnable" in query:
        return return_policies["non_returnable_items"]
    elif "receive my refund" in query:
        return return_policies["refund_method"]
    else:
        return "I'm sorry, I don't have information on that specific query. Please ask about general return policies, non-returnable items, or refund methods."
