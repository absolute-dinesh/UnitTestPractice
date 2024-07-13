class Operations:

    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def summation(self):
        return self.num1 + self.num2
    
    def multiplcation(self):
        return self.num1*self.num2

    def increment(self,increment):
        self.value = self.summation() + increment
        return self.value
    