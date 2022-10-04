# CMP - Course Management Program
class CMP:  # Main class which consists of all functionalities, students, courses
    __students = []
    courses = []

    def __init__(self):
        print("Course Management Program is ready")

    def getStudents(self, is_admin):
        if is_admin:
            return self.__students

    def __add(self, action_to, action_object, is_admin):
        if action_to == "student":
            action_array = self.__students
        else:
            action_array = self.courses

        print(f"Add {action_to.capitalize()} is ready")

        if is_admin:
            if not action_array:
                action_array.append(action_object)
                print(f"{action_to.capitalize()} {action_object[f'{action_to}_name']} is added")
            else:
                if action_object in action_array:
                    print(f"{action_to.capitalize()} {action_object[f'{action_to}_name']} is already added!")
                else:
                    action_array.append(action_object)
                    print(f"{action_to.capitalize()} {action_object[f'{action_to}_name']} is added!")
        else:
            print("You are not authorized!")
        print(f"Students {self.__students}")

    def __update(self, action_to, action_object, is_admin):
        if action_to == "student":
            action_array = self.__students
            identifier = 'student_id'
        else:
            action_array = self.courses
            identifier = 'course_name'

        print(f"Update {action_to.capitalize()} is ready")

        if is_admin:
            if not action_array:
                print(f"No {action_to.capitalize()}s in the system. Add {action_to} first!")
            else:
                # Checking whether the key(student or course id) is present in action_array or not using list comprehension
                object_exist = False
                for object_dict in action_array:
                    if action_object[identifier] == object_dict[identifier]:
                        object_exist = True
                        # I have used update function to remove any complexity and for simplicity
                        object_dict.update(action_object)
                        print(f"{action_to.capitalize()} {action_object[f'{action_to}_name']} is updated!")
                if not object_exist:
                    print(f"Not found: {action_object[f'{action_to}_name']} in {action_to.capitalize()}s!")

        else:
            print("You are not authorized!")
        print(f"Students {self.__students}")

    def __delete(self, action_to, action_object, is_admin):
        if action_to == "student":
            action_list = self.__students
            identifier = 'student_id'
        else:
            action_list = self.courses
            identifier = 'course_name'

        print(f"Delete {action_to.capitalize()} is ready")

        if is_admin:
            if not action_list:
                print(f"No {action_to.capitalize()}s in the system. Add {action_to} first!")
            else:
                # Checking whether the key(student or course id) is present in action_list or not using list comprehension
                object_exist = False
                for object_dict in action_list:
                    if action_object[identifier] == object_dict[identifier]:
                        object_exist = True
                        delete_index = action_list.index(object_dict)
                        # I have used update function to remove any complexity and for simplicity
                        action_list.pop(delete_index)
                        print(f"{action_to.capitalize()} {action_object[f'{action_to}_name']} is deleted!")
                if not object_exist:
                    print(f"Not found: {action_object[f'{action_to}_name']} in {action_to.capitalize()}s!")

        else:
            print("You are not authorized!")
        print(f"Students {self.__students}")

    def __enroll(self, action_object):
        # three parameters are important for enrolling into a course: student_name, student_id, course_name
        print(f"Enroll Course is ready")
        if self.__students:
            student_exist = False
            course_exist = False
            # The below lines can be alot simpler with the use of list comprehension

            for student_dict in self.__students:
                if action_object['student']['student_id'] == student_dict['student_id']:
                    student_exist = True
                    for course_dict in self.courses:
                        if action_object['course']['course_name'] == course_dict['course_name']:
                            course_exist = True
                            course_enroll = course_dict['course_name']
                            if 'courses_enrolled' in student_dict:
                                student_dict['courses_enrolled'].append(course_enroll)
                            else:
                                student_dict['courses_enrolled'] = [course_enroll]
                            print(f"Enrollment success for {student_dict['student_name']} in {course_enroll}")
            if not student_exist:
                print(f"Student record not found. Contact admin to add you!")
            if not course_exist:
                print(f"Course is not found. Contact admin to check the list of courses offered!")
            print(self.__students)
        else:
            print("No students registered on the program! Contact admin")

    def __unenroll(self, action_object):
        print("Enroll Course is ready")
        if self.__students:
            student_exist = False
            course_exist = False
            # The below lines can be alot simpler with the use of list comprehension
            for student_dict in self.__students:
                if action_object['student']['student_id'] == student_dict['student_id']:
                    student_exist = True
                    for course_dict in self.courses:
                        if action_object['course']['course_name'] == course_dict['course_name']:
                            course_exist = True
                            course_enroll = course_dict['course_name']
                            if 'courses_enrolled' in student_dict:
                                unroll_index = self.__students.index(student_dict)
                                student_dict['courses_enrolled'].pop(unroll_index)
                                print(
                                    f"Unenrollment success for {student_dict['student_name']} in {course_enroll}")
                            else:
                                print("No courses added to unroll")
            if not student_exist:
                print(f"Student record not found. Contact admin to add you!")
            if not course_exist:
                print(f"Course is not found. Contact admin to check the list of courses offered!")
            print(self.__students)
        else:
            print("No students registered on the program! Contact admin")

    def __submit_grade(self, action_to, action_object, is_admin, grade):
        if is_admin:
            if self.__students:
                student_exist = False
                # The below lines can be alot simpler with the use of list comprehension
                for student_dict in self.__students:
                    if action_object['student_id'] == student_dict['student_id']:
                        student_exist = True
                        student_dict['grade'] = grade
                        if 'grade' in student_dict:
                            print(f"Upgraded the grade of {student_dict['student_name']} with {grade}")
                        else:
                            print(f"Graded {student_dict['student_name']} with {grade}")
                if not student_exist:
                    print(f"Student record not found. Contact admin to add you!")
                print(self.__students)
            else:
                print("No students registered on the program! Contact admin")
        else:
            print("You are not authorized!")

    def admin_functionality(self, f_action_to, f_object, f_action, f_admin, grade=""):
        f_action_list = ['add', 'update', 'delete', 'submit_grade']
        assert f_action_to != "student" or f_action_to != "course", 'Enter student or course details!'
        assert f_action in f_action_list, 'Input only valid action to take'

        if f_action == "add":
            self.__add(f_action_to, f_object, f_admin)
        elif f_action == "update":
            self.__update(f_action_to, f_object, f_admin)
        elif f_action == "delete":
            self.__delete(f_action_to, f_object, f_admin)
        elif f_action == "submit_grade":
            self.__submit_grade(f_action_to, f_object, f_admin, grade)

    def student_functionality(self, f_object, f_action):
        f_action_list = ['enroll', 'unenroll']
        assert f_action in f_action_list, 'Input only valid action to take'

        if f_action == "enroll":
            self.__enroll(f_object)
        else:
            self.__unenroll(f_object)


