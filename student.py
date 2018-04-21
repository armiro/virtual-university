class Student:
    """Common base class for all students"""
    numReg = []

    # basic init method for Student class
    def __init__(self, number, name, family, courses=None):
        if courses is None:
            courses = []
        self.number = number
        self.numReg.append(self)
        self.name = name
        self.family = family
        self.courses = courses

    # when called, it will display student's name anf family
    def displayStudent(self):
        print('You are logged in as ' + self.name + ' ' + self.family)

    # when called, it'll display the courses a student has
    def displayStudentCourses(self, numStudent):
        if self.number == numStudent:
            if self.courses:
                print(self.courses)
            else:
                print('You have no courses, yet!')

    # when called, it will add the "wantedCourse" to the "numStudent" courses
    def studentCourseAdding(self, wantedCourse, numStudent):
        if self.number == numStudent:
            self.courses.append(wantedCourse)
            print('You Added ' + wantedCourse + ' to your schedule, successfully!')
