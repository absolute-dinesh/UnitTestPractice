from operations import Operations

class Usage:

    def __init__(self,n1,n2) :
        self.operations_class = Operations(num1=n1,num2=n2)
        print("Initiated the operations class")

    def increment(self,value1,value2):
        return self.operations_class.increment(value1+value2)


if __name__ == '__main__':
    obj1 = Usage(1,2)
    print(f'Incrementing with 3+4 : {obj1.increment(3,4)}')
    print(f"Objects in Obj and incrementing with 5 in the internal method {obj1.operations_class.num1,obj1.operations_class.num2} and incremented value {obj1.operations_class.increment(5)} ")
    obj2 = Operations(3,4)
    print(obj2.division())