class Admin(CMP):
    def __init__(self):
        super().__init__()
        self.__program_admin = True

    def students_list(self):
        print(self.getStudents(self.__program_admin))

    def student_function(self, student_name: str, student_id: int = 0, student_action: str = "", grade=""):
        assert student_action != "", 'Tell us what you want to do in 3rd parameter for student!'
        assert student_name != "", 'Your name is required!'
        assert student_id != 0, 'Your student is required!'
        assert 3 < len(str(student_id)) < 10, 'Student Id should be an integer of length between 4 to 9'
        student_object = {'student_name': student_name, 'student_id': student_id}
        self.admin_functionality("student", student_object, student_action, self.__program_admin, grade)

    def course_function(self, course_name: str, course_action: str = ""):
        assert course_action != "", 'Tell us what you want to do in 2nd parameter for course!'
        assert course_name != "", 'Course name is required!'
        course_object = {'course_name': course_name}
        self.admin_functionality("course", course_object, course_action, self.__program_admin)


class Student(CMP):
    def __init__(self, student_name: str, student_id: int):
        super().__init__()
        self.student_name = student_name
        self.student_id = student_id

    def enroll_course(self, course_name=""):
        assert self.student_name != "", 'Your name is required!'
        assert self.student_id != 0, 'Your student is required!'
        assert course_name != "", 'Course name is required!'
        enroll_details = {
            'student': {'student_name': self.student_name, 'student_id': self.student_id},
            'course': {'course_name': course_name}
        }
        self.student_functionality(enroll_details, "enroll")

    def unenroll_course(self, course_name=""):
        assert self.student_name != "", 'Your name is required!'
        assert self.student_id != 0, 'Your student is required!'
        assert course_name != "", 'Course name is required!'
        enroll_details = {'student_name': self.student_name, 'student_id': self.student_id, 'course_name': course_name}
        self.student_functionality(enroll_details, "unenroll")
        print(f"The student name: {self.student_name} and student id: {self.student_id} ")


#   common interface


admin = Admin()
admin.student_function("JaiK", 4534, "add")  # pass student name, student id, action to do
admin.student_function("Jai", 4534, "update")
admin.student_function("Jai", 4354, "delete")
admin.student_function("Jai", 4534, "add")

admin.course_function("System Optimization", "add") # pass course name, action to do
admin.course_function("Full Stack Cloud Development", "add")
admin.course_function("delete test course", "add")
admin.course_function("delete test course", "delete")

student = Student('Jai', 4534) # pass student name, student id,


student.enroll_course("System Optimization") # pass course name
student.unroll_course('System Optimization')

admin.student_function("Jai", 4534, 'submit_grade', "A")
admin.student_function("Jai", 4534, 'submit_grade', "B")

admin.students_list()
