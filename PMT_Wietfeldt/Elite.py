# importing super class
from CreditCard import CreditCard


class Elite(CreditCard):
    # initializing with the super class
    def __init__(self, description, online, gas, other):
        super().__init__(description, online, gas, other, "Elite Card")

    # Calculate and return the cashback amount for this credit card.
    # Overrides the super class
    def get_cashback_amount(self):
        super().get_cashback_amount()
        return (super().get_online() * .1) + (super().get_gas() * .05) + (super().get_other() * .02)
