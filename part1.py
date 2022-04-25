'''
______
PART 1
______
The program below currently asks the user to enter input two numbers and then prints the sum. 
Change the code so that it asks the user to enter five numbers and finds then prints the sum 
of those five numbers in the formatted sentence that's already there.

What should appear on the console when the program runs:

Enter a number: 10
Enter a second number: 9
Enter a third number: 8
Enter a fourth number: 7
Enter a fifth number: 6
The sum of the numbers you entered is 40

'''

#code starts here
first_value = int(input("Enter a number: 1 "))
second_value = int(input("Enter a second number: 2 "))
third_value = int(input("Enter a second number: 3 "))
fourth_value = int(input("Enter a second number: 4 "))
fifth_value = int(input("Enter a second number: 5 "))

print("The sum of the numbers you entered is", first_value + second_value + third_value + fourth_value + fifth_value)

