#Create a list 'k' having seven characters from 'a' to 'g'. Perform the following tasks and print the outputs in separate lines.

#Print alternative characters, using slicing option, starting from 'a'.
#Print alternative characters among the first 4 elements alone
#Print only the odd indexed elements of list 'k'

k=list('abcdefg')
print(k[::2])
print(k[0:4:2])
print(k[1::2])
