import random
import time



def rolldice():
    dice = [0,0,0]
    dice[0] = random.randint (1,6)
    dice[1] = random.randint (1,6)
    dice[2] = random.randint (1,6)
    print ("The dice have been rolled, and the results are...")
    time.sleep (2)
    print ("     ",dice[0])
    time.sleep (1)
    print ("     ",dice[1])
    time.sleep (1)
    print ("     ",dice[2],"\n")
    time.sleep (1)
    dicetotal = sum(dice)
    print("The total is",dicetotal,"!")
    return dice


def bet():
    repbet = 0
    while repbet == 0:
        repbet = 1
        bet1 = input ("""
1. Small (total between 4-10) [1-1]
2. Big   (total between 11-7) [1-1]
3. Total                      [1-6 to 1-60]
4. 1 Die                      [1-1 to 1-3]
""")

        if bet1 == "1":
            return ("small")
        if bet1 == "2":
            return ("big")

        if bet1 == "3":
            bet4 = input ("""
1. 4   [1-60]
2. 5   [1-20]
3. 6   [1-18]
4. 7   [1-12]
5. 8   [1-8]
6. 9   [1-6]
7. 10  [1-6]
8. 11  [1-6]
9. 12  [1-6]
10. 13 [1-8]
11. 14 [1-12]
12. 15 [1-18]
13. 16 [1-20]
14. 17 [1-60]
15. Back
""")
            if bet4 == "1":
                return ("Total 4")
            if bet4 == "2":
                return ("Total 5")
            if bet4 == "3":
                return ("Total 6")
            if bet4 == "4":
                return ("Total 7")
            if bet4 == "5":
                return ("Total 8")
            if bet4 == "6":
                return ("Total 9")
            if bet4 == "7":
                return ("Total 10")
            if bet4 == "8":
                return ("Total 11")
            if bet4 == "9":
                return ("Total 12")
            if bet4 == "10":
                return ("Total 13")
            if bet4 == "11":
                return ("Total 14")
            if bet4 == "12":
                return ("Total 15")
            if bet4 == "13":
                return ("Total 16")
            if bet4 == "14":
                return ("Total 17")
            if bet4 == "15":
                repbet = 0


bankroll = int(input("How much would you like to buy in for? :"))

while bankroll != 0:
    print("You have $"+str(bankroll)+" remaining.")
    betamount = int(input("How much would you like to bet? :"))

    if betamount<=bankroll:
        print("Bet accepted!")
        bankroll-=betamount
    else:
        print("Invalid amount! Bet what you can afford!")
        continue
    betlod = bet()
    dicetotal=rolldice()
    dicetotaltemp = dicetotal[0]+dicetotal[1]+dicetotal[2]
    if betlod == "small":
        if dicetotaltemp >= 4 and dicetotaltemp <= 10:
            print("Nice lah! You won $",betamount)
            bankroll+=betamount*2
        else:
            print("Bad luck!")
    elif betlod == "big":
        if dicetotaltemp >=11 and dicetotaltemp<18:
            print("Cool beans! You won $", betamount)
            bankroll+=betamount*2
        else:
            print("Unlucky!")
    elif betlod == "Total 4":
        if dicetotaltemp == 4:
            print("You win $",str(60*betamount))
            bankroll+=60*betamount
        else:
            print("Unlucky!")
    elif betlod == "Total 5":
        if dicetotaltemp == 5:
            print("You win $", str(20 * betamount))
            bankroll += 20 * betamount
        else:
            print("Unlucky!")
    elif betlod == "Total 6":
        if dicetotaltemp == 6:
            print("You win $", str(18*betamount))
            bankroll+=18*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 7":
        if dicetotaltemp == 7:
            print("You win $", str(12*betamount))
            bankroll+=12*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 8":
        if dicetotaltemp == 8:
            print("You win $", str(8*betamount))
            bankroll+=8*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 9":
        if dicetotaltemp == 9:
            print("You win $", str(6*betamount))
            bankroll+=6*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 10":
        if dicetotaltemp == 10:
            print("You win $", str(6*betamount))
            bankroll+=6*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 11":
        if dicetotaltemp == 11:
            print("You win $", str(6*betamount))
            bankroll+=6*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 12":
        if dicetotaltemp == 12:
            print("You win $", str(6*betamount))
            bankroll+=6*betamount

        else:
            print("Sorry! You lose.")
    elif betlod == "Total 13":
        if dicetotaltemp == 13:
            print("You win $", str(8*betamount))
            bankroll+=8*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 14":
        if dicetotaltemp == 14:
            print("You win $", str(12*betamount))
            bankroll+=12*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 15":
        if dicetotaltemp == 15:
            print("You win $", str(18*betamount))
            bankroll+=18*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 16":
        if dicetotaltemp == 16:
            print("You win $", str(20*betamount))
            bankroll+=20*betamount
        else:
            print("Sorry! You lose.")
    elif betlod == "Total 17":
        if dicetotaltemp == 17:
            print("You win $", str(60*betamount))
            bankroll+=60*betamount
        else:
            print("Sorry! You lose.")




