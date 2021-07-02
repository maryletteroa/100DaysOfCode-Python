import pandas as pd

word = input("Enter a word: ").upper()

df = pd.read_csv("./nato_phonetic_alphabet.csv")

nato_alphabet = [row.code for w in word for (index,row) in df.iterrows() if row.letter == w]
print(nato_alphabet)