n = int(input("Enter fibonacci number:"))
x = 0
y = 1
for i in range(2,n+1):
    z = x + y
    x = y
    y = z
    print(z)