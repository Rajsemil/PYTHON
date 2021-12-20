class Adpresso:
    def hello(self, name=None):
        if name is not None:
            print("Hello: ",name)
        else:
            print("Hello")
obj = Adpresso()
obj.hello()
