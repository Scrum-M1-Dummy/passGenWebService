from cmath import log
import string
import secrets
import random

from sources.keys import *
from sources.Data.DataGetter import DataGetter
from sources.PassGen.Models.PhraseExpert import PhraseExpert


class PassGen:
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
        # TODO : handle the "must" value for character_selection_method aka ban
        restricted_alphabet = ""
        whole_alphabet = string.digits + string.ascii_letters
        if character_selection_method == METHOD_BAN:
            for i in whole_alphabet:
                if i not in character_list:
                    restricted_alphabet += i
        elif character_selection_method == METHOD_ONLY:
            restricted_alphabet = character_list
        else:
            return whole_alphabet
        return restricted_alphabet

    @classmethod
    def get_alphabet_french_words(cls):
        """
        @return: list
            return a list of french words
        """
        return DataGetter.get_french_words()

    @classmethod
    def get_password_words(cls, length):
        """
        @param length: int
            the number of words to put in the password
        @return: string
            a password composed of words separated by "-"
        """
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for _ in range(length))


    @classmethod
    def get_password_sentence(cls, length):
        """
        @param length: int
            the number of words to put in the password
        @return: string
            a password composed of words separated by "-"
        """
        pe = PhraseExpert(DataGetter.get_apple_text_words())
        return pe.gen_phrase(length)

    @classmethod
    def get_password_entropy(self,passtest,characterList):
        L = len(passtest)
        R = len(characterList)
        E = L * log(R)/log(2)
        return E

    @classmethod
    def get_password_character_choice(cls, length, character_list, desired_entropy,character_selection_method="ban"):
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

        # character_list = list(dict.fromkeys(character_list))
        print(character_selection_method)
        alphabet = PassGen.get_alphabet_character_choice(character_list, character_selection_method)
        password=""
        while(PassGen.get_password_entropy(password,alphabet).real < desired_entropy) or password == "":
            if character_selection_method == METHOD_INCLUDE:
                mdp=''.join(secrets.choice(alphabet) for _ in range(length-len(character_list)))
                for i in range(len(character_list)):
                    r=random.randint(0,len(mdp))
                    mdp=mdp[:r]+character_list[i]+mdp[r:]
                password=mdp
            else:
                password=''.join(secrets.choice(alphabet) for _ in range(length))
        return password


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=6, character_list="abcdaaabe",desired_entropy=1, character_selection_method="include"))
