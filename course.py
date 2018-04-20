pStudents = []
qStudents = []
rStudents = []
sStudents = []
tStudents = []
uStudents = []
vStudents = []
wStudents = []

courseList = {1: 'math', 2: 'data analyzing', 3: 'physics', 4: 'dynamic', 5: 'history', 6: 'literature',
              7: 'chemistry', 8: 'statistics'}


class Course:

    numReg = []

    def __init__(self, number, name, profOfCourse, studentInCourse):
        self.number = number
        self.name = name
        self.profOfCourse = profOfCourse
        self.studentInCourse = studentInCourse
        self.numReg.append(self)

    def displayCourse(self):
        print('Which course do you want to see the details of?')
        for k in Course.numReg:
            print('%d) %s' % (k.number, k.name))


math = Course(1, 'math', 'X', pStudents)
data_analyzing = Course(2, 'data analyzing', 'Y', qStudents)
physics = Course(3, 'physics', 'Z', rStudents)
dynamic = Course(4, 'dynamic', 'W', sStudents)
history = Course(5, 'history', 'X', tStudents)
literature = Course(6, 'literature', 'Y', uStudents)
chemistry = Course(7, 'chemistry', 'Z', vStudents)
statistics = Course(8, 'statistics', 'W', wStudents)