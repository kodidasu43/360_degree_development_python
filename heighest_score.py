#Highest score in class

student_scores=input("Enter Scores of students, seperated by space\n") #Asking user for input
student_scores=student_scores.split() # covereting the string to list

student_scores_numbers = [int(string) for string in student_scores] # converting strings to integer

max_score=0

for score in student_scores_numbers: # looping over list to get the max value
    if score > max_score:
        max_score=score
        #print(max_score)

print(f"The highest score in the class is: {max_score}")
    