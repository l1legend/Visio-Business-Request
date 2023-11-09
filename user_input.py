
from rules_loader import load_rules

def get_person_details():
    while True:
        try:
            credit_score = int(input('Enter the credit score: '))
            if credit_score < 0:
                print("Credit score cannot be negative. Please enter a valid positive integer.")
                continue  # Continue will restart the loop, asking for input again
            break  # If input is valid, break out of the loop
        except ValueError:
            print("That's not a valid number. Please enter an integer value for the credit score.")
    state = input('Enter the state: ')
    return credit_score, state

def get_product_details():
    rules = load_rules()
    valid_product_names = set()
    for rule in rules:
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
