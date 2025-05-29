import array
arr=array.array('I')
duparray=array.array('I')
number=int(input("Enter the number of numbers you want to add :"))

for i in range (0, number):
     x=int(input("Enter the elements of array:"))
     arr.append(x)
     
for j in range (0, number):
     x=int(input("Enter the elements that you entered in array 1:"))
     arr.append(x)


arr=array.array('I',sorted(arr))
for j in range (0,number ):
    if arr[i]/ arr[j] !=0:
        duparray.append(arr[i])
        temp=i
        i=j
        j=temp
    else :
        print("The repeated numbers are not listed")
        
        
duparray=array.array('I',sorted(duparray))   
print(*duparray)    
        
        
    
    
    