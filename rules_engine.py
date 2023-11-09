
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

# Example usage:
if __name__ == '__main__':
    rules = load_rules_from_json('rules.json')
    rules_engine = RulesEngine(rules)
    
    person_example = Person(720, 'Florida')
    product_example = Product('7-1 ARM', 5.0)
    
    rules_engine.run_rules(person_example, product_example)
    
    print({
        'product_interest_rate': product_example.interest_rate,
        'product_disqualified': product_example.disqualified
    })
