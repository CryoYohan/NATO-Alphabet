import pandas as pd

class NATO:
    def __init__(self):
        self.df = self.read_csv()
        self.nato_dict = self.csv_to_dict()

    def read_csv(self):
        self.df = pd.read_csv('nato_phonetic_alphabet.csv')
        return self.df

    def csv_to_dict(self):
        nato_dict = {row.letter:row.code for index,row in self.df.iterrows()}
        return nato_dict

    def convert_to_nato(self, name:str):
        letter_list:list = [letter.upper() for letter in name]
        converted_name = [self.nato_dict[letter] for letter in letter_list]
        return converted_name

if __name__ == "__main__":
    nato = NATO()
    name = input("Enter your name: ")
    print(nato.convert_to_nato(name=name))