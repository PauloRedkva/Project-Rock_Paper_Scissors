"""[Interactive Coding Exercise] Banker Roulette - Who will pay the bill?"""

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
num_items = len(names)
random_choice = random.randint(0, num_items -1)
payBill = names[random_choice]

# utilizando apenas método random_choice
#payBill = random.choice(names)

print(f"{payBill} is going to buy the meal today!")





















"""
## Who's Paying

# UPDATE
We've moved away from repl.it for coding exercises.
Check out the new exercises on Coding Rooms with automated submissions.

Login to your Udemy course and head over to the link below to get the sign up link:

[Click here](https://www.udemy.com/course/100-days-of-code/learn/lecture/17825914#questions)

# Instructions

You are going to write a program which will select a random name from a list of names. The person selected will have to pay for everybody's food bill. 

**Important**: You are not allowed to use the `choice()` function.

**Line 8** splits the string `names_string` into individual names and puts them inside a **List** called `names`. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input

```
Angela, Ben, Jenny, Michael, Chloe
```
Note: notice that there is a space between the comma and the next name. 
# Example Output

```
Michael is going to buy the meal today!
```


# Hint

1. You might need the help of the `len()` function.   

[https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list](https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list)

2. Remember that Lists start at index 0!

# Solution

[https://repl.it/@appbrewery/day-4-2-solution](https://repl.it/@appbrewery/day-4-2-solution)
"""