
import json
from person import Person
from product import Product

class RulesEngine:
    def __init__(self, rules):
        self.rules = rules

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

# Example usage with user input:
if __name__ == '__main__':
    # Load the rules from the JSON file.
    rules = load_rules_from_json('rules.json')
    rules_engine = RulesEngine(rules)
    
    # Get user input for the Person and Product details.
    credit_score = int(input('Enter the credit score: '))
    state = input('Enter the state: ')
    product_name = input('Enter the name of the product: ')
    interest_rate = float(input('Enter the interest rate of the product: '))
    
    # Create instances of Person and Product with the user input.
    person_example = Person(credit_score, state)
    product_example = Product(product_name, interest_rate)
    
    # Run the rules engine with the provided details.
    rules_engine.run_rules(person_example, product_example)
    
    # Output the results.
    print('\nResults:')
    print(f'Product Interest Rate: {product_example.interest_rate}')
    print(f'Product Disqualified: {product_example.disqualified}')
