class Product:
    def __init__(self, name, interest_rate=None):
        self.name = name
        self.interest_rate = interest_rate if interest_rate is not None else 0
        self.disqualified = False
