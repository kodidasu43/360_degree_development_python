#Average Height

student_heights=input("Enter Heights of studnets, seperated by space\n") #Asking user for input
student_heights=student_heights.split() # covereting the string to list
#print(student_heights)

student_heights_numbers = [int(string) for string in student_heights] # converting strings to integer
#print(student_heights_numbers)

#print(sum(student_heights_numbers))

total_height=0
for student_height in student_heights_numbers: # Looping over each element to get the total sum
   total_height +=student_height # total_height=total_height+student_height
   
print(f"total height = {total_height}")

#print(len(student_heights_numbers))
number_of_students=0
for student in student_heights_numbers: #looping over eacxh element to get the no of elemeent in list
    number_of_students+=1
    
print(f"number of students = {number_of_students}")

average_height = round(total_height/number_of_students)

print(f"average height = {average_height}")





