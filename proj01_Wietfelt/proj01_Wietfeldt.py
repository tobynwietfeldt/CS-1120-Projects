# Project No.: 1
# Author: Tobyn Wietfeldt
# Description: Spanish Quiz

import random


def get_dict(filename):
    words_dict = {}
    with open(filename, "r") as file:
        for line in file:
            english_word, spanish = line.strip().split(":")
            spanish_words = spanish.split(",")
            for word in range(0, len(spanish_words)):
                spanish_words[word] = spanish_words[word].strip()
            words_dict[english_word] = spanish_words
    return words_dict


def check_quizWords(engWords, spaWords):
    response_check = []
    repetition_check = []
    for word in range(0, len(spaWords)):
        if spaWords[word] in get_dict("words.txt")[engWords]:
            response_check.append("T")
        else:
            response_check.append("F")
        if spaWords[word] in repetition_check:
            return False
        repetition_check.append(spaWords[word])
    if "F" in response_check:
        return False
    else:
        return True


def make_quizFile(userName, date, quizDict, score):
    with open("quiz.txt", "w") as outfile:
        outfile.write(f"Name: {userName}\n")
        outfile.write(f"Date: {date}\n")
        for key in quizDict:
            spanish = ", ".join(quizDict[key])
            outfile.write(f"{key}:{spanish}\n")
        outfile.write(f"Score: {score}")


def main():
    print("Welcome to the vocabulary quiz program.\n")
    file_name = input("Please enter a file name: ")
    try:
        words_dict = get_dict(file_name)
        num_words = len(words_dict)
        print(num_words, "entries found.")
        user_name = input("Please enter your full name: ")
        date = input("Please enter the date: ")
        print("\n")
        q_number = 0
        while q_number not in range(1, num_words + 1):
            try:
                q_number = int(input("How many words would you like to be quizzed on? "))
                if q_number not in range(1, num_words + 1):
                    print("Please enter a valid number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")
                continue
        print("\n")
        quiz_keys = random.sample(list(words_dict), q_number)
        correct = 0
        incorrect = 0
        quiz_dict = {}
        for key in quiz_keys:
            quiz_dict[key] = words_dict[key]
            responses = []
            print(f"English word: {key}")
            responses.append(input(f"Enter {len(words_dict[key])} "
                                   f"equivalent Spanish word(s). Word [1]: ").lower().strip())
            if len(words_dict[key]) > 1:
                for spanish_words in range(1, len(words_dict[key])):
                    responses.append(input(f"Word [{spanish_words + 1}]: ").lower().strip())
            if check_quizWords(key, responses) is True:
                print("Correct!\n\n---\n\n")
                correct += 1
            else:
                print("Incorrect.\n\n---\n\n")
                incorrect += 1
        score = f"{correct} out of {correct + incorrect} correct"
        print(score, ".")
        outfile = input("Enter an output file (or press enter to quit): ")
        if outfile == "quiz.txt":
            make_quizFile(user_name, date, quiz_dict, score)
        print("\n\nBye!")
    except FileNotFoundError:
        print(f"The file name {file_name} does not exist\n")
        print("Bye!")


main()
