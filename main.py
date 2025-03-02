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
        name_list:list = [letter.upper() for letter in name]
        # converted_name = [v for k,v in self.nato_dict.items() if [letter for letter in name_list if k == letter]]
        converted_name = [v for k,v in self.nato_dict.items()if k in name_list]
        return converted_name

if __name__ == "__main__":
    nato = NATO()
    name = 'Angela'
    print(nato.convert_to_nato(name=name))