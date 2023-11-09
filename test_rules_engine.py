
import unittest
from rules_engine import RulesEngine
from person import Person
from product import Product

class TestRulesEngine(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rules = RulesEngine.load_rules_from_json('rules.json')

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

    def test_interest_rate_adjustment_for_credit_score_of_720(self):
        engine = RulesEngine(self.rules)
        person = Person(720, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.2, "Interest rate should be adjusted to 5.2 for credit score 720")

    def test_interest_rate_adjustment_for_credit_score_over_720(self):
        engine = RulesEngine(self.rules)
        person = Person(730, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.2, "Interest rate should be adjusted to 5.2 for credit score 730")

    def test_interest_rate_adjustment_for_credit_score_below_720(self):
        engine = RulesEngine(self.rules)
        person = Person(710, 'Florida')
        product = Product('7-1 ARM')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 6.0, "Interest rate should be adjusted to 6.0 for credit score 710")


    def test_unrecognized_product_name(self):
        engine = RulesEngine(self.rules)
        person = Person(710, 'Texas')
        product = Product('Unknown Product')
        engine.run_rules(person, product)
        self.assertEqual(product.interest_rate, 5.5, "Interest rate should remain at the default for an unrecognized product name")
        self.assertFalse(product.disqualified, "Product should not be disqualified if the product name is unrecognized")

# If this file is run directly, run the tests
if __name__ == '__main__':
    unittest.main()
