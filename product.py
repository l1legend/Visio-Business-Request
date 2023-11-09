class Product:
    def __init__(self, name, interest_rate=None):  # The interest_rate defaults to None because no rate has been set yet.
        self.name = name                           # This accounts for the default interest rate being set in the json file, else it would have
        self.interest_rate = interest_rate         # to be hardcoded in the rule_engine file
        self.disqualified = False
