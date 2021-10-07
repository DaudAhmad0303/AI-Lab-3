class my_queue:
    '''
    This class works same as the Queue Data Structure does.
    '''
    def __init__(self):
        self.__lst = []

    def is_empty(self):
        if len(self.__lst) == 0:
            return True

    def size_of_queue(self):
        return len(self.__lst)
        
    def enqueue(self, val):
        self.__lst.append(val)

    def dequeue(self):
        if self.size_of_queue() != 0:
            val = self.__lst[0]
            self.__lst.pop(0)
            return val
        else:
            return None

    def print_queue(self):
        print(self.__lst)
        

#--------------------Driver Program-------------------------
q1 = my_queue()
print('Current size of Queue: ',q1.size_of_queue())
q1.enqueue('Aqib')
q1.enqueue('Zain')
q1.enqueue('Ali')
q1.print_queue()
print('Current size of Queue: ',q1.size_of_queue())
print('De-Queued: ', q1.dequeue())
print('De-Queued: ', q1.dequeue())
print('Current size of Queue: ',q1.size_of_queue())
print('De-Queued: ', q1.dequeue())
print('Current size of Queue: ',q1.size_of_queue())
print(q1.__lst)