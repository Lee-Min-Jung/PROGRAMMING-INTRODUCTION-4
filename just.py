def selecting(listOfNames,listOfQuantity):
    while True:
        print("*"*47)
        print("Welcome to Hello cafe")
        print("*"*47)
        for i in range(len(listOfNames)):
            print(i+1,")",listOfNames[i],"(quantity:",listOfQuantity[i],")")
        selectMenuOn='Y'
        while selectMenuOn=='Y':
            try:
                selectMenu=int(input("Enter menu number: "))-1
            except:
                print("Please enter number.")
                continue
            else:
                selectMenuOn='N'
                selectQuantityOn='Y'
                while selectQuantityOn=='Y':
                    try:
                        selectQuantity=int(input("Enter quantity"))
                    except:
                        print("You have to enter number.")
                    else:
                        selectQuantityOn=='N'
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


