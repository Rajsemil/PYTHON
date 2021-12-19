f = open('semil.txt', mode='r')
data = f.readlines()
for i in data:
    print(i, end="")
f.close()