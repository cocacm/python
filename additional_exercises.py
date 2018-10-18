# Written by Paul Gotcher for the Association of Computing Machinery's COC chapter

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Fizz Buzz FizzBuzz
# check if a number is even or odd

def odd_even(num):
  if (num % 2) == 1:
    print(str(num) + " is an odd number!")
  elif (num % 2) == 0:
    print(str(num) + " is an even number!")
  else:
    print("how did you get here..?")

odd_even(19)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Madlib string game!
# ask for user input and generate a story

verb = input("Give me a verb ending with ed!")
noun = input("Give me a noun you'd find underwater!")
nouns = input("Give me a ploural noun!")

print("There once was a boy who was really into " + nouns
+ ". He also really liked the " + noun + " version, so much so that he "
+ verb + " it! All the way to the moon.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Tip Calculator
# ask for the bill amount and desired tip (e.g., 15). Print out the final value.

bill = float(input("How much is the bill?"))

tip = float(input("what percent for tip?"))
tipp = bill*tip

print("Bill is $" + str(bill)
+ " plus $" + str(tipp)
+ " comes out to $" + str(float(bill)+float(tipp)))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# If-else Statement
# Take in 2 numbers from the user, output the larger number

num1 = int(input("Input a number"))
num2 = int(input("Input a number"))

if num1 > num2:
  print(num1)
elif num2 > num1:
  print(num2)
else:
  print("the numbers are the same")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Password Checker
# Ask the User to submit a password. Notify the user
# that the password is invalid if it is shorter than 8
# characters and does not contain a numeral (e.g.,1,2,3).

password = input("enter a password 8 digits long, and contains a number.")
while len(password) < 8 or str.isalpha(password):
  print("invalid password")
  password = input("enter a password 8 digits long, and contains a number.")
print("password saved as " + password)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Are you okay?
# Use for in range to print hello 3 times

for i in range(3):
  print(i)
  print("hello")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Countdown
# Use a while loop to count down from 10 to 5

While loops
count = 10
while count >= 0:
  print(count)
  count = count-1
  if count == 5:
    break;

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Complex while loop
# Keep a running sum of numbers prompted to the user.

# num = input("Enter a number. Press enter to find sum:")
# count = 0;

while str(num) != "":
  if str(num) == "":
    break;
  count += float(num)
  num =input("Enter a number:")
print("The total sum is: " + str(count))
