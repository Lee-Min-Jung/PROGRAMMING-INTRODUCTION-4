class Student:
    def __init__(self,name="",midterm=0,final=0):
        self._name = name
        self._midterm = 0
        self._final = 0
    def setName(self,name):
        self._name=name
    def setMidterm(self,midterm):
        self._midterm=midterm
    def setFinal(self,final):
        self._final = final
    def getName(self):
        return self._name
    def __str__(self):
        return self._name + "\t" + self.calcSemGrade()

class LGstudent(Student):
    def calcSemGrade(self):
        average = round((self._midterm + self._final)/2)
        if average>=90:
            return "A"
        elif average >=80:
            return "B"
        elif average >=70:
            return "C"
        elif average >=60:
            return "D"
        else:
            return "F"

class PFstudent(Student):
    def __init__(self, name="", midterm=0,final=0,fullTime=True):
        super().__init__(name,midterm,final)
        self._fullTime=fullTime
    def setFullTime(self,fullTime):
        set._fullTime=fullTime
    def getFullTime(self):
        return self._fullTime
    def calcSemGrade(self):
        average = round((self._midterm+self._final)/2)
        if average >=60:
            return "Pass"
        else:
            return "Fail"
    def __str__(self):
        if self._fullTime:
            status="Full-time student"
        else:
            status="Part-time student"
        return (self._name+"\t"+self.calcSemGrade()+"\t" + status)
   

def main():
    listOfStudnets = obtainListOfStudents()
    displayResults(listOfStudnets)

def obtainListOfStudents():
    listOfStudnets=[]
    carryOn='Y'
    while carryOn=='Y':
        name=input("Enter student's name: ")
        midterm=float(input("Enter student's grade on midterm exam: "))
        final=float(input("Enter student's grade on final: "))
        category = input("Enter category: ")
        if category.upper()=="LG":
            st = LGstudent(name,midterm,final)
        else:
            question=input("Is " + name + "a full time student?")
            if question.upper()=="Y":
                fullTime=True
            else:
                fullTime=False
            st=PFstudent(name,midterm,final,fullTime)
        listOfStudnets.append(st)
        carryOn=input("Do you wnat to continue?")
        carryOn=carryOn.upper()
    return listOfStudnets

def displayResults(listOfStudents):
    print("\nNAME\tGRADE")
    numberOfLGstudents=0
    listOfStudents.sort(key=lambda x: x.getName())
    for pupil in listOfStudents:
        print(pupil)
        if isinstance(pupil,LGstudent):
            numberOfLGstudents +=1
    print("Number of letter-grade students: ", numberOfLGstudents)
    print("Number of pass-fail students: ", len(listOfStudents)-numberOfLGstudents)

main()
    
