import pandas as pd

class NATO:
    def __init__(self):
        self.df = pd.read_csv('nato_phonetic_alphabet.csv')
        self.nato_dict = {row.letter:row.code for index,row in self.df.iterrows()}

    def convert_to_nato(self, name:str):
        letter_list:list = [letter.upper() for letter in name]
        try:
            converted_name = [self.nato_dict[letter] for letter in letter_list]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            return converted_name

if __name__ == "__main__":
    nato = NATO()
    while True:
        name = input("Enter your name: ")
        output = nato.convert_to_nato(name=name)
        if not output is None:
            print(output)
            break
