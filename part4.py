'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. Those two number will be the base and height of a triangle. 
The program will then output the area of that triangle. (Reminder: the area of a triangle can be calculated by (base * height)/2 ).

What should appear on the console when this code runs:

Enter the base: 8
Enter the height: 3
The area of the triangle is 12.0

'''

#start writing your code below
number_1 = int(input("Enter the base:"))
number_2 = int(input("Enter the height:"))
area = ((number_1 * number_2)/2)
print("The area of the triangle is", area)
