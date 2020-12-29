import menu
import summary
import calculatepurchase
import displaypurchase


def cal1(ticket):
    singlecal = int(ticket) * 40
    displaypurchase.displaycal1(singlecal)
    print(singlecal)


def cal2(couple):
    couplecal = int(couple) * 70
    displaypurchase.displaycal2(couplecal)
    print(couplecal)


def cal3(group1,group2,group3):
    grouptotal = int(group1) + int(group2) + int(group3)
    displaypurchase.displaycal3(grouptotal)
    print(grouptotal)
