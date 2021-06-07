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
    def getQuantity(self):
        return self._quantity
    def __str__(self):
        return self._name +"(quantity=" + str(self._quantity) + ")\n"

class Drink(Cafe):
    pass

class Food(Cafe):
    def __init__(self, name="", quantity=0, isWarm=True):
        super().__init__(name,quantity)
        self._isWarm=isWarm
    def setIsWarm(self,isWarm):
        set._isWarm=isWarm
    def getIsWarm(self):
        return self._isWarm


def main():
    listOfMenus=[]
    listOfNames=[]
    listOfQuantity=[]
    carryOn='Y'
    while carryOn=='Y':
        nameOn='Y'
        while nameOn=='Y':
            try:
                name=input("Enter menu's name: ")
            except:
                print("Please enter menu's name.")
                continue
            else:
                nameOn='N'
                quantityOn='Y'
                while quantityOn=='Y':
                    try:
                        quantity=int(input("Enter initial quantity of menu: "))
                    except:
                        print("Please enter quantity in number.")
                        continue
                    else:
                        quantityOn='N'
                        categoryOn='Y'
                        baseCategory={"DRINK":"DRINK","drink":"drink","FOOD":"FOOD","food":"food"}
                        while categoryOn=='Y':
                            try:
                                category = input("Enter category of menu(DRINK/FOOD) ")
                                category = baseCategory[category]
                            except:
                                print("You have to enter drink or food")
                                continue
                            else:
                                categoryOn='N'
                                if category.upper()=="DRINK":
                                    st = Drink(name,quantity)
                                else:
                                    questionOn='Y'
                                    baseQuestion={"WARM":"WARM","warm":"warm","COLD":"COLD","cold":"cold"}
                                    while questionOn=='Y':
                                        try:
                                            question=input("Enter warming option(WARM/COLD)")
                                            question=baseQuestion[question]
                                        except:
                                            print("You have to enter warm or cold.")
                                            continue
                                        else:
                                            questionOn='N'
                                            if question.upper()=="WARM":
                                                isWarm=True
                                            else:
                                                isWarm=False
                                                st=Food(name,quantity,isWarm)
        listOfMenus.append(st)
        listOfNames.append(st._name)
        listOfQuantity.append(st._quantity)
        carryOn=input("Do you wnat to continue?(Y or N)")
        carryOn=carryOn.upper()   
    selecting(listOfNames,listOfQuantity)

def selecting(listOfNames,listOfQuantity):
    while True:
        print("*"*47)
        print("Welcome to Hello cafe")
        print("*"*47)
        for i in range(len(listOfNames)):
            print(i+1,")",listOfNames[i],"(quantity:",listOfQuantity[i],")")

        selectMenu=int(input("Enter menu"))-1
        selectQuantity=int(input("Enter quantity"))
        listOfQuantity[selectMenu] -= selectQuantity
        if listOfQuantity[selectMenu]==0:
            print("no left. delete " + listOfNames[selectMenu])
            del listOfNames[selectMenu]
            del listOfQuantity[selectMenu]
            if len(listOfNames)==0:
                print("All sold out")
                break
        else:
            continue
main()