#dictionaries demo

my_dictionary={"Sai":"30","Kishore":"31"} 
print(type(my_dictionary))
print(my_dictionary["Sai"])
my_dictionary["David"]="40"
print(my_dictionary.keys())
my_dictionary["Sai"]="32"
print(my_dictionary.values())
#del my_dictionary
#print(my_dictionary)

for name in my_dictionary:
	print(name)
    
for name in my_dictionary.items():
	print(name)
    
for name in my_dictionary:
    print(my_dictionary[name])
    
my_dictionary.clear()

print(my_dictionary)

