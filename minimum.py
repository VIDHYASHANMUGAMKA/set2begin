a = [] 
num = int(input("Enter number of elements in list: ")) 
  
 
for i in range(1, num + 1): 
    ele = int(input("Enter elements: ")) 
    a.append(ele) 
      
  
print("Smallest element is:", min(a))   
