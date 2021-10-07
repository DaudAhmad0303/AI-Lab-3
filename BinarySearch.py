def my_binarySearch(lst, val):
    '''
    Binary Search in Python 
    
    Takes the list of numbers and the value to find out.
    '''
    init = 0
    fin = len(lst) - 1
    while init <= fin:
        m = init + (fin - init) // 2
        if lst[m] == val:
            return m
        elif lst[m] < val:
            init = m + 1
        else:
            fin = m - 1
    return -1

#--------------------Driver Program-------------------------
lst = [6, 12, 17, 23, 38, 45, 77, 84, 90] # len = 9
val = int(input('Enter value to find: '))

result = my_binarySearch(lst, val)

if result != -1:
    print(f'{val} is present at index {result}...')
else:
    print(f'{val} is not present in list...')