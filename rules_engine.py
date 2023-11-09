from rules_loader import load_rules
from person import Person
from product import Product
from user_input import get_person_details, get_product_details

class RulesEngine:
    def __init__(self, rules):
        self.rules = rules
 
    def run_rules(self, person, product):
        for rule in self.rules:
            if eval(rule['condition']):
                action = rule['action']
                if action == 'set_default_interest_rate':
                    # Set the default interest rate from the rule
                    product.interest_rate = rule['parameters']['amount']
                elif action == 'disqualify':
                    product.disqualified = True
                elif action == 'adjust_interest_rate':
                    # Adjust the interest rate based on the rule
                    amount = rule['parameters']['amount']
                    product.interest_rate += amount

if __name__ == '__main__':
    # Load the rules from the JSON file.
    rules = load_rules()

    # Get user input for the Person and Product details.
    credit_score, state = get_person_details()
    product_name = get_product_details()

    # Create an instance of Person with the user input.
    person_input = Person(credit_score, state)

    # Create an instance of Product with the default interest rate set by the rules.
    product_input = Product(product_name)

    # Run the rules engine with the provided details.
    rules_engine = RulesEngine(rules)
    rules_engine.run_rules(person_input, product_input)

    # Output the results.
    print('\nResults:')
    print(f'Product Interest Rate: {product_input.interest_rate}')
    print(f'Product Disqualified: {product_input.disqualified}')