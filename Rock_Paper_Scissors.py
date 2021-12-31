#Greatings.
print("Welcome to Rock Paper Scissors By i_4th4rv4_8!!!")
#Taking the names of the players.
player1=str(input("Enter your the name of First Player:"))
player2=str(input("Enter your the name of Second Player:"))
player1=player1.title()
player2=player2.title()
#Taking the number of times they want to play.
ntime=int(input("Enter the number of times you want to play:"))
i=1 #Here i is number of turns.
while(i<=ntime):
    print("#"*30)
    print("This is your ",i,"turn.")
    i+=1
    p1=int(input(player1+" : 1.Rock | 2.Paper | 3.Scissors:"))
    p2=int(input(player2+" :1.Rock | 2.Paper | 3.Scissors:")) 
    if p1>3 or p2>3:
        print("Invalid Option. Try Again.")
    elif p1==1 and p2==3:
        print(player1+" wins.")    
    elif p1==2 and p2==3:
        print(player2+" wins.")    
    elif p1==3 and p2==2:
        print(player1+" wins.")
    else:
        print("Try Again.")
print("Thank you for playing!! See You Next Time.")

