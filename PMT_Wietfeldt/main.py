# PMT number 1
# By Tobyn Wietfeldt
# Credit Card program

# Importing classes
from Customer import Customer
from Elite import Elite
from Classic import Classic
from VIP import VIP


# Main function as provided
def main():
    cust = Customer()
    card1 = Elite("Convocation Luncheon", 100, 25, 150)  # (description, online_exp, gas_exp, other_exp)
    card2 = Classic("Faculty Supplies", 80, 40, 50)  # (description, online_exp, gas_exp, other_exp)
    card3 = VIP("Miscellaneous", 50, 100)  # (description, online_exp, other_exp)

    cust.add_credit_card(card1)
    cust.add_credit_card(card2)
    cust.add_credit_card(card3)

    cards = cust.get_credit_cards()

    print("List of Credit Card Expenses")
    print("============================\n")

    print(f'{"Card":<15}{"Description":<25}{"Cash-back"}')
    print(f'{"----":<15}{"-----------":<25}{"--------"}')

    for i in range(len(cards)):
        print(
            f'{cards[i].get_type():<15}{cards[i].get_description():<25}{"$"}'
            f'{cards[i].get_cashback_amount():>6,.2f}')

    print()
    print(
        f'{"Total cash-back: $"}{cust.calculate_total_cashback():>6,.2f}')

    card4 = Elite("Convocation Awards", 200, 0, 150)  # (description, online_exp, gas_exp, other_exp)
    card5 = Classic("Staff Appreciation", 250, 50, 150)  # (description, online_exp, gas_exp, other_exp)

    cust.add_credit_card(card4)
    cust.add_credit_card(card5)

    print()
    for i in range(len(cards)):
        print(
            f'{cards[i].get_type():<15}{cards[i].get_description():<25}{"$"}'
            f'{cards[i].get_cashback_amount():>6,.2f}')

    print()
    print(
        f'{"Total cash-back: $"}{cust.calculate_total_cashback():>6,.2f}')


main()
