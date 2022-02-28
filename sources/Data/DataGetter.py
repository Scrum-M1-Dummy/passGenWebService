import os
import re

dataPath = os.path.dirname(__file__) + "/database/"


class DataGetter:
    @classmethod
    def get_words_from_file(cls, fileName, seplines=False):
        """
        @param fileName: string
            the name of the file in the folder indicated by dataPath
        @return: list
            a list of words
        """
        with open(dataPath + fileName) as file:
            if seplines:
                words = []
                content = file.read()
                reg_groups = re.compile(r"([\w\d\',]*).", flags=re.MULTILINE)
                findings = reg_groups.findall(content)
                for i in range(len(findings)):
                    findings[i] = findings[i].replace(",", "").replace("et", '').replace("ou", "")
                return findings

            else:
                return file.read().splitlines()

    @classmethod
    def get_french_words(cls):
        """
        @return: list
            return a list of french words
        """
        return cls.get_words_from_file("french_words.txt")

    @classmethod
    def get_apple_text_words(cls):
        return cls.get_words_from_file("appleTexte.txt", seplines=True)


if __name__ == "__main__":
    print(DataGetter.get_apple_text_words())
