import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

user_word = input("Enter a word: ").upper()
nato_phonetic_list = [nato_alphabet_dict[letter] for letter in user_word]

print(nato_phonetic_list)
