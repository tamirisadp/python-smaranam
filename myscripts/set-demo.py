#Question
#Create two sets 'a', and 'b' with following values.
#a = ('10','20','30','40')
#b = ('30','60')

#Determine the following
#Union; store the output in variable 'u' and print it.
#Intersection; store the output in variable 'i' and print it.
#Difference between set 'a' and 'b'; store the output in variable 'd' and print it.
#Symmetric difference; store the output in variable 'sd' and print it.'

a = set(('10','20','30','40'))
b = set(('30','60'))
u = a|b
print(u)
i= a&b
print(i)
d=a-b
print(d)
sd=a^b #new set with elements in either s or t but not both
print(sd)
