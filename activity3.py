tuple1 = (0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0)
sunny = 0
rainy = 0
for i in range(0, 13):
    if(tuple1[i] == 0):
        rainy += 1
    else:
        sunny += 1
if(sunny > rainy):
    print("Good weather!")
else:
    print("Bad weather.")