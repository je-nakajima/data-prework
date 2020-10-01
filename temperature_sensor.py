
temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]

min_temp = min(temperatures_C)
max_temp = max(temperatures_C)
hot_temps = []
for temp in temperatures_C:
    if temp >= 70:
        hot_temps.append(temp)

avg_temp = sum(temperatures_C) / len(temperatures_C)

#sensor failure at 3am - change the temp at 3am to average temp
temperatures_C = [x if x != 0 else int(avg_temp) for x in temperatures_C]
print(temperatures_C)


print('Min temp is',min_temp)
print('max temp is',max_temp)
print('Temperatures above 70 are',hot_temps)
print('Average temp is',avg_temp)

def c_to_f(temp):
    f = 1.8 * temp + 32
    return f

#convert temperatures from C to F
temperatures_F = [c_to_f(x) for x in temperatures_C]
print('Temperatures in Fahrenheit are',temperatures_F)


#decision making
if len(hot_temps) > 4 or avg_temp > 65 or [True if x > 80 else False for x in temperatures_C]:
    print('Replace the cooling system')
else:
    print('Do not replace the cooling system')
