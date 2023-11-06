#love calculator

name=input("Enter your Name..!\n")
partner_name=input("Enter your partner Name..!\n")

combine_name=name+partner_name
combine_name=combine_name.lower()

print("The Love Calculator is calculating your score...")

#print(combine_name)
#logic goes here
#calculation for true word letters count
t_count=combine_name.count("t")
r_count=combine_name.count("r")
u_count=combine_name.count("u")
e_count=combine_name.count("e")

true_total_count=t_count+r_count+u_count+e_count

#calculation for love word letters count
l_count=combine_name.count("l")
o_count=combine_name.count("o")
v_count=combine_name.count("v")
e_count_1=combine_name.count("e")

love_total_count=l_count+o_count+v_count+e_count_1

total_love_score=int(str(true_total_count)+str(love_total_count))

if total_love_score < 10 or total_love_score > 90 :
    print("Your score is {}, you go together like coke and mentos.".format(total_love_score))
elif total_love_score >=40 and total_love_score <=50 :
    print("Your score is {}, you are alright together.".format(total_love_score))
else:
    print("Your score is {}".format(total_love_score))

