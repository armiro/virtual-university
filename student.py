pCourses = [None]
qCourses = [None]
rCourses = [None]
sCourses = [None]
tCourses = [None]
uCourses = [None]


class Student:
    """Common base class for all students"""
    numReg = []

    def __init__(self, number, name, family, courses=[]):
        self.number = number
        self.numReg.append(self)
        self.name = name
        self.family = family
        self.courses = courses

    def displayStudent(self):
        print('You are logged in as ' + self.name + ' ' + self.family)

    def displayStudentCourses(self):
        if self.courses == [None]:
            print('You have no courses, yet!')
        else:
            if self.courses[0] == None:
                del self.courses[0]
                print(self.courses)
            else:
                print(self.courses)

    def studentCourseAdding(self, wantedCourse):
        if self.courses[0] == None:
            del self.courses[0]
            self.courses.append(wantedCourse)
        else:
            self.courses.append(wantedCourse)
        print('You Added ' + wantedCourse + ' to your schedule!')


student1 = Student(9701, 'amir', 'ahmadi', pCourses)
student2 = Student(9702, 'sina', 'mohammadi', qCourses)
student3 = Student(9703, 'hossein', 'faghihi', rCourses)
student4 = Student(9704, 'javad', 'hatami', sCourses)
student5 = Student(9705, 'mohammad', 'karimi', tCourses)
student6 = Student(9706, 'amin', 'mousavi', uCourses)
