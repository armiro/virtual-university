from course import *

pp = ['math', 'literature']
qq = []
rr = []
ss = []

class Professor:
    """common base class for all professors"""
    numReg = []

    def __init__(self, number, family, profCourses=[]):
        self.number = number
        self.numReg.append(self)
        self.family = family
        self.profCourses = profCourses

    def displayProfessor(self):
        print('Welcome Dear Dr.' + self.family)
        print('You are the instructor of %d courses ' % len(self.profCourses))


professor1 = Professor(1, 'X', pp)
professor2 = Professor(2, 'Y', qq)
professor3 = Professor(3, 'Z', rr)
professor4 = Professor(4, 'W', ss)

