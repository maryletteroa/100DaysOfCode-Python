print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2

true = names.lower().count("t") +\
  names.lower().count("r") +\
  names.lower().count("u") +\
  names.lower().count("e")

love =  names.lower().count("l") +\
  names.lower().count("o") +\
  names.lower().count("v") +\
  names.lower().count("e")

score_msg = f"{true}{love}"

score = int(score_msg)

if score <10 or score > 90:
  print(f"Your score is {score_msg}, you go together like coke and mentos.")
elif score >=40 and score <=50:
  print(f"Your score is {score_msg}, you are alright together.")
else:
  print(f"Your score is {score_msg}.")

