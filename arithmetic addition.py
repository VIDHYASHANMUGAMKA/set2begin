a = int(input("Please Enter First Number   : "))
n = int(input("Please Enter the Total Numbers   : "))
d = int(input("Please Enter the Common Difference : "))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)  
