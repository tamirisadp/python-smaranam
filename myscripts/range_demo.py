#Write a script to generate the following list of numbers using range
#Generate the list 'k1' having five continuous numbers starting from 0.
#Print 'k1'
#Generate the list 'k2' having five continuous numbers starting from 10.
#Print 'k2'
#Generate the list 'k3' having even numbers between 10 and 20 (including both of them too).
#Print 'k3'
#Generate the list 'k4' having numbers from 100 to 1 in decreasing order, which are also multiple of 25.
#Print 'k4'

k1=range(5)
print(list(k1))
k2=range(10,15)#range(start, stop)
print(list(k2))
k3=range(10,20,2)#range(start,stop,step)
print(list(k3))
k4=range(100,1,-25)
print(list(k4))
