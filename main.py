from classes import Student
from classes import Course
from classes import Professor

# display the welcome text
def welcomeText():
    print('Welcome to the virtual university!')
    studentOrProfessor()

# the main menu
def studentOrProfessor():
    print('1) student   2) professor    3) see the courses')
    try:
        answer = int(input())
    except:
        print('Please choose a valid number from the main menu!')
        studentOrProfessor()
    if answer == 1:
        studentNumber()
    elif answer == 2:
        professorID()
    elif answer == 3:
        seeTheCourses()
    else:
        print('Please input a valid name!')
        studentOrProfessor()

# check the student's number
def studentNumber():
    print('Your student number?')
    global numStudent
    numStudent = int(input())
    if 9701 <= numStudent <= 9706:
        studentAuth()
    else:
        print('please write a valid student number!')
        studentNumber()

# the students number is valid, now display student name & family
def studentAuth():
    for i in Student.numReg:
        if i.number == numStudent:
            Student.displayStudent(i)
    studentMenu()

# student logged in, now see the menu: see/get courses or log out
def studentMenu():
    print('1) See your courses   2) Get a new course    3) Log out')
    userOption = int(input())
    if userOption == 1:
        seeStudentCourses()
    elif userOption == 2:
        getNewCourse()
    elif userOption == 3:
        studentOrProfessor()
    else:
        print('Please choose a valid option from the student menu')
        studentMenu()

# the student can see the courses he has
def seeStudentCourses():
    Student.displayStudentCourses(0, numStudent)
    studentMenu()

# the student can choose a new course to attend
def getNewCourse():
    print('Which course you wanna attend to?')
    Course.displayCourses(0)
    selectedCourseNumber = int(input())
    if 1 <= selectedCourseNumber <= 8:
        Student.studentCourseAdding(0, selectedCourseNumber, numStudent)
        Course.newStudentGotACourse(0, numStudent, selectedCourseNumber)
        studentMenu()
    else:
        print('Please choose a valid number!')
        getNewCourse()

# check the professor's ID
def professorID():
    print('Your ID?')
    global numProfessor
    numProfessor = int(input())
    if 1 <= numProfessor <= 4:
        professorAuth()
    else:
        print('Please type a valid professor ID!')
        professorID()

# the professor ID is valid, now display his family
def professorAuth():
    Professor.displayProfessor(0, numProfessor)
    professorMenu()

# the professor logged in, now see the menu: see attending students, give a new courses or log out
def professorMenu():
    print('1) See attending students    2) Give a new course!   3) Log out')
    professorOption = int(input())
    if professorOption == 1:
        for j in Professor.numReg:
            if j.number == numProfessor:
                if len(j.profCourses) == 0:
                    print('You have not instructed any courses, yet!')
                    professorMenu()
                else:
                    whichCourseToSee()

    elif professorOption == 2:
        profGiveNewCourse()
    elif professorOption == 3:
        studentOrProfessor()
    else:
        print('please choose a valid option')
        professorMenu()

# the professor has instructed some courses, see which one to display the attending students
def whichCourseToSee():
    print('Which course to see the attending students?')
    for j in Professor.numReg:
        if j.number == numProfessor:
            for l in range(0, len(j.profCourses)):
                print('%d. %s' % (l + 1, j.profCourses[l]))

            courseSelectionToSeeStudents = int(input())

            if 1 <= courseSelectionToSeeStudents <= len(j.profCourses):
                studentCount = 1
                courseName = j.profCourses[courseSelectionToSeeStudents - 1]
                for i in Student.numReg:
                    for z in range(0, len(i.courses)):
                        if i.courses[z] == courseName:
                            print('%d. ' % studentCount + i.name + ' ' + i.family)
                            studentCount += 1
                        else:
                            pass

                if studentCount == 1:
                    print('It seems that nobody has chosen this course yet!')

                professorMenu()

            else:
                print('Please choose a valid course number!')
                whichCourseToSee()

# the professor wants to give a new course!
def profGiveNewCourse():
    print('Which course you wanna give?')
    Course.displayCourses(0)
    newCourseOption = int(input())
    if 1<= newCourseOption <= 8:
        Professor.professorCourseGiving(0, newCourseOption, numProfessor)
        professorMenu()
    else:
        print('Please choose a valid course number!')
        profGiveNewCourse()

# the user selected to see the course details (option 3 in main menu)
def seeTheCourses():
    print('Which course to see the details of?')
    Course.displayCourses(0)
    courseNumber = int(input())
    if 1 <= courseNumber <= 8:
        Course.displayCourseDetails(0, courseNumber)
        studentOrProfessor()
    else:
        print('please type a valid course number!')
        seeTheCourses()

# the main function
def main():
    welcomeText()

if __name__ == '__main__':
    main()
