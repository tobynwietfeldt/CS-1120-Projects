# Project No.: 2
# Authors: Mohammed Alfaraj and Tobyn Wietfeldt
# Description: Student profile application

from graduation_auditor import GraduationAuditor
from undergrad_student import UndergradStudent
from grad_student import GradStudent


def main():
    auditor = GraduationAuditor()
    print("\nUndergraduate Students:")
    print("=======================\n")
    students = dict()
    students["undergrads"] = list()
    # Student #1
    students["undergrads"].append(UndergradStudent("Mark Lutz", 111))
    print(students["undergrads"][0].get_name())
    print("==============")
    students["undergrads"][0].do_community_service(20)
    students["undergrads"][0].do_community_service(20)
    students["undergrads"][0].take_course("Intro to Python", 26)
    students["undergrads"][0].take_course("Intro to Computing", 8)
    students["undergrads"][0].print_data()
    print()
    # Student #2
    students["undergrads"].append(UndergradStudent("Zed Shaw", 222))
    print(students["undergrads"][1].get_name())
    print("==============")
    students["undergrads"][1].do_community_service(15)
    students["undergrads"][1].take_course("Intro to Python", 15)
    students["undergrads"][1].take_course("Intro to Computing", 8)
    students["undergrads"][1].print_data()
    print("\nGraduate Students:")
    print("==================\n")
    students["grads"] = list()
    # Student #3
    students["grads"].append(GradStudent("Naomi Ceder", 111))
    print(students["grads"][0].get_name())
    print("==============")
    students["grads"][0].publish_paper("Formal Semantics of Programming Languages")
    students["grads"][0].publish_paper("Cyber Security in Digital Sector")
    students["grads"][0].take_course("Intro to Python", 26)
    students["grads"][0].take_course("Intro to Computing", 8)
    students["grads"][0].print_data()
    print()
    # Student #4
    students["grads"].append(GradStudent("David Beazley", 222))
    print(students["grads"][1].get_name())
    print("==============")
    students["grads"][1].publish_paper("Formal Semantics of Programming Languages")
    students["grads"][1].take_course("Intro to Python", 15)
    students["grads"][1].take_course("Intro to Computing", 8)
    students["grads"][1].print_data()
    print("\nAudit results:")
    print("==============\n")
    auditor.audit(students["undergrads"])
    auditor.audit(students["grads"])


main()
