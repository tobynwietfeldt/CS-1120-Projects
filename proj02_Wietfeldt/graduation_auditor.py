from undergrad_student import UndergradStudent
from grad_student import GradStudent


class GraduationAuditor:
    # This function iterates through the list of students input.
    # It checks graduation requirements for each student using
    # methods from the Students class and the students respective subclass.
    # It then outputs if students have passed the requirements
    def audit(self, students):
        for student in students:
            if isinstance(student, UndergradStudent):
                if (student.get_total_credits() >= 30 and
                        student.get_community_service_hours() >= 20):
                    print(f"{student.get_name()} can graduate")
                else:
                    print(f"{student.get_name()} cannot graduate")
            elif isinstance(student, GradStudent):
                if (student.get_total_credits() >= 30 and
                        len(student.get_publications()) >= 2):
                    print(f"{student.get_name()} can graduate")
                else:
                    print(f"{student.get_name()} cannot graduate")
