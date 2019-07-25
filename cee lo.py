'''
cee lo scoring:
4-5-6 
The highest possible roll. If you roll 4-5-6, you automatically win.
Trips 
Rolling three of the same number is known as rolling "trips". Higher trips beat lower trips, so 4-4-4 is better than 3-3-3. Any trips beats any established point.
Point 
Rolling a pair, and another number, establishes the singleton as a "point". A higher point beats a lower point, so 2-2-6 is better than 5-5-2.
1-2-3
The lowest possible roll. If you roll 1-2-3, you automatically lose.
'''

def main():
    L=[]
    CPU=[]
    
    from random import randint
    for i in range(3): # allows up to 3 rolls per player
        if checkWin(L) == 0:
            L=[]
            for i in range(3): # rolls a set of 3 D6 for the player
                L.insert(0,randint(1, 6))
            L.sort()
            print("your roll",L)
        if checkWin(CPU) == 0:
            CPU=[]
            for i in range(3): # rolls a set of 3 D6 for the CPU
                CPU.insert(0,randint(1, 6))
            CPU.sort()
            print("enemy roll",CPU)

        if (checkWin(L) == -1 or checkWin(CPU) == -1 or checkWin(L) == 13 or checkWin(CPU) == 13):#ends loop the moment a 1,2,3 or 4,5,6 is rolled
            break


    if checkWin(L) > checkWin(CPU):
        print("Y O U W I N!")
    elif checkWin(L) < checkWin(CPU):
        print("you lose")
    else:
        print("It's a tie")

def checkWin(L):# assigns value denoting the relative score of every possible scoring roll
    if L == []:
        return 0
    score = 0
    if (L == [4, 5, 6]):
        score = 13
    elif (L[0] == L[1] and L[1] == L[2]): # Triple
        score = L[0] + 6
    elif (L[0] == L[1]): # Double
        score = L[2]
    elif (L[1] == L[2]): # Double
        score = L[0]
	elif (L[0] == L[2]): # Double
		score = L[1]
    elif (L == [1, 2, 3]):
        score = -1
    return score

main()
