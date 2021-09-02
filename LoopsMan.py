a = 1
sum = 0
n = int(input("How many numbers do you want to enter?"))
while a <= n:
    num = int(input("Enter a number"))
    sum = sum + num
    a = a + 1

print ("Your sum is: %s" % (sum))