import pickle

car_list = ["Honda", "Toyota", "Kia", "Mercedes", "Ford", "BMW"]
car_pickle = open ("file.txt", "wb")
pickle.dump(car_list, car_pickle)