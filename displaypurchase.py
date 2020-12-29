import menu
import summary
import calculatepurchase
import displaypurchase

buy = [0,0,0,0]
def displaycal1(singlecal):
    cal1 = int(singlecal)
    buy[0] = cal1


def displaycal2(couplecal):
    cal2 = int(couplecal)
    buy[1] = cal2


def displaycal3(grouptotal):
    cal3 = int(grouptotal)
    buy[2] = cal3



def displaybuy():
    print("~~ Swin Virtual Run ~~")
    f = open("SwinVirtualRun.txt", "a")
    f.write("~~ Transaction entry ~~"+"\n")
    print("Single registration total: RM"+str(buy[0]))
    f.write("Single registration total: RM"+str(buy[0])+"\n")
    print("Couple registration total: RM"+str(buy[1]))
    f.write("Couple registration total: RM"+str(buy[1])+"\n")
    print("Group registration total: RM"+str(buy[2]))
    f.write("Group registration total: RM"+str(buy[2])+"\n")
    buy[3] = buy[0]+buy[1]+buy[2]
    print("Total purchase: RM"+str(buy[3])+"\n")
    f.write("Total purchase: RM"+str(buy[3])+"\n\n")
    f.close()
    print("~~Thank you. Program terminates.~~")
    input("~~Press enter to exit.~~")
