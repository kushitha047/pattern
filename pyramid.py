***
 Write a program to print a pyramid of stars, where the number of rows is taken as input from the user.
input:
Enter the number of rows: 5
output:
    *
   ***
  *****
 *******
*********
***
n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
