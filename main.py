data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letters = []

for i in data_tuple:
    if type(i) ==str:
         letters.append(i)
         
    else:
        
         numbers.append(i)
numbers.remove(6.13)

numbers.remove(True)
letters.append(True)
letters[0] = ('T')
letters[1] = ('E')
letters[2] = ('X')
letters[3] = ('N')
letters[4] = ('O')
letters[5] = ('L')
letters[6] = ('O')
letters[7] = ('G')
letters[8] = ('Y')    
numbers.sort
print(numbers)
print(letters)        