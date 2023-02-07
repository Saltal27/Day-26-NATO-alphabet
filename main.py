import pandas

nato_phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (index, row) in nato_phonetic_alphabet.iterrows()}

valid_info = True

while valid_info:
    user_word = input("Enter a word: ").upper()
    try:
        nato_phonetic_list = [nato_alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        valid_info = False
        print(nato_phonetic_list)
