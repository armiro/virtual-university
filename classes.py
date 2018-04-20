pCourses = [None]
qCourses = [None]
rCourses = [None]
sCourses = [None]
tCourses = [None]
uCourses = [None]

pStudents = []
qStudents = []
rStudents = []
sStudents = []
tStudents = []
uStudents = []
vStudents = []
wStudents = []

pp = []
qq = []
rr = []
ss = []

courseList = {1: 'math', 2: 'data analyzing', 3: 'physics', 4: 'dynamic',
              5: 'history', 6: 'literature', 7: 'chemistry', 8: 'statistics'}

class Course:
    """common base class for all courses"""
    numReg = []

    def __init__(self, number, name, profOfCourse, studentInCourse):
        self.number = number
        self.name = name
        self.profOfCourse = profOfCourse
        self.studentInCourse = studentInCourse
        self.numReg.append(self)

    def displayCourses(self):
        for k in Course.numReg:
            print('%d) %s' % (k.number, k.name))

    def displayCourseDetails(self, courseNumber):
        for k in Course.numReg:
            if k.number == courseNumber:
                print('Name of course is: ' + k.name)
                print('Instructor is: ' + k.profOfCourse)
                if len(k.studentInCourse) > 0:
                    print('Attending students are: ' + str([k.studentInCourse[q] for q in range(0, len(k.studentInCourse))]))
                else:
                    print('No students attend here!')

    def newStudentGotACourse(self, numStudent, selectedCourseNumber):
        wantedCourse = courseList[selectedCourseNumber]
        for k in Course.numReg:
            if wantedCourse == k.name:
                for i in Student.numReg:
                    if numStudent == i.number:
                        nameAndFamily = i.name + ' ' + i.family
                        k.studentInCourse.append(nameAndFamily)

class Professor:
    """common base class for all professors"""
    numReg = []

    def __init__(self, number, family, profCourses=[]):
        self.number = number
        self.numReg.append(self)
        self.family = family
        self.profCourses = profCourses

    def displayProfessor(self, numProfessor):
        for j in Professor.numReg:
            if j.number == numProfessor:
                print('Welcome Dear Dr.' + j.family)
                print('You are the instructor of %d course(s) ' % len(j.profCourses))
                # courseDict = j.profCourses

    def professorCourseGiving(self, newCourseOption, numProfessor):
        for k in Course.numReg:
            if k.number == newCourseOption:
                for j in Professor.numReg:
                    if j.number == numProfessor:
                        j.profCourses.append(k.name)
        print('You are now the instructor of %s!' % courseList[newCourseOption])

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

    def displayStudentCourses(self, numStudent):
        for i in Student.numReg:
            if i.number == numStudent:
                if i.courses == [None]:
                    print('You have no courses, yet!')
                else:
                    if i.courses[0] is None:
                        del i.courses[0]
                        print(i.courses)
                    else:
                        print(i.courses)

    def studentCourseAdding(self, selectedCourseNumber, numStudent):
        wantedCourse = courseList[selectedCourseNumber]
        for i in Student.numReg:
            if i.number == numStudent:
                if i.courses[0] is None:
                    del i.courses[0]
                    i.courses.append(wantedCourse)
                else:
                    i.courses.append(wantedCourse)
                print('You Added ' + wantedCourse + ' to your schedule, successfully!')


professor1 = Professor(1, 'X', pp)
professor2 = Professor(2, 'Y', qq)
professor3 = Professor(3, 'Z', rr)
professor4 = Professor(4, 'W', ss)

math = Course(1, 'math', 'X', pStudents)
data_analyzing = Course(2, 'data analyzing', 'Y', qStudents)
physics = Course(3, 'physics', 'Z', rStudents)
dynamic = Course(4, 'dynamic', 'W', sStudents)
history = Course(5, 'history', 'X', tStudents)
literature = Course(6, 'literature', 'Y', uStudents)
chemistry = Course(7, 'chemistry', 'Z', vStudents)
statistics = Course(8, 'statistics', 'W', wStudents)

student1 = Student(9701, 'amir', 'ahmadi', pCourses)
student2 = Student(9702, 'sina', 'mohammadi', qCourses)
student3 = Student(9703, 'hossein', 'faghihi', rCourses)
student4 = Student(9704, 'javad', 'hatami', sCourses)
student5 = Student(9705, 'mohammad', 'karimi', tCourses)
student6 = Student(9706, 'amin', 'mousavi', uCourses)
