#Consider the string 's' having the value 'tata consultancy services limited'
#Determine the no. of vowels present in it, using While loop. Store the number in variable 'count' and print it.

s="tata consultancy services limited"
count=0
s_list=list(s)
while s_list:
    if s_list.pop() in "aeiouAEIOU":
        count+=1

print(count)
