
import json
from person import Person
from product import Product
from user_input import get_person_details, get_product_details

class RulesEngine:
    def __init__(self, rules, default_interest_rate=5):
        self.rules = rules
        self.default_interest_rate = default_interest_rate

    def run_rules(self, person, product):
        for rule in self.rules:
            if eval(rule['condition']):
                action = rule['action']
                if action == 'disqualify':
                    product.disqualified = True
                elif action == 'adjust_interest_rate':
                    amount = rule['parameters']['amount']
                    product.interest_rate += amount

def load_rules_from_json(file_path):
    with open(file_path, 'r') as file:
        rules = json.load(file)
    return rules

# Example usage with configurable default interest rate:
if __name__ == '__main__':
    # Load the rules from the updated JSON file.
    rules = load_rules_from_json('rules.json')
    
    # Get user input for the Person details.
    credit_score, state = get_person_details()
    product_name = get_product_details()
    
    # Create an instance of Product with an initial interest rate of 0.
    product_example = Product(product_name, 0)
    
    # Create an instance of RulesEngine with the default interest rate.
    rules_engine = RulesEngine(rules, default_interest_rate=5)
    
    # Create an instance of Person with the user input.
    person_example = Person(credit_score, state)
    
    # Run the rules engine with the provided details.
    # This will set the default interest rate before applying any other rules.
    rules_engine.run_rules(person_example, product_example)
    
    # Output the results.
    print('\nResults:')
    print(f'Product Interest Rate: {product_example.interest_rate}')
    print(f'Product Disqualified: {product_example.disqualified}')
