#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open("Input/Names/invited_names.txt") as names_file:
    for name in names_file.readlines():
        names.append(name.strip())

with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()

for name in names:
    final_letter = starting_letter.replace("[name]",name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as final_letter_file:
        final_letter_file.write(final_letter)