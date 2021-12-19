# All of the one day
tm = float(input("ENTER A TIME: "))
if tm <= 06.00:
    print("GOOD EVEBING SIR")
elif tm<=12:
    print("GOOD MORNING SIR")
elif tm<=18:
    print("GOOD AFTER NOON")
elif tm<=20:
    print("HAVE A NICE DAY SIR")
elif tm<=24:
    print("GOOD NIGHT SIR")
else:
    print("WISH YOUB GOOD LUCK SIR")