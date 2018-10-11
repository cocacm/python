
# Hello! These are all the (potential) exercises for the Python workshop.
#To test any code, uncomment between the ~ lines and run.
#Make sure to comment out the code lines when you want to test another section
#so the exercies don't overlap or conflit.  

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#ice breaker exercise
# def hello(name):
#   print("Hello my name is " + name)


# hello('paul')
# 

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def perimeter(length, width, color="red"):
#   perim = (length*2)+(width*2)
#   print("The perimeter of the rectangle is " +  str(perim))
#   print("It's color is " + color + "!")
#   if length == width:
#     print("This rectangle is a square!")

# perimeter(4,4)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# def odd_even(num):
#   if (num % 2) == 1:
#     print(str(num) + " is an odd number!")
#   elif (num % 2) == 0:
#     print(str(num) + " is an even number!")
#   else:
#     print("how did you get here..?")

# odd_even(19)

# Madlib string game!
# ask for user input and generate a story

# verb = input("Give me a verb ending with ed!")
# noun = input("Give me a noun you'd find underwater!")
# nouns = input("Give me a ploural noun!")

# print("There once was a boy who was really into " + nouns
# + ". He also really liked the " + noun + " version, so much so that he "
# + verb + " it! All the way to the moon.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#Create tip calculator 

#Ask for the bill amount and desired tip (e.g., 15). Print out the final value. 

# bill = float(input("How much is the bill?"))

# tip = float(input("what percent for tip?"))
# tipp = bill*tip

# print("Bill is $" + str(bill) 
# + " plus $" + str(tipp) 
# + " comes out to $" + str(float(bill)+float(tipp)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#If-else Statement 

#Take in 2 numbers for the user
#Figure out which number is bigger
#Output the bigger number?

# num1 = int(input("Input a number"))
# num2 = int(input("Input a number"))

# if num1 > num2:
#   print(num1)
# elif num2 > num1:
#   print(num2)
# else:
#   print("the numbers are the same")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Ask the User to submit a password. Notify the user that the password is invalid if it is shorter than 8 characters and does not contain a numeral (e.g.,1,2,3)


# password = input("enter a password 8 digits long, and contains a number.")
# while len(password) < 8 or str.isalpha(password):
#   print("invalid password")
#   password = input("enter a password 8 digits long, and contains a number.")
# print("password saved as " + password)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# For in range loops. Repeating things!

# for i in range(3):
#   print(i)
#   print("hello")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# While loops
# count = 10
# while count >= 0:
#   print(count)
#   count = count-1
#   if count == 5:
#     break;
  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Complex while loop
# Keep a running sum of numbers prompted to the user.

# num = input("Enter a number. Press enter to find sum:")
# count = 0;

# while str(num) != "":
#   if str(num) == "":
#     break;
#   count += float(num)
#   num =input("Enter a number:")
# print("The total sum is: " + str(count))
#
