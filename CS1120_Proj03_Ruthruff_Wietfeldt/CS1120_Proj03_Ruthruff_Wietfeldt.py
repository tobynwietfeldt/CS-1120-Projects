# Project No.: 3
# Authors: Nolan Ruthruff and Tobyn Wietfeldt
# Description: Boggle Board Game

# Importing
import string
import random


class BoggleBoard:
    # Initializing board
    def __init__(self):
        self.board = ""

    # Setter for board
    def set_board(self, board):
        self.board = board

    # Getter for board
    def get_board(self):
        return self.board

    # Generating board using user-input seed.
    # Board is a 4x4, two-dimensional array with a random letter at each element.
    def generate_board(self, seed):
        random.seed(seed)
        board = [[random.choice(string.ascii_uppercase) for _ in range(4)] for _ in range(4)]
        self.board = board

    # Displays the board and accounts for if carrots are present.
    def display_board(self):
        print("+---+ +---+ +---+ +---+")
        for row in self.board:
            for letter in row:
                if "<" in letter:
                    print(f"|{letter}| ", end="")
                else:
                    print(f"| {letter} | ", end="")
            print("\n+---+ +---+ +---+ +---+")

    # Uses a loop to call the search_word function for each letter on the board.
    def is_valid_word(self, word):
        for row in range(4):
            for letter in range(4):
                if self.search_word(row, letter, word):
                    return True
        return False

    # This function uses recursion to check if the word is within the rules of the game
    # The base case is an empty string, returning True
    def search_word(self, row, letter, word):
        if not word:
            return True
        if row < 0 or row >= 4 or letter < 0 or letter >= 4:
            return False
        if self.board[row][letter] != word[0]:
            return False
        letter_holder = self.board[row][letter]
        self.board[row][letter] = ''
        found = self.search_word(row + 1, letter, word[1:]) or \
                self.search_word(row - 1, letter, word[1:]) or \
                self.search_word(row, letter + 1, word[1:]) or \
                self.search_word(row, letter - 1, word[1:])
        if not found:
            self.board[row][letter] = letter_holder
        if found:
            self.board[row][letter] = f"<{letter_holder}>"
        return found

    # Using recursion to check if word is a palindrome
    # Base case is a one-letter word.
    def is_palindrome(self, word):
        if len(word) <= 1:
            return True
        if word[0] != word[-1]:
            return False
        return self.is_palindrome(word[1:-1])


def main():
    # Getting user-input seed, creating an instance, generating board, displaying board
    seed = int(input("Enter seed: "))
    boggle_board = BoggleBoard()
    boggle_board.generate_board(seed)
    boggle_board.display_board()

    # Getting user-input word, displaying output based on input and class methods
    word = input("Enter word (in UPPERcase): ")
    if boggle_board.is_valid_word(word) and word != "":
        print("Nice Job!")
        if boggle_board.is_palindrome(word) and word != "":
            print(f"The word {word} is a palindrome.")
            boggle_board.display_board()
        else:
            print(f"The word {word} is not a palindrome.")
            boggle_board.display_board()
    else:
        print("I don't see that word.")
        if boggle_board.is_palindrome(word) and word != "":
            print(f"The word {word} is a palindrome.")
        else:
            print(f"The word {word} is not a palindrome.")
        print("Are we looking at the same board?")


main()
