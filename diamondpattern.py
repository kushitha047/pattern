***
 Write a program to print a diamond pattern of stars, where the number of rows for the upper half is taken as input from the user.
input:
Enter the number of rows for the upper half: 5
output:
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
***
n = int(input("Enter the number of rows for the upper half: "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
