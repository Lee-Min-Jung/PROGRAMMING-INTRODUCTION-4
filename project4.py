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
        name=input("Enter menu's name: ")
        quantity=int(input("Enter initial quantity of menu: "))
        category = input("Enter category(DRINK or FOOD): ")
        if category.upper()=="DRINK":
            st = Drink(name,quantity)
        else:
            question=input("Enter warming option(WARM or COLD): ")
            if question.upper()=="WARM":
                isWarm=True
            else:
                isWarm=False
            st=Food(name,quantity,isWarm)
        listOfMenus.append(st)
        listOfNames.append(st._name)
        listOfQuantity.append(st._quantity)
        carryOn=input("Do you wnat to continue?(Y or N")
        carryOn=carryOn.upper()

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
        


    






main()