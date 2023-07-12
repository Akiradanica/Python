import datetime
today =datetime.date.today()
year = today.year

#age = 20
#is_new = True

#print(patient_name)
#print(age)

first_name = input("First Name: ")
last_name = input("Last Name: ")
age = input("age: ")
status = input("Are you old or new patient?: ")

patient_name = first_name + " " + last_name
birth_year = int(year) - int(age)
print("You are " + patient_name)
print("Your age is " + str(age) + ", you are born on " + str(birth_year))

if status == "old" and "OLD":
    print("I am an Old Patient")
else:
    print("New patient here!!!")