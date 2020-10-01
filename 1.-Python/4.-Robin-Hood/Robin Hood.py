from math import sqrt, pow

points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),
          (-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]

#find where arrow hits another arrow (duplicates)
shots = len(points)

remove_duplicates = set(points)
duplicates = len(points) - len(remove_duplicates)
print('Arrows that hit another arrow =',duplicates)

#shots in each quadrant
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for point in points:
    if point[0] > 0 and point[1] > 0:
        q1 = q1 + 1
    elif point[0] < 0 and point[1] > 0:
        q2 = q2 + 1
    elif point[0] < 0 and point[1] < 0:
        q3 = q3 + 1
    elif point[0] > 0 and point[1] < 0:
        q4 = q4 + 1
        
print('Q1 =',q1)
print('Q2 =',q2)
print('Q3 =',q3)
print('Q4 =',q4)

#Euclidean distance

def euc_dist(point):
    distance = sqrt(pow((0 - point[0]),2)+ pow((0 - point[1]),2))
    #print('Euclidean distance is',distance)
    return distance

distances = []
for point in points:
    distances.append(euc_dist(point))
#print(distances)
print('Smallest distance to center is',min(distances))
print('Number of arrows with same smallest distances', distances.count(min(distances)))


#won't hit the target
count = 0
for point in points:
    if euc_dist(point) > 9:
        count = count + 1
        
print("Number of arrows that won't hit the target if radius is 9 is ",count)





