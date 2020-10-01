from math import sqrt

stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]

number_of_stops = len(stops)
ocupation_at_stops = []
passengers_present = 0
for i in range(number_of_stops):
    passengers_present = passengers_present + stops[i][0] - stops[i][1]
    ocupation_at_stops.append(passengers_present)
    print('There are ' + str(passengers_present)+ ' passengers at stop '+ str(i+1))

print(ocupation_at_stops)
maximum_occupation = max(ocupation_at_stops)
print('Maximum occupation was',maximum_occupation)

#average occuation
avg_occ = sum(ocupation_at_stops) / len(ocupation_at_stops)
print('Average occupation is',avg_occ)

#standard deviation
mean1 = avg_occ
i = 0
sum2 = 0
while i < len(ocupation_at_stops):
    b = ocupation_at_stops[i] - mean1
    sum2 = sum2 + b*b
    i = i + 1

mean2 = sum2/len(ocupation_at_stops) 
sd = sqrt(mean2)

print('Standard deviation is',sd)
