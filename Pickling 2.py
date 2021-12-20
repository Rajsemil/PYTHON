import pickle
lst = ['a','b','c','d','f']
with open('file.txt','rb') as f:
    emp = pickle.load(f)
    print(emp)