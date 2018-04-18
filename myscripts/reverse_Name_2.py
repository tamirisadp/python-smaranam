#Super Easy way to reverse the names

name=input("What is your name ? ")
first,last=name.split()
print("Your Reversed Name is: ",first[::-1],last[::-1])
