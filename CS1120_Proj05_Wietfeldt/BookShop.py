# Project No.: 5
# Author: Tobyn Wietfeldt
# Description: Book Shop functionality program

# Importing for the reduce function
import functools


# Class for all bookshop methods
class BookShop:
    # Initializing order
    def __init__(self, order):
        self.__orders = order

    # Setter for order
    def set_orders(self, order):
        self.__orders = order

    # Getter for order
    def get_orders(self):
        return self.__orders

    # Iterating through each order
    # Then mapping the order number and price into a list of tuples
    # Finally, adding the bookshop order number to the list of tuples and appending
    # it to a bigger list containing each order
    def two_item_tuples(self):
        two_item_tuples = []
        for order in self.__orders:
            num = order[0]
            products = order[1:]
            entry = list(map(lambda x: (x[0], x[1]*x[2] + 10) if x[1]*x[2] < 100 else (x[0], x[1]*x[2]), products))
            entry.insert(0, num)
            two_item_tuples.append(entry)
        return two_item_tuples

    # Iterating through each order
    # finding the smallest purchase in the order
    # filtering out all purchases that are greater than the smallest
    # appending a tuple with the bookshop order number and the
    # order number of the smallest purchase to a list of smallest orders
    def min_price_filter(self):
        small_orders = []
        for order in self.__orders:
            products = order[1:]
            num = order[0]
            min_price = min([item[1] * item[2] for item in products])
            smallest_order = list(filter(lambda x: x[1] * x[2] <= min_price, products))
            order_num = smallest_order[0][0]
            small_orders.append((num, order_num))
        return small_orders

    # Iterating through each order
    # finding the largest purchase in the order
    # filtering out all purchases that are less than the greatest
    # appending a tuple with the bookshop order number and the
    # order number of the largest purchase to a list of largest orders
    def max_price_filter(self):
        big_orders = []
        for order in self.__orders:
            products = order[1:]
            num = order[0]
            max_price = max([item[1] * item[2] for item in products])
            biggest_order = list(filter(lambda x: x[1] * x[2] >= max_price, products))
            order_num = biggest_order[0][0]
            big_orders.append((num, order_num))
        return big_orders

    # Iterating through each order
    # mapping the price of each product to the product in the order
    # summing the prices
    # appending a tuple containing the bookshop order number and the sum of the prices
    # to a list of tuples
    def orders_and_totals_tuples(self):
        orders_and_totals_tuples = []
        for order in self.__orders:
            products = order[1:]
            num = order[0]
            amount = sum(list(map(lambda x: x[1]*x[2], products)))
            orders_and_totals_tuples.append((num, float(f"{amount: .2f}")))
        return orders_and_totals_tuples

    # Iterating through each order
    # assigning a key to the order number and the value to zero for my dictionary
    # adding the product for each order number to the value in my dictionary
    # Finding the key with the highest value
    # outputting that key (order number) and the value (total product) in a list
    def order_number_and_total_list(self):
        numbers_and_amounts_dict = {}
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_amounts_dict[product[0]] = 0
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_amounts_dict[product[0]] += product[1] * product[2]
        max_product_key = max(numbers_and_amounts_dict, key=lambda x: numbers_and_amounts_dict[x])
        return [max_product_key, numbers_and_amounts_dict[max_product_key]]

    # Iterating through each order
    # assigning a key to the order number and the value to zero for my dictionary
    # adding the quantity for each order number to the value in my dictionary
    # Finding the key with the highest value
    # outputting that key (order number) and the value (total quantity) in a list
    def order_number_and_count_list(self):
        numbers_and_quantity_dict = {}
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_quantity_dict[product[0]] = 0
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_quantity_dict[product[0]] += product[1]
        max_quantity_key = max(numbers_and_quantity_dict, key=lambda x: numbers_and_quantity_dict[x])
        return [max_quantity_key, numbers_and_quantity_dict[max_quantity_key]]

    # Iterating through each order
    # mapping the quantities of the order, then summing them
    # appending the order num and sum to a list of tuples containing
    # the order numbers and quantities
    # sorting the list of tuples from high to low based on the tuples quantities
    def ordered_quantity_list(self):
        quantity_list = []
        for order in self.__orders:
            products = order[1:]
            num = order[0]
            total_quantity = sum(list(map(lambda x: x[1], products)))
            quantity_list.append((num, total_quantity))
        ordered_quantity_list = sorted(quantity_list, key=lambda x: x[1], reverse=True)
        return ordered_quantity_list

    # Iterating through each order
    # mapping each quantity to a list and getting the sum
    # adding the sum to a list of all quantities
    # using reduce to sum all quantities
    def total_quantity(self):
        quantity = []
        for order in self.__orders:
            products = order[1:]
            quantity.append(sum(list(map(lambda x: x[1], products))))
        quantity = functools.reduce(lambda a, b: a + b, quantity)
        return quantity

    # Iterating through each order
    # assigning a key to the order number and the value to zero for my dictionary
    # adding the quantity for each order number to the value in my dictionary
    # Finding the keys with the highest and lowest values
    # outputting the keys (order numbers) in a list
    def most_and_least_ordered(self):
        numbers_and_quantity_dict = {}
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_quantity_dict[product[0]] = 0
        for order in self.__orders:
            products = order[1:]
            for product in products:
                numbers_and_quantity_dict[product[0]] += product[1]
        max_quantity_key = max(numbers_and_quantity_dict, key=lambda x: numbers_and_quantity_dict[x])
        min_quantity_key = min(numbers_and_quantity_dict, key=lambda x: numbers_and_quantity_dict[x])
        return [max_quantity_key, min_quantity_key]

    # mapping the length of each sublist to a list
    def sublist_lengths(self):
        lengths = list(map(lambda x: len(x), self.__orders))
        return lengths
