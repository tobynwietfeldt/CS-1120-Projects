# importing super class
from CreditCard import CreditCard


class VIP(CreditCard):
    # initializing with the super class
    def __init__(self, description, online, other):
        super().__init__(description, online, 0, other, "VIP Card")

    # Calculate and return the cashback amount for this credit card.
    # Overrides the super class
    def get_cashback_amount(self):
        super().get_cashback_amount()
        return (super().get_online() * .05) + (super().get_gas() * .05) + (super().get_other() * .02)
