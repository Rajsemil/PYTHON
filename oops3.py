class Mobile:
    def __init__(sel, model):
        self.model = model

    def show_model(self):
        print("Model: ",self.model)

realme = Mobile(input("Enter Your Model Name: "))
realme.show_model()