string = input("Please enter a sentence: ")
count = len(string)

flag = True

for i in range(0, count//2):
    if string[i] != string[count - 1 - i]:
        flag = False
        break

if flag == True:
    print("Your string is a palindrome.")
else:
    print("Your string is not a palindrome.")
