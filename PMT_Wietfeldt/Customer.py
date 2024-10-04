class Customer:
    def __init__(self):
        self.__cards = []
        self.__total = 0

    # Add credit card ‘card’ to list of cards
    def add_credit_card(self, card):
        self.__cards.append(card)

    # Return list of cards
    def get_credit_cards(self):
        return self.__cards

    # Calculate cash back
    def calculate_total_cashback(self):
        self.__total = 0
        for card in self.__cards:
            self.__total += card.get_cashback_amount()
        return self.__total
