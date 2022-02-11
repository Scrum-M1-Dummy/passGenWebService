import os

dataPath = os.path.dirname(__file__) + "/database/"

class DataGetter:
    @classmethod
    def get_french_words(self):
        with open(dataPath + "french_words.txt") as french_words:
            return french_words.read().splitlines()



if __name__ == "__main__":
    print(DataGetter.get_french_words())