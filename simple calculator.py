#first = input('First value: ')
#second = input('Second value: ')
#sum = float(first) + float(second)
#print('Total ' + str(sum))
#happy = 'hi'
#print(happy.replace('hi', input()))

weight = float(input("Weight: "))

input_of = input("(K)g or (L)bs: ")

if input_of.lower() == "k":
    print("Weight in " + str(weight) + " " + input_of.upper() + "g")

elif input_of.lower() == "l":
    print("Weight in " + str(weight) + " " + input_of.upper() + "bs")
    25
else:
    print("ERROR")



