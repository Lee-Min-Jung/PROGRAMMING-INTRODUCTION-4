


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

class Exception(Cafe):
    def exc1(var,inputSentence,errSentence):
        while True:
            try:
                var=input(inputSentence)
            except:
                print(errSentence)
            else:
                break

    def exc2(var,inputSentence,errSentence):
        while True:
            try:
                var=int(input(inputSentence))
            except:
                print(errSentence)
            else:
                break
        
    def exc3(var,inputSentence,errSentence,categoryDic):
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
    st = Exception("a")
    listOfMenus=[]
    carryOn='Y'
    
    while carryOn=='Y':
        (st._name,"Enter menu's name:","Enter menu's name:")
        (st._quantity,"Enter initial quantity of menu: ","Enter quantity in number:")
        (st._name,"Enter category(FOOD or DRINK):","Enter category(FOOD or DRINK):",{"drink":"drink","food":"food"})
        
                            
                            
                        

                
            

def displayResults(listOfMenus):
    print("*"*47)
    print("Welcome to Hello cafe")
    print("*"*47)
    for pupil in listOfMenus:
        print(pupil,end="")
        
    
   
main()
    

    