class my_stack:
    '''
    This class works same as the Stack Data Structure does.
    '''
    lst = []
    def __init__(self):
        self.lst = []
    
    def top(self):
        return self.lst[-1]

    def is_empty(self):
        if len(self.lst) == 0:
            return True
        
    def push(self,val):
        self.lst.append(val)

    def pop(self):
        val = self.top()
        self.lst.pop()
        return val
    def print_stack(self):
        print(self.lst)
    
    def size_of_stack(self):
        return len(self.lst)

#--------------------Driver Program-------------------------
s1 = my_stack()
s1.push(56)
s1.push(45)
s1.push(34)
s1.print_stack()
print('Top: ',s1.top())
print('Pop: ',s1.pop())
s1.print_stack()
s1.push(100)
s1.push(80)
print(s1.size_of_stack())
s1.print_stack()