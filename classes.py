
class Course:
    """common base class for all courses"""
    numReg = []

    def __init__(self, number, name, profOfCourse=None, studentInCourse=None):
        if studentInCourse is None:
            studentInCourse = []
        self.number = number
        self.name = name
        self.profOfCourse = profOfCourse
        self.studentInCourse = studentInCourse
        self.numReg.append(self)

    @staticmethod
    def displayCourses():
        for k in Course.numReg:
            print('%d) %s' % (k.number, k.name))

    def displayCourseDetails(self, courseNumber):
        if self.number == courseNumber:
            print('Name of course is: ' + self.name)
            if self.profOfCourse:
                print('Instructor is: Dr. ' + self.profOfCourse)
            else:
                print('No professor has chosen this course to teach!')

            if len(self.studentInCourse) > 0:
                print('Attending student(s) are: ' + str([self.studentInCourse[q] for q in range(0, len(self.studentInCourse))]))
            else:
                print('No students attend here!')

    def newStudentGotACourse(self, numStudent, selectedCourseNumber):
        wantedCourse = courseList[selectedCourseNumber-1]
        if wantedCourse == self.name:
            for i in Student.numReg:
                if numStudent == i.number:
                    nameAndFamily = i.name + ' ' + i.family
                    self.studentInCourse.append(nameAndFamily)

class Professor:
    """common base class for all professors"""
    numReg = []

    def __init__(self, number, family, profCourses=None):
        if profCourses is None:
            profCourses = []
        self.number = number
        self.numReg.append(self)
        self.family = family
        self.profCourses = profCourses

    def displayProfessor(self, numProfessor):
        # for j in Professor.numReg:
            if self.number == numProfessor:
                print('Welcome Dear Dr.' + self.family)
                print('You are the instructor of %d course(s) ' % len(self.profCourses))

    @staticmethod
    def professorCourseGiving(newCourseOption, numProfessor):
        for k in Course.numReg:
            if k.number == newCourseOption:
                courseProf = k.profOfCourse
        if courseProf:
            print('Sorry Sir! Another professor has instructed this course, before!')
        else:
            for k in Course.numReg:
                if k.number == newCourseOption:
                    for j in Professor.numReg:
                        if j.number == numProfessor:
                            j.profCourses.append(k.name)
                            k.profOfCourse = j.family
            print('You are now the instructor of %s!' % courseList[newCourseOption-1])

class Student:
    """Common base class for all students"""
    numReg = []

    def __init__(self, number, name, family, courses=None):
        if courses is None:
            courses = []
        self.number = number
        self.numReg.append(self)
        self.name = name
        self.family = family
        self.courses = courses

    def displayStudent(self):
        print('You are logged in as ' + self.name + ' ' + self.family)

    def displayStudentCourses(self, numStudent):
        if self.number == numStudent:
            if self.courses:
                print(self.courses)
            else:
                print('You have no courses, yet!')

    def studentCourseAdding(self, wantedCourse, numStudent):
        if self.number == numStudent:
            self.courses.append(wantedCourse)
            print('You Added ' + wantedCourse + ' to your schedule, successfully!')


professor1 = Professor(1, 'X')
professor2 = Professor(2, 'Y')
professor3 = Professor(3, 'Z')
professor4 = Professor(4, 'W')

math = Course(1, 'math')
data_analyzing = Course(2, 'data analyzing')
physics = Course(3, 'physics')
dynamic = Course(4, 'dynamic')
history = Course(5, 'history')
literature = Course(6, 'literature')
chemistry = Course(7, 'chemistry')
statistics = Course(8, 'statistics')
logic_circuits = Course(9, 'logic circuits')

courseList = [k.name for k in Course.numReg]

student1 = Student(9701, 'amir', 'ahmadi')
student2 = Student(9702, 'sina', 'mohammadi')
student3 = Student(9703, 'hossein', 'faghihi')
student4 = Student(9704, 'javad', 'hatami')
student5 = Student(9705, 'mohammad', 'karimi')
student6 = Student(9706, 'amin', 'mousavi')
