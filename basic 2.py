# write a table of 30 in a format 30 x 1 = 30


n=30
for i in range(1,11):
    print(n,"x",i,"=",n*i)
    





# write a table of 2 without using x and format 2 4 6 ......



for i in range(2,21):
    if i%2==0:
       print (i)
       



#print an array by taking input itself


x = [1,2,3,4,5,6,7,8,20,30]
print(x)
    
    
    
 
    











#after printing an array check and return count of element which is divisble by 2

count = 0
for i in range(len(x)):
    if x[i]%2==0:
        count+=1
print(count)
        


# write a code to print array of element in an alternate order make sure len arr >= 10

x =[2,45,77,888,99999,909,111,563,934,12222,13333,123]
for i in range(0,len(x),2): 
    print(x[i])
    
    

# perform an operation only above array to print those elements which is greater than 15
print("v")

for i in range(len(x)):
    if x[i]>=15:
        print(x[i])


# in a same array check how many elements in range between 40 to 200 return count of those element
print("v")

count = 0 
for i in range(len(x)):
    if x[i]>=40 and x[i]<=200:
        count+=1
print(count)




# In a same array check whether a no 200 is there or not if yes then print index else print not presnt

print("v")

      

for i in range(len(x)):
    if x[i]==200:
        print(i)
print("not present")
     



























