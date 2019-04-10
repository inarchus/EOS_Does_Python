class Money:

    currency_types = {'USD': 1, 'GBP': 0.77, 'RUB': 64.82, 'BIT': 0.00019, 'EUR': 0.89}

    def __init__(self, amount=0, currency_type='USD'):
        self.currency_type = currency_type
        self.amount = amount

    def convertTo(self, new_currency_type):
        if new_currency_type in Money.currency_types and new_currency_type != self.currency_type:
            self.amount /= Money.currency_types[self.currency_type]
            self.amount *= Money.currency_types[new_currency_type]
            self.currency_type = new_currency_type
        return self

    def __add__(self, other_money):
        return Money(self.amount + other_money.convertTo(self.currency_type).amount, self.currency_type)

    def __str__(self):
        return str(round(self.amount, 2)) + ' ' + self.currency_type


x = Money(1, 'USD')
y = Money(1, 'GBP')
print((x + y).amount)

x = Money(1, 'USD')
y = Money(1, 'GBP')
z = Money(2.5, 'RUB')
w = Money(3.7, 'BIT')
print(x, y, z, w)

