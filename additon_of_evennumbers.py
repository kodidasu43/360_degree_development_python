# addition of even numbers

user_number=int(input("Enter the number till whihc you want the summation of even numbers\n")) # user input

if user_number < 0 or user_number > 1000:
    print("Your number exceeded the range. Please give any number less than 1000") # keeping the constraint on the user input
else :
    # even_number_sum=0
    # for number in range(2,user_number+1,2):
        # even_number_sum+=number
        
    # print(even_number_sum)
    even_number_sum=sum(range(2,user_number+1,2))
    print(even_number_sum)
    