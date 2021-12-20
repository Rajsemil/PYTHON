# Find the driving eligiblity
age = int(input("Enter your age: "))
if age==18:
    print("You can drive")
elif age < 18:
    print("You are not eligible")
elif age > 18:
    print("You are eligible")
else:
    print("Rest of the code")