"""
Accessor Method
get method
      def get_variable(self):
      def get_result(self):
      def get_name(self):
      def get_id(self):
"""
class Laptop:

    def __init__(self):
        self.model = "Lattitude E6420"

    def get_model(self):
        return self.model
dell = Laptop()
d = dell.get_model()
print(d)