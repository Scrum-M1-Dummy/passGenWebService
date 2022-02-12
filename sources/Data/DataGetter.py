import os

dataPath = os.path.dirname(__file__) + "/database/"


class DataGetter:
    @classmethod
    def get_words_from_file(cls, fileName):
        """
        @param fileName: string
            the name of the file in the folder indicated by dataPath
        @return: list
            a list of words
        """
        with open(dataPath + fileName) as french_words:
            return french_words.read().splitlines()

    @classmethod
    def get_french_words(cls):
        """
        @return: list
            return a list of french words
        """
        return cls.get_words_from_file("french_words.txt")



if __name__ == "__main__":
    print(DataGetter.get_french_words())
