# magic8.py
# This is a Magic 8-Ball program that answers and "Yes" or "No" question with a different fortune

# Import module
import random

# Set up variables
name = input("Your name: ")
ques = input("Your question: ")
ans = ""

# Create random number variable
random_num = random.randint(1,9)

# Generate response to question
if random_num == 1:
  ans = "Yes - definitely."
elif random_num == 2:
  ans =  "It is decidedly so."
elif random_num == 3:
  ans =  "Without a doubt."
elif random_num == 4:
  ans =  "Reply hazy, try again."
elif random_num == 5:
  ans = "Ask again later."
elif random_num == 6:
  ans = "Better not tell you now."
elif random_num == 7:
  ans = "My sources say no."
elif random_num == 8:
  ans = "Outlook not so good."
elif random_num == 9:
  ans = "Very doubtful."
else:
  ans = "Error"

# Check question was asked
if len(ques) == 0:
    print("The Magic 8-Ball cannot provide a fortune unless you ask it something")
# Output on terminal
elif name == "":
  print("You asked: " + ques)
else:
  print(name + " asks: " + ques)
  print("Magic 8-Ball's answer: " + ans)