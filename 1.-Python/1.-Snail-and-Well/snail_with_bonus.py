#BONUS
from math import sqrt

well_height = 125
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
nightly_distance = 20
snail_position = 0
days = 0
displacement = []


while well_height > 0:
    well_height = well_height - advance_cm[days]
    snail_position = well_height
    print(snail_position)
    if snail_position <= 0:
        displacement.append(advance_cm[days])
        days = days + 1
        break
    else:
        well_height = well_height + nightly_distance
        snail_position = well_height
        print(snail_position)

    displacement.append(advance_cm[days]-20)
    days = days + 1

print(displacement)
print('Max displacement was: ',max(displacement))
print('Min displacement was: ',min(displacement))
print('Average progress was: ',sum(displacement)/days)
print('It took '+str(days)+' days')

#calculate standard devation
mean1 = sum(displacement)/len(displacement)
i = 0
sum2 = 0
while i < len(displacement):
    b = displacement[i] - mean1
    sum2 = sum2 + b*b
    i = i + 1

mean2 = sum2/len(displacement) 
sd = sqrt(mean2)

print('Standard deviation is',sd)


