# Python program to print positive Numbers in a List2

 

# list of numbers

list2 = [12, 14, -95, 3]

num = 0

 

# using while loop     

while(num < len(list2)):

     

    # checking condition

    if list2[num] >= 0:

        print(list2[num], end = " ")

     

    # increment num 

    num += 1
