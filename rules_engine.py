from person import Person
from product import Product
from rules_loader import load_rules
from user_input import get_valid_credit_score, get_valid_state, get_product_details

class RulesEngine:
    def __init__(self, rules): # Initialize the RulesEngine with a set of rules
        self.rules = rules
 
    def run_rules(self, person, product):
        for rule in self.rules:  # Iterate over each rule and evaluate its condition
            if eval(rule['condition']): # Use eval to interpret the condition string
                action = rule['action']
                if action == 'set_default_interest_rate': # Set the default interest rate from the rule
                    product.interest_rate = rule['parameters']['amount']
                elif action == 'disqualify':  
                    product.disqualified = True
                elif action == 'adjust_interest_rate':
                    amount = rule['parameters']['amount'] # Adjust the interest rate based on the rule
                    product.interest_rate += amount

if __name__ == '__main__':
    # Load the rules from the JSON file.
    rules = load_rules()

    # Get user input for the Person and Product details.
    credit_score = get_valid_credit_score()
    state = get_valid_state()
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