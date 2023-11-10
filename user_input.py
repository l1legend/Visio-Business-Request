
from rules_loader import load_rules

def get_valid_credit_score() -> int:
    while True:
        try:
            credit_score = int(input('Enter the credit score: '))
            if credit_score < 0:
                print("Credit score cannot be negative. Please enter a valid positive integer.")
            else:
                return credit_score
        except ValueError:
            print("That's not a valid number. Please enter an integer value for the credit score.")

def get_valid_state() -> str:
    valid_states = {
        'alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut', 'delaware', 'florida',
        'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana', 'maine',
        'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi', 'missouri', 'montana', 'nebraska',
        'nevada', 'new hampshire', 'new jersey', 'new mexico', 'new york', 'north carolina', 'north dakota', 'ohio',
        'oklahoma', 'oregon', 'pennsylvania', 'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas',
        'utah', 'vermont', 'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming'
    }

    while True:
        state_input = input("Please enter a valid U.S. state name: ").lower()
        if state_input in valid_states:
            return state_input.title()
        else:
            print("Invalid input. Please enter a valid U.S. state name.")

def get_product_details() -> str:
    rules = load_rules()
    valid_product_names = set()
    for rule in rules: # parse through rules.json
        condition = rule.get('condition', '')
        if "product.name" in condition:
            start = condition.find("'") + 1  # Find the opening quote
            end = condition.find("'", start)  # Find the closing quote
            product_name = condition[start:end]  # Extract the product name
            valid_product_names.add(product_name)
    while True:
        product_name = input('Enter the name of the product: ')
        if product_name in valid_product_names:
            return product_name
        else:
            print("Product does not exist, please enter a valid product name.")
