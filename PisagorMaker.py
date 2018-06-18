your_number = input("Please insert your number for triangle: ")
if your_number % 2 == 0:
    y = ((your_number ** 2)/4) - 1
    if your_number < y :
        print(str(your_number) + " " + str(int(y)) + " " + str(int(y + 2)))
else:
    y = ((your_number ** 2) - 1)/2
    if y > your_number :
        print(str(int(your_number)) + " " +str(int(y)) + " " +str(int(y + 1)))
