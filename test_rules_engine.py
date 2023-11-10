
import unittest
from unittest.mock import patch
from rules_engine import RulesEngine
from person import Person
from product import Product
from user_input import get_valid_state
from rules_loader import load_rules

class TestRulesEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = load_rules()

    def test_invalid_state_input(self):
        with patch('builtins.input', side_effect=['123', '!@#', 'ValidState']):
            state = get_valid_state()
            self.assertTrue(state.isalpha(), "The state should not contain numbers or special characters.")

    def test_disqualified_state(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertTrue(product.disqualified, "Product should be disqualified for the state of Florida")

    def test_non_disqualified_state(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Illinois')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertFalse(product.disqualified, "Product should not be disqualified for the state of Illinois")

    def test_non_disqualified_state(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Illinois')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertFalse(product.disqualified, "Product should not be disqualified for the state of Illinois")

    def test_interest_rate_adjustment_for_credit_score_of_720(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.2, "Interest rate should be adjusted to 5.2 for credit score of 720")

    def test_interest_rate_adjustment_for_credit_score_over_720(self):
        engine = RulesEngine(self.rules)
        person = Person(730, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.2, "Interest rate should be adjusted to 5.2 for credit score of 730")

    def test_interest_rate_adjustment_for_credit_score_below_720(self):
        engine = RulesEngine(self.rules)
        person = Person(710, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 6.0, "Interest rate should be adjusted to 6.0 for credit score of 710")

    def test_alternative_product(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Texas')
        product = Product('7-2 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.3, "Interest rate should be adjusted to 5.3 for product 7-2 ARM")       

# If this file is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
