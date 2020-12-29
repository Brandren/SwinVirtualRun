import menu
import summary
import calculatepurchase
import displaypurchase

def mainmenu():
    print("~~ Swin Virtual Run ~~\n")
    print("[1] Single Registration")
    print("[2] Couple Registration")
    print("[3] Group Registration")
    print("[4] Calculate and Quit\n\n")
    print("[0] Summary\n")
    choice= input("Choice:")
    if int(choice) == 1:
        ticket = input("How many single ticket?")
        print("Registration for "+str(ticket)+" runner is successful")
        calculatepurchase.cal1(ticket)
        print("")
        menu.mainmenu()
    elif int(choice) == 2:
        couple = input("How many couple?")
        print("Registration for "+str(couple)+" couple is successful")
        calculatepurchase.cal2(couple)
        print("")
        menu.mainmenu()
    elif int(choice) == 3:
        menu.groupmenu()
        print("")
        menu.mainmenu()
    elif int(choice) == 4:
        displaypurchase.displaybuy()
    elif int(choice) == 0:
        summary.summary()
        menu.mainmenu()
    else:
        print("Please select correct choice menu !!!")
        menu.mainmenu()



def groupmenu():
    print("[1] Group of 4\t\tRM128")
    print("[2] Group of 6\t\tRM168")
    print("[3] More than 6\t\tRM25/person\n\n")
    choice= input("Choice:")
    group = [0, 0, 0]
    if int(choice) == 1:
        print("Registration for [1] Group of 4 RM128 is successful")
        group[0] += 128
        calculatepurchase.cal3(group[0],group[1],group[2])
    elif int(choice) == 2:
        print("Registration for [2] Group of 6 RM168 is successful")
        group[1] += 168
        calculatepurchase.cal3(group[0],group[1],group[2])
    elif int(choice) == 3:
        more = input("How many runner to register?")
        while int(more) > 0:
            if int(more) >= 6:
                print("Registration for "+ str(more) + " runner is successful")
                calmore = int(more) * 25
                group[2] += calmore
                calculatepurchase.cal3(group[0],group[1],group[2])
                break
            else:
                more = input("How many runner to register?")
