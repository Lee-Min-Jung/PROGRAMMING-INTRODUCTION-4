


class Cafe:
    def __init__(self,name="",quantity=0):
        self._name = name
        self._quantity=quantity
    def setName(self,name):
        self._name=name
    def setQuantity(self,quantity):
        self._quantity=quantity
    def getName(self):
        return self._name
    def __str__(self):
        return self._name +"(quantity=" + str(self._quantity) + ")\n"
        
class Drink(Cafe):
    pass

class Food(Cafe):
    def __init__(self, name="", quantity=0, isWarm=True):
        super().__init__(name,quantity)
        self._isWarm=isWarm
    def setIsWarm(self,isWarm):
        self._isWarm=isWarm
    def getIsWarm(self):
        return self._isWarm
   
def main():
    listOfMenus = obtainListOfMenus()
    displayResults(listOfMenus)

def exception(var,inputSentence,errSentence):
    while True:
        try:
            var=input(inputSentence)
        except:
            print(errSentence)
        else:
            break

def exception2(var,inputSentence,errSentence):
    while True:
        try:
            var=int(input(inputSentence))
        except:
            print(errSentence)
        else:
            break
        
def exception3(var,inputSentence,errSentence,categoryDic):
    
    while True:
        try:
            categoryDic
            var=input(inputSentence)
            categoryDic[categoryDic]
        except:
            print(errSentence)
        else:
            break

def obtainListOfMenus():
    st = Cafe("a")
    listOfMenus=[]
    carryOn='Y'
    
    while carryOn=='Y':
        exception(st._name,"Enter menu's name:","Enter menu's name:")
        exception2(st._quantity,"Enter initial quantity of menu: ","Enter quantity in number:")
        exception3(st._name,"Enter category(FOOD or DRINK):","Enter category(FOOD or DRINK):",{"drink":"drink","food":"food"})
        if .upper()=="DRINK":
            st = Drink(name,quantity)
        else:
                            
                            
                        
#                         except:
#                             print("Enter category")
#                         else:
#                             while carryOn=='Y':
                                
                                    while carryOn=='Y':
                                        try:
                                            checkQuestion={"warm":"warm","cold":"cold"}
                                            question=input("Enter warming option(WARM or COLD): ")
                                            checkQuestion[question]
                                        except:
                                            print("Enter warm or cold")
                                        else:
                                            if question.upper()=="WARM":
                                                isWarm=True
                                            else:
                                                isWarm=False
                                                st=Food(name,quantity,isWarm)
                                                listOfMenus.append(st)
                                                while carryOn=='Y':
                                                    try:
                                                        checkCarryOn={"Y":"Y","N":"N"}
                                                        carryOn=input("Do you wnat to continue?(Y or N")
                                                    except:
                                                        print("Enter Y or N")
                                                    else:
                                                        carryOn=carryOn.upper()
    
    return listOfMenus
            

def displayResults(listOfMenus):
    print("*"*47)
    print("Welcome to Hello cafe")
    print("*"*47)
    for pupil in listOfMenus:
        print(pupil,end="")
        
    
   
main()
    

    