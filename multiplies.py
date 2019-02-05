def print_factors(x):
    

   print("The factors of",x,"are:")
   for i in range(1, x):
       if x % i == 0:
           print(i)

 
 

 
num = int(input("Enter a number: "))

print_factors(num) 
