# Program to display the Fibonacci sequence up to nth term

nterms = int(input("Enter the number of terms : "))

# first two terms
count = 0
n1 = 0
n2 = 1

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")

# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
