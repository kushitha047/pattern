***
Write a program to print an inverted right-angled triangle of stars, where the number of rows is taken as input from the user.
input:
Enter the number of rows: 5
output:
*****
****
***
**
*
***
n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print('*' * i)
