import unittest
from chatbot.order_status import get_order_status
from chatbot.human_representative import request_human_representative
from chatbot.return_policies import get_return_policy
from chatbot.conversation_handler import handle_conversation


class TestChatbot(unittest.TestCase):

    def test_get_order_status(self):
        self.assertEqual(get_order_status("12345"), "The status of order 12345 is 'Shipped'.")

    def test_request_human_representative(self):
        response = request_human_representative("John Doe", "john@example.com", "1234567890")
        self.assertEqual(response, "Your request has been submitted. Our representative will contact you shortly.")

    def test_get_return_policy(self):
        self.assertEqual(get_return_policy("What is the return policy for items purchased at our store?"),
                         "You can return most items within 30 days of purchase for a full refund or exchange. Items must be in their original condition, with all tags and packaging intact. Please bring your receipt or proof of purchase when returning items.")
        self.assertEqual(get_return_policy("Are there any items that cannot be returned under this policy?"),
                         "Yes, certain items such as clearance merchandise, perishable goods, and personal care items are non-returnable. Please check the product description or ask a store associate for more details.")
        self.assertEqual(get_return_policy("How will I receive my refund?"),
                         "Refunds will be issued to the original form of payment. If you paid by credit card, the refund will be credited to your card. If you paid by cash or check, you will receive a cash refund.")

    def test_handle_conversation(self):
        response = handle_conversation("Tell me a joke.")
        self.assertTrue(len(response) > 0)

    def test_accuracy(self):
        questions_and_expected_answers = [
            ("What is the return policy?", "You can return most items within 30 days of purchase"),
            ("How will I receive my refund?", "Refunds will be issued to the original form of payment"),
            ("Who was the first president of the United States?", "George Washington")
        ]

        for question, expected in questions_and_expected_answers:
            response = handle_conversation(question)
            self.assertIn(expected, response, f"Expected '{expected}' in response but got '{response}'")

    def test_relevance(self):
        questions = [
            "What is the return policy?",
            "How will I receive my refund?",
            "Who was the first president of the United States?"
        ]

        for question in questions:
            response = handle_conversation(question)
            relevance_score = int(input(f"Rate the relevance of the response to '{question}': {response} (1-5): "))
            self.assertGreaterEqual(relevance_score, 3, f"Relevance score too low for response: '{response}'")

    def test_user_satisfaction(self):
        questions = [
            "What is the return policy?",
            "How will I receive my refund?",
            "Who was the first president of the United States?"
        ]

        satisfaction_scores = []
        for question in questions:
            response = handle_conversation(question)
            satisfaction_score = int(
                input(f"Rate your satisfaction with the response to '{question}': {response} (1-5): "))
            satisfaction_scores.append(satisfaction_score)

        average_satisfaction = sum(satisfaction_scores) / len(satisfaction_scores)
        self.assertGreaterEqual(average_satisfaction, 4, f"Average satisfaction score too low: {average_satisfaction}")


if __name__ == '__main__':
    unittest.main()
