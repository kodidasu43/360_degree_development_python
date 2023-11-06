#pizza order bill calculation

print("Thank you for choosing Python Pizza Deliveries!")

pizza_size=input('What size pizza you want ? for Small input "S" or or for Medium input "M" or for Large input "L"\n')
add_pepperoni=input('Would you like to add pepperoni ? if yes input "Y" or if no input "N"\n')
add_cheese=input('Would you like to add cheese ? if yes input "Y" or if no input "N"\n')

#logic goes here
#bill=0
if pizza_size == 'S':
    bill=15
elif pizza_size == 'M':
    bill=20
else :
    bill=25
    
if add_pepperoni == 'Y':
    if pizza_size == 'S':
        bill+=2
    else :
        bill+=3
else :
    bill=bill
    
if add_cheese=='Y':
    bill+=1
else :
    bill=bill
    
print("Your final bill is: ${}".format(bill))
