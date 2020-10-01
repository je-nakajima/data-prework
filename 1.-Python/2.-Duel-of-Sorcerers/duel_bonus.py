from math import sqrt

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

spells = 0
gandalf_wins  = 0
saruman_wins = 0
tie = 0
g_win_streak = 0
s_win_streak = 0

for spells in range(len(gandalf)):
    if POWER[gandalf[spells]] > POWER[saruman[spells]]:
        g_win_streak = g_win_streak + 1
        s_win_streak = 0
        print('Gandalf won this duel')
        if g_win_streak == 3:
            gandalf_wins = gandalf_wins + 1
            print('Gandal won this game')
    elif POWER[gandalf[spells]] < POWER[saruman[spells]]:
        s_win_streak = s_win_streak + 1
        g_win_streak = 0
        print('Saruman won this duel')
        if s_win_streak == 3:
            saruman_wins = saruman_wins + 1
            print('Saruman won this game')           
    else:
        print('Tie in this duel')
        
print('Gandalf won',gandalf_wins)
print('Saruman won',saruman_wins)
print('Number of Ties =',tie)


gandalf_avg = 0
saruman_avg = 0
for spells in range(len(gandalf)):
    gandalf_avg = gandalf_avg + POWER[gandalf[spells]]
    saruman_avg = saruman_avg + POWER[saruman[spells]]

gandalf_avg_sp = gandalf_avg / len(gandalf)
saruman_avg_sp = saruman_avg / len(saruman)   
print('Gandalf spell power average ',gandalf_avg_sp)
print('Saruman spell power average ',saruman_avg_sp)

#calculate standard devation for Gandalf spells
mean1 = gandalf_avg_sp
i = 0
sum2 = 0
while i < len(gandalf):
    b = POWER[gandalf[i]] - mean1
    sum2 = sum2 + b*b
    i = i + 1

mean2 = sum2/len(gandalf) 
sd = sqrt(mean2)

print('Standard deviation for Gandalf is ',sd)

#calculate standard devation for Saruman spells

mean1 = saruman_avg_sp
i = 0
sum2 = 0
while i < len(saruman):
    b = POWER[saruman[i]] - mean1
    sum2 = sum2 + b*b
    i = i + 1

mean2 = sum2/len(saruman) 
sd = sqrt(mean2)

print('Standard deviation for Saruman is',sd)
