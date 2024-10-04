from student import Student


class GradStudent(Student):
    # Creating a subclass of Student for grads
    # initializing publications and attributes from superclass
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.__publications = []

    # Setter
    def set_publications(self, publications):
        self.__publications = publications

    # Getter
    def get_publications(self):
        return self.__publications

    # Method for adding a new paper to the list
    def publish_paper(self, paper_title):
        self.__publications.append(paper_title)

    # Printing output (uses the output from the superclass, but overrides it by adding publications)
    def print_data(self):
        for publication in range(0, len(self.__publications)):
            print(f"Publication #{publication + 1}:", self.__publications[publication])
        super().print_data()
        print("Number of Publications:", len(self.__publications))
