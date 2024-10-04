class CreditCard:
    def __init__(self, description, online, gas, other, types):
        self.__description = description
        self.__online = online
        self.__gas = gas
        self.__other = other
        self.__types = types

    # Getters
    def get_description(self):
        return self.__description

    def get_online(self):
        return self.__online

    def get_gas(self):
        return self.__gas

    def get_other(self):
        return self.__other

    def get_type(self):
        return self.__types

    # Setters
    def set_description(self, description):
        self.__description = description

    def set_online(self, online):
        self.__online = online

    def set_gas(self, gas):
        self.__gas = gas

    def set_other(self, other):
        self.__other = other

    def set_type(self, types):
        self.__types = types

    # Calculate and return the cashback amount for this credit card.
    # Method gets overridden by subclasses
    def get_cashback_amount(self):
        pass
