from cmath import log
import string
import secrets
import random

from sources.keys import *
from sources.Data.DataGetter import DataGetter
from sources.PassGen.Models.PhraseExpert import PhraseExpert


class PassGen:
    @classmethod
    def get_password_entropy(self, passtest, characterList):
        """
        @param passtest: mot de passe à tester
        @param characterList: liste des caractères possible dans le choix du mot de passe
        @return: l'entropie du mot de passe
        """
        L = len(passtest)
        R = len(characterList)
        E = L * log(R) / log(2)
        return E

    @classmethod
    def get_alphabet_character_choice(cls, character_list, character_selection_method="ban"):
        """
        @param character_list: string of the characters to include / exclude
        @param character_selection_method: string
            "only" : use only characters in the list
            "ban" : remove characters from the list
            "must" : characters from the list are needed
        @return: string
            list of the characters to USE for the password
          """

        restricted_alphabet = ""
        whole_alphabet = string.digits + string.ascii_letters
        if character_selection_method == METHOD_BAN:  # ban characters from the list in the alphabet
            for i in whole_alphabet:
                sublist = ""
                for j in character_list:
                    if j == "\\d":
                        sublist += string.digits
                    elif j == "\\c":
                        sublist += string.ascii_lowercase
                    elif j == "\\C":
                        sublist += string.ascii_lowercase
                    elif j == "\\s":
                        sublist += ''.join(
                            ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                             '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'])
                    elif j == "\\[dev]":
                        sublist += " les devs vous disent bonjour "
                    else:
                        sublist += j
                if i not in sublist:
                    restricted_alphabet += i
        elif character_selection_method == METHOD_ONLY:  # use only characters from the list in the alphabet
            for i in character_list:
                if i == "\\d":
                    restricted_alphabet += string.digits
                elif i == "\\c":
                    restricted_alphabet += string.ascii_lowercase
                elif i == "\\C":
                    restricted_alphabet += string.ascii_lowercase
                elif i == "\\s":
                    restricted_alphabet += ''.join(
                        ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                         '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'])
                elif i == "\\[dev]":
                    restricted_alphabet += " les devs vous disent bonjour "
                else:
                    restricted_alphabet += i
        else:  # if method other than ban and only return the whole alphabet
            return whole_alphabet
        restricted_alphabet_no_duplicates = ""
        for i in restricted_alphabet:
            if i not in restricted_alphabet_no_duplicates:
                restricted_alphabet_no_duplicates += i
        return restricted_alphabet_no_duplicates

    @classmethod
    def get_alphabet_french_words(cls):
        """
        @return: list
            return a list of french words
        """
        return DataGetter.get_french_words()

    @classmethod
    def get_password_words(cls, length, word_delimitor="-", desired_entropy=0):
        """
        @param length: int
            the number of words to put in the password
        @return: string
            a password composed of words separated by the word_delimitor
        """
        alphabet = DataGetter.get_french_words()

        password = ""
        entropy = 0

        timer = 0
        while (entropy := PassGen.get_password_entropy(password, alphabet).real) <= desired_entropy:
            print("nono")
            password = word_delimitor.join(secrets.choice(alphabet) for _ in range(length))
            if (timer := timer + 1) > 360:
                entropy = PassGen.get_password_entropy(password, alphabet).real
                return "entropie impossible", entropy

        return password, entropy

    @classmethod
    def get_password_sentence(cls, length, lang, word_delimitor="", desired_entropy=0):
        """
        @param length: int
            the number of words to put in the password
        @return: string
            a password composed of words separated by the word_delimitor
        """
        if lang == "fre":
            pe = PhraseExpert(DataGetter.get_apple_text_words)
            alphabet = DataGetter.get_french_words()
        elif lang == "eng":
            pe = PhraseExpert(DataGetter.get_ang_sentences)
            alphabet = DataGetter.get_ang_sentences()

        password = ""
        entropy = -1
        timer = 0
        while (entropy := PassGen.get_password_entropy(password, alphabet).real) <= desired_entropy:
            password = pe.gen_phrase(length, word_delimitor)
            if (timer := timer + 1) > 360:
                entropy = PassGen.get_password_entropy(password, alphabet).real
                return "entropie impossible", entropy

        return password, entropy

    @classmethod
    def get_password_character_choice(cls, length, character_list, desired_entropy, character_selection_method="ban"):
        """
        @param length: int
            the length of the password
        @param character_list: string of the characters to include / exclude
        @param character_selection_method:  string
            "only" : use only characters in the list
            "ban" : remove characters from the list
            "must" : characters from the list are needed
        @return: string
            a password with the requirements specified
        """
        print(character_list)
        timer = 0
        # character_list = list(dict.fromkeys(character_list))
        print(character_selection_method)
        alphabet = PassGen.get_alphabet_character_choice(character_list,
                                                         character_selection_method)  # get the alphabet depending of the method
        password = ""
        entropy = 0
        while ((entropy := PassGen.get_password_entropy(password,
                                                        alphabet).real) < desired_entropy) or password == "":  # if password entropy lower than allowed entropy
            print("pass", password)
            print("genEntropy in while:", entropy)
            if character_selection_method == METHOD_MUST:  # if characters to include
                mdp = ''.join(secrets.choice(alphabet) for _ in range(length - len(character_list)))  # create a pass
                for i in range(len(character_list)):  # add characters that must be included
                    r = random.randint(0, len(mdp))
                    char = ""
                    if character_list[i] == "\\d":
                        char = random.choice(string.digits)
                    elif character_list[i] == "\\c":
                        char = random.choice(string.ascii_lowercase)
                    elif character_list[i] == "\\C":
                        char = random.choice(string.ascii_lowercase)
                    elif character_list[i] == "\\s":
                        char = random.choice(
                            ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<',
                             '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'])
                    elif character_list[i] == "\\[dev]":
                        char = " les devs vous disent bonjour "
                    else:
                        char = character_list[i]
                    print(char)
                    mdp = mdp[:r] + char + mdp[r:]
                password = mdp
            else:
                password = ''.join(secrets.choice(alphabet) for _ in range(length))
            timer = timer + 1
            if timer == 360:
                return "entropie impossible", entropy
        print("genEntropy:", entropy)
        print(entropy < desired_entropy)
        return password, entropy


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=6, character_list="abcdaaabe", desired_entropy=1,
                                                character_selection_method="must"))
