import pickle
empID = {'1',"Zack",'2',"Smith",'3',"Sameer"}
pickle_on = open('empID.txt','wb')
pickle.dump(empID,pickle_on)
pickle_on.close()
print("Your pickle is done")