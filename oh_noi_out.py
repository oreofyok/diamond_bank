import random
from rock_paper_scissors import play

def playing():
    user = input("What's your choice? 'f' for front and 'b' for back please choose : ")
    computer1 = random.choice(['f', 'b'])
    computer2 = random.choice(['f', 'b'])
    computer3 = random.choice(['f', 'b'])
    
    if is_win(user, computer1, computer2, computer3):
        return 'Congrate you win!'
    
    #return 'All'
    else:
        print ("Times for rock paper scissors")
        print(play())
    
        
    
def is_win(player, com1, com2, com3):
    if player != com1 and player != com2 and player != com3:
        return True

def is_a_tie(player, com1, com2, com3):
    if player != com1
    
    
print(playing())