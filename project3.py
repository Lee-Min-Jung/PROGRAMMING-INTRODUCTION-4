#Set values for initial variables
menu1="coffee"
menu2="juice"
coffeeInventory=3
juiceInventory=2

#main function for process
def main():    
    menulist={1:"Coffee",2:"Juice"}
    while True:
        global coffeeInventory
        global juiceInventory
        try:
#When there is no coffee and juice
            if (coffeeInventory==0 and juiceInventory==0):
                print("#"*47)
                print("All sold out. Thank you for using \"Hello Cafe\".")
                print("#"*47)
                break
            else:
#When there are some coffee or juice left
                displayMenu()
                menuSelect=int(input("Please enter a menu 1 or 2:"))
                print("You chose " + menulist[menuSelect])
        except KeyError:
            print("There are only 1 and 2 on the menu. Please enter a valid menu number.")
        except ValueError:
            print("Please enter a number for the menu.")
        else:
            if menuSelect==1:
               coffeeInventory=check(menu1,coffeeInventory)
            elif menuSelect==2:
               juiceInventory=check(menu2,juiceInventory)
#function for menu displaying
def displayMenu():
    print("*"*20)
    print("{0:^20s}".format("Hello Cafe"))
    print("*"*20)
    print("1. Coffee")
    print("2. Juice \n")
#function when customer selecting menu              
def check(menu,inventory):
    global coffeeInventory
    global juiceInventory
    if inventory==0:
        print("There is no " +menu+ " left.")
        return inventory
    else: 
        while True:
            try:
                quantity=int(input("Please give a quantity."))
                if quantity<=inventory:
                    print("Here it is.")
                    inventory -=quantity
                    return inventory
                else:
                    continue
            except ValueError:
                print("You have to enter a right quantity of menu in number")
            finally:
                print(str(inventory) + " "+ menu+" is(are) left.")
main()
    
        
  
            
    

    
