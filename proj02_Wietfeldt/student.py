class Student:
    # Initializing students name, id number, courses, and total credits
    def __init__(self, name, student_id):
        self.__name = name
        self.__student_id = student_id
        self.__courses = {}
        self.__total_credits = 0

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_total_credits(self, num):
        self.__total_credits = num

    # Getters
    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_total_credits(self):
        return self.__total_credits

    def get_course(self):
        return self.__courses

    # Method for adding a course and its respective credits
    def take_course(self, course_name, credits):
        self.__courses[course_name] = credits
        self.__total_credits += credits

    # Method for printing output (is overridden by subclasses using polymorphism)
    def print_data(self):
        for course, credits in self.__courses.items():
            print(f"Course taken: {course} ({credits} credits)")
        print("\nCredits completed", self.__total_credits)
