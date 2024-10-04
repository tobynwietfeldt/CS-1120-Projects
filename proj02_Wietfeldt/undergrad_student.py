from student import Student


class UndergradStudent(Student):
    # Creating a subclass of Student for undergrads
    # initializing community service hours and attributes from superclass
    def __init__(self, name, student_id):
        super().__init__(name, student_id)
        self.__community_service_hours = 0

    # Setter
    def set_community_service_hours(self, community_service_hours):
        self.__community_service_hours = community_service_hours

    # Getter
    def get_community_service_hours(self):
        return self.__community_service_hours

    # Method for adding community service hours to total
    def do_community_service(self, hours):
        self.__community_service_hours += hours

    # Printing output (uses the output from the superclass, but overrides it by adding community service)
    def print_data(self):
        super().print_data()
        print("Hours of community service:", self.__community_service_hours)
