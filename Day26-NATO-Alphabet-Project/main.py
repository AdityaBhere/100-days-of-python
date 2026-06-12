import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    user_input = input("Enter word to spell:")
    try:
        phonetic_list = [data_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()