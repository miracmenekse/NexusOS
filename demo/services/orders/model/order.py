PRICES = {"book": 12.5, "pen": 1.2, "lamp": 30.0}


class Order:
    def __init__(self, item, qty):
        self.item, self.qty = item, qty

    def total(self):
        return PRICES.get(self.item, 10.0) * self.qty

    def to_dict(self):
        return {"item": self.item, "qty": self.qty, "total": self.total()}
