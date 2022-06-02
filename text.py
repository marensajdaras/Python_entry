# text in python is a sequence of characters 
text = 'Python Programming'
list(text) # this line will split text's(which is variable) value('P...g') into characters tokens and create in the same time a list
Output: ['P', 'y', 't', 'h', 'o', 'n', ' ', 'P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g']
# we can then go forward and get some info about that list
# for example with set and len methods we get the set of unique tokens and nr of characters respectively
set(text)
Output: {'a', 'i', 'o', 'n', 'P', 'm', 't', 'r', 'g', 'y', 'h', ' '}
len(text) 
Output: 18
...  
