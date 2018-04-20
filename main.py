from student import *
from professor import *
from course import *


def listOfCourses():
    print('Which course you wanna attend to?')
    for k in Course.numReg:
        print('%d) %s' % (k.number, k.name))

def welcomeText():
    print('Welcome to the virtual university!')
    studentOrProfessor()

def studentOrProfessor():
    print('student or professor or courses?')
    global answer
    answer = input()
    if answer == 'student':
        studentNumber()
    elif answer == 'professor':
        professorID()
    elif answer == 'courses':
        Course.displayCourse(0)
        courseAuth()
    else:
        print('Please input a valid name!')
        studentOrProfessor()


def studentNumber():
    print('Your student number?')
    global numStudent
    numStudent = int(input())
    if 9701 <= numStudent <= 9706:
        studentAuth()
    else:
        print('please write a valid student number!')
        studentNumber()


def studentAuth():
    counter = 0
    for i in Student.numReg:
        if i.number == numStudent:
            Student.displayStudent(i)
            counter += 1
    if counter == 0:
        print('You are not registered!')
        studentNumber()
    studentMenu()


def studentMenu():
    print('1) See your courses   2) Get a new course    3) Log out')
    global userOption
    userOption = int(input())
    if userOption == 1:
        seeCourses()
    elif userOption == 2:
        getNewCourse()
    elif userOption == 3:
        studentOrProfessor()
    else:
        print('please choose a valid option')
        studentMenu()


def seeCourses():
    global i
    for i in Student.numReg:
        if i.number == numStudent:
            Student.displayStudentCourses(i)
    studentMenu()

def getNewCourse():
    listOfCourses()
    selectedCourseNumber = int(input())
    if 1 <= selectedCourseNumber <= 8:
        wantedCourse = courseList[selectedCourseNumber]
        for i in Student.numReg:
            if i.number == numStudent:
                Student.studentCourseAdding(i, wantedCourse)
                for k in Course.numReg:
                    if wantedCourse == k.name:
                        nameAndFamily = i.name + ' ' + i.family
                        k.studentInCourse.append(nameAndFamily)
        studentMenu()
    else:
        print('Please choose a valid number!')
        getNewCourse()


def professorID():
    print('Your ID?')
    global numProfessor
    numProfessor = int(input())
    if 1 <= numProfessor <= 4:
        professorAuth()
    else:
        print('Please type a valid professor ID!')
        professorID()

def professorAuth():
    global j
    for j in Professor.numReg:
        if j.number == numProfessor:
            Professor.displayProfessor(j)
            global courseDict
            courseDict = j.profCourses
    professorMenu()

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


def whichCourseToSee():
    print('Which course to see the attending students?')
    for j in Professor.numReg:
        if j.number == numProfessor:
            for l in range(0, len(j.profCourses)):
                print('%d. %s' % (l + 1, j.profCourses[l]))
            courseSelectionToSeeStudents = int(input())
            if 1 <= courseSelectionToSeeStudents <= len(j.profCourses):
                studentCount = 1
                courseName = j.profCourses[courseSelectionToSeeStudents-1]
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
                print('Please select a valid course number!')
                print(courseSelectionToSeeStudents)
                print(len(j.profCourses))
                whichCourseToSee()




        # global studentCount
        # studentCount = 1
        # courseName = courseDict[professorOption]
        # for i in Student.numReg:
        #     for z in range(0, len(i.courses)):
        #         if i.courses[z] == courseName:
        #             print('%d. ' % studentCount + i.name + ' ' + i.family)
        #             studentCount += 1
        #         else:
        #             pass
        # if studentCount == 1:
        #     print('It seems that nobody has chosen this course yet!')
        # professorMenu()


def profGiveNewCourse():
    print('Which course you wanna give?')
    for k in Course.numReg:
        print('%d) %s' % (k.number, k.name))
    newCourseOption = int(input())



def courseAuth():
    courseNumber = int(input())
    if 1 <= courseNumber <= 8:
        for k in Course.numReg:
            if k.number == courseNumber:
                print('Name of course is: ' + k.name)
                print('Instructor is: ' + k.profOfCourse)
                if len(k.studentInCourse) > 0:
                    print('Attending students are: ' + str([k.studentInCourse[q] for q in range(0, len(k.studentInCourse))]))
                else:
                    print('No students attend here!')
        studentOrProfessor()
    else:
        print('please type a valid course number!')
        courseAuth()


def main():

    welcomeText()


if __name__ == '__main__':
    main()
