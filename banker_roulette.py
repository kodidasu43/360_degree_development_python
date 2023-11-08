#Banker Roulette

import random

names_string=input("Enter names of all the persons in your group, followed by comma and space.\n")
names=names_string.split(',')
#print(names)

names_length=len(names)
print(names_length)

name_index=random.randint(0,names_length-1)
print(name_index)

name_for_billpay=names[name_index]
print(name_for_billpay)

print("{} is going to buy the meal today!".format(name_for_billpay))

