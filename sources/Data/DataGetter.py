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
        stopwords = []
        try:
            file1 = open(dataPath + fileName + ".stop",'r')
            Lines = file1.readlines()
            for Line in Lines:
                stopwords.append(Line[:-1])
            print(stopwords)
            print("file found")
        except FileNotFoundError:
            print("not found file")
            pass     
        with open(dataPath + fileName) as file:
            if seplines:
                words = []
                content = file.read()
                reg_groups = re.compile(r"([\w\d\'éàè,]*).", flags=re.MULTILINE)
                findings = reg_groups.findall(content)
                for i in range(len(findings)):
                    findings[i] = findings[i].replace(",", "")
                    if findings[i] in stopwords:
                        findings[i] = ""
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
    def get_ang_sentences(cls):
        """
        @return: list
            return a list of english words
        """
        return cls.get_words_from_file("ang_sentences.txt", seplines=True)

    @classmethod
    def get_apple_text_words(cls):
        """
        Return a list of french words
        @return: list
        """
        return cls.get_words_from_file("appleTexte.txt", seplines=True)


if __name__ == "__main__":
    print(DataGetter.get_apple_text_words())
