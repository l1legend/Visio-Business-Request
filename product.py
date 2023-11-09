class Product:
    def __init__(self, name, interest_rate=None):
        self.name = name
        self.interest_rate = interest_rate
        self.disqualified = False
