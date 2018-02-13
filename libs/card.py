CARD_VALUES = {
    '1': [1],
    '2': [2],
    '3': [3],
    '4': [4],
    '5': [5],
    '6': [6],
    '7': [7],
    '8': [8],
    '9': [9],
    'K': [10],
    'Q': [10],
    'J': [10],
    'A': [1, 11]
}

CARD_NAMES = {
    'K': 'King',
    'Q': 'Queen',
    'J': 'Jack',
    'A': 'Ace'
}

class Card:
    def __init__(self, value):
        if not CARD_VALUES.get(value):
            raise ValueError('Unrecognized Card')
        self.card = value

    def get_value(self):
        return CARD_VALUES[self.card]

    def get_name(self):
        if self.card in ['K', 'J', 'Q', 'A']:
            return CARD_NAMES[self.card]

        return str(CARD_VALUES[self.card][0])
