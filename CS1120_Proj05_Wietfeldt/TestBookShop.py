# Importing for Bookshop methods
# Importing for testing
import BookShop
import unittest


# Subclass of unittest.TestCase for testing my bookshop methods
class TestBookShop(unittest.TestCase):
    # Testing first bookshop method using actual and expected
    def test1(self):
        expected = [[1, ("5464", 49.96), ("8274", 233.82), ("9744", 404.55)],
                    [2, ("5464", 99.91), ("9744", 404.55)],
                    [3, ("5464", 99.91), ("88112", 274.89)],
                    [4, ("8732", 93.93), ("7733", 208.89), ("88112", 199.75)]]
        actual = BookShop.BookShop.two_item_tuples(order)
        self.assertEqual(expected, actual)
        print(f"Test 1 \nActual: {actual} \nExpected: {expected}\n")

    # Testing second bookshop method using actual and expected
    def test2(self):
        expected = [(1, "5464"), (2, "5464"), (3, "5464"), (4, "8732")]
        actual = BookShop.BookShop.min_price_filter(order)
        self.assertEqual(expected, actual)
        print(f"Test 2 \nActual: {actual} \nExpected: {expected}\n")

    # Testing third bookshop method using actual and not expected
    def test3(self):
        wrong_expected = [(1, "9744"), (2, "5464"), (3, "88112"), (4, "7733")]
        correct_expected = [(1, "9744"), (2, "9744"), (3, "88112"), (4, "7733")]
        actual = BookShop.BookShop.max_price_filter(order)
        self.assertNotEqual(wrong_expected, actual)
        print(f"Test 3 \nActual: {actual} \nWrong Expected: {wrong_expected}\n"
              f"Correct Expected: {correct_expected}\n")

    # Testing fourth bookshop method using actual and expected
    def test4(self):
        expected = [(1, 678.33), (2, 494.46), (3, 364.8), (4, 492.57)]
        actual = BookShop.BookShop.orders_and_totals_tuples(order)
        self.assertEqual(expected, actual)
        print(f"Test 4 \nActual: {actual} \nExpected: {expected}\n")

    # Testing fifth bookshop method using actual and expected
    def test5(self):
        expected = ["9744", 809.1]
        actual = BookShop.BookShop.order_number_and_total_list(order)
        self.assertIn(expected[0], actual)
        print(f"Test 5 \nActual: {actual} \nExpected: {expected[0]}\n")

    # Testing sixth bookshop method using actual and expected
    def test6(self):
        expected = ["5464", 22]
        actual = BookShop.BookShop.order_number_and_count_list(order)
        self.assertEqual(expected, actual)
        print(f"Test 6 \nActual: {actual} \nExpected: {expected}\n")

    # Testing seventh bookshop method using actual and expected
    def test7(self):
        expected = [(1, 31), (4, 23), (3, 20), (2, 18)]
        actual = BookShop.BookShop.ordered_quantity_list(order)
        self.assertEqual(expected, actual)
        print(f"Test 7 \nActual: {actual} \nExpected: {expected}\n")

    # Testing eighth bookshop method using actual and expected
    def test8(self):
        expected = 92
        actual = BookShop.BookShop.total_quantity(order)
        self.assertEqual(expected, actual)
        print(f"Test 8 \nActual: {actual} \nExpected: {expected}\n")

    # Testing ninth bookshop method using actual and expected
    def test9(self):
        expected = ["5464", "8732"]
        actual = BookShop.BookShop.most_and_least_ordered(order)
        self.assertEqual(expected, actual)
        print(f"Test 9 \nActual: {actual} \nExpected: {expected}\n")

    # Testing tenth bookshop method using actual and expected
    def test10(self):
        expected = [4, 3, 3, 4]
        actual = BookShop.BookShop.sublist_lengths(order)
        self.assertEqual(expected, actual)
        print(f"Test 10 \nActual: {actual} \nExpected: {expected}\n")


# declaring the sample list provided
orders = [[1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
          [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
          [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
          [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]]
# creating an object using the sample list, for performing methods
order = BookShop.BookShop(orders)
