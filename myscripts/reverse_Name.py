#Program to reverse the first name and last name, but in the same order.

firstName=input("What is your first name ? ")
lastName=input("What is your last name ? ")
print ("Your First name is : ", firstName)
print ("Your Last name is : ", lastName)
lFirstName=list(firstName)
lLastName=list(lastName)
lFirstName.reverse()
lLastName.reverse()
print ("Your reversed First name is: ", ''.join(str(e) for e in lFirstName))
print ("Your reversed Last name is: ", ''.join(str(f) for f in lLastName))
print ("Your reversed full name is: ",''.join(str(e) for e in lFirstName)+" "+''.join(str(e) for e in lLastName))
