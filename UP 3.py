import pickle
with open("data.pickle","rb") as f:
    obj = pickle.loads(f)
    print(obj)