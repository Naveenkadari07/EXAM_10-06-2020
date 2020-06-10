x = int(input("Enter the first value:"))
y = int(input("Enter the secocnd value:"))
for i in range(x,y+1):
    count = 0
    for j in range(1,i+1):
        if i%j==0:
         count=count+1
    if count==2:
        print(i)