from student import Student

class Course:
    """common base class for all courses"""
    numReg = []

    # basic init method for Course class
    def __init__(self, number, name, profOfCourse=None, studentInCourse=None):
        if studentInCourse is None:
            studentInCourse = []
        self.number = number
        self.name = name
        self.profOfCourse = profOfCourse
        self.studentInCourse = studentInCourse
        self.numReg.append(self)

    # when called, it'll display course number and name
    def displayCourses(self):
        print('%d) %s' % (self.number, self.name))

    # when called, it'll display name, instructor and attending students in a course
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

    # when called, it will add the name & family of new student to the studentInCourse list
    def newStudentGotACourse(self, numStudent, wantedCourse):
        if wantedCourse == self.name:
            for i in Student.numReg:
                if numStudent == i.number:
                    nameAndFamily = i.name + ' ' + i.family
                    self.studentInCourse.append(nameAndFamily)
