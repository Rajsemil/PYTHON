import pickle
my_list = [11, 'Python', b'Love Python']
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

print("Pickling completed!")