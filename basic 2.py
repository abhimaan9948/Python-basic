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
        







