from random import choice

gestures = ['rock','paper','scissors']

n_rounds = 1
rounds_to_win = 3
cpu_score = 0
player_score = 0

def random_choice():
    return choice(gestures)


def player_c():
    player_choice = None
    while player_choice not in gestures:
        player_choice = input("Choose rock! paper! or scissors! >>> ")
    return player_choice

def winner(cpu_c,player_c):
    if cpu_c == player_c:
        return 0
    elif cpu_c == 'rock' and player_c == 'paper':
        return 2
    elif cpu_c == 'rock' and player_c == 'scissors':
        return 1
    elif cpu_c == 'paper' and player_c == 'rock':
        return 1
    elif cpu_c == 'paper' and player_c == 'scissors':
        return 2
    elif cpu_c == 'scissors' and player_c == 'paper':
        return 1
    elif cpu_c == 'scissors' and player_c == 'rock':
        return 2

def show_results(pc,you,score):
    global player_score
    global cpu_score
    print("CPU chose ",pc)
    print("Player chose",you )
    if score == 0:
        print("It's a TIE")
    elif score == 1:
        print("CPU won")
        cpu_score = cpu_score + 1
    elif score == 2:
        print("Player won")
        player_score = player_score + 1


while cpu_score != rounds_to_win and player_score != rounds_to_win and n_rounds <= 5:
    player = player_c()
    cpu = random_choice()
    won = winner(cpu,player)
    show_results(cpu,player,won)
    print("Current player score is ",player_score)
    print("Current cpu score is ",cpu_score)
    n_rounds = n_rounds + 1

if cpu_score > player_score:
    print("CPU WON THE GAME")
elif cpu_score < player_score:
    print("Player WON THE GAME")
else:
    print("NO WINNER")
    
    
    


