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
3. Doubles                    [1-11]
4. Triples                   [1-180 or 1-30]   
5. Total                      [1-6 to 1-60]
6. 2 Die                      [1-6]
7. 1 Die                      [1-1 to 1-3]

""")

        if bet1 == "1":
            return ("small")
        if bet1 == "2":
            return ("big")
        if bet1 == "3":
            bet2 = input ("""
[all are 1-11 odds]

1. 1 and 1
2. 2 and 2
3. 3 and 3
4. 4 and 4
5. 5 and 5
6. 6 and 6
7. Back

""")
            if bet2 == "1":
                return ("Doubles 1 and 1")
            if bet2 == "2":
                return ("Doubles 2 and 2")
            if bet2 == "3":
                return ("Doubles 3 and 3")
            if bet2 == "4":
                return ("Doubles 4 and 4")
            if bet2 == "5":
                return ("Doubles 5 and 5")
            if bet2 == "6":
                return ("Doubles 6 and 6")
            if bet2 == "7":
                repbet = 0
        if bet1 == "4":
            bet3 = input ("""
1. 1-1-1 [1-180]
2. 2-2-2 [1-180]
3. 3-3-3 [1-180]
4. 4-4-4 [1-180]
5. 5-5-5 [1-180]
6. 6-6-6 [1-180]
7. Any   [1-30]
8. Back

""")
            if bet3 == "1":
                return ("Triples 1 and 1")
            if bet3 == "2":
                return ("Triples 2 and 2")
            if bet3 == "3":
                return ("Triples 3 and 3")
            if bet3 == "4":
                return ("Triples 4 and 4")
            if bet3 == "5":
                return ("Triples 5 and 5")
            if bet3 == "6":
                return ("Triples 6 and 6")
            if bet3 == "7":
                return ("Triples any")
            if bet3 == "8":
                repbet = 0
        if bet1 == "5":
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
        if bet1 == "6":
            bet5 = input ("""
[all are 1-6]

1.  1 and 2
2.  1 and 3
3.  1 and 4
4.  1 and 5
5.  1 and 6
6.  2 and 3
7.  2 and 4
8.  2 and 5
9.  2 and 6
10. 3 and 4
11. 3 and 5
12. 3 and 6
13. 4 and 5
14. 4 and 6
15. 5 and 6
16. Back

""")
            if bet5 == "1":
                return ("2Die 12")
            if bet5 == "2":
                return ("2Die 13")
            if bet5 == "3":
                return ("2Die 14")
            if bet5 == "4":
                return ("2Die 15")
            if bet5 == "5":
                return ("2Die 16")
            if bet5 == "6":
                return ("2Die 23")
            if bet5 == "7":
                return ("2Die 24")
            if bet5 == "8":
                return ("2Die 25")
            if bet5 == "9":
                return ("2Die 26")
            if bet5 == "10":
                return ("2Die 34")
            if bet5 == "11":
                return ("2Die 35")
            if bet5 == "12":
                return ("2Die 36")
            if bet5 == "13":
                return ("2Die 45")
            if bet5 == "14":
                return ("2Die 46")
            if bet5 == "15":
                return ("2Die 56")
            if bet5 == "16":
                repbet = 0
        if bet1 == "7":
            bet6 = input ("""
[1:1 if 1 die is correct, 2:1 if 2 dice are correct, 3:1 if 3 are correct]

1. ONE
2. TWO
3. THREE
4. FOUR
5. FIVE
6. SIX
7. Back

""")
            if bet6 == "1":
                return ("1Die 1")
            if bet6 == "2":
                return ("1Die 2")
            if bet6 == "3":
                return ("1Die 3")
            if bet6 == "4":
                return ("1Die 4")
            if bet6 == "5":
                return ("1Die 5")
            if bet6 == "6":
                return ("1Die 6")
            if bet6 == "7":
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
    print("The result is ",betlod)
    if betlod == "small":
        if dicetotaltemp >= 4 and dicetotaltemp <= 10:
            print("Nice lah! You won $",betamount)
            bankroll+=betamount*2
        else:
            print("Bad luck mate! XD")
    elif betlod == "big":
        if dicetotaltemp >=11 and dicetotaltemp<18:
            print("Cool beans! You won $", betamount)
            bankroll+=betamount*2
        else:
            print("Haix unlucky! Lose loh!")








