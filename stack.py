class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        return self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return not self.items
    def __str__(self):
        return str(self.items)


# This if statement means that, when we have to import the Stack class in another file then the code other than the Stack class
# will also be imported but if you use the following snippent then only the Stack class will be imported.

if __name__ == "__main__":
    a = Stack()
    a.push(2)
    print(a.__str__())
    
