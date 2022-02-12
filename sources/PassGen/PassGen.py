import string
import secrets
from sources.Data.DataGetter import DataGetter


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
        if character_selection_method == "ban":
            whole_alphabet = string.digits + string.ascii_letters
            restricted_alphabet = ""
            for i in whole_alphabet:
                if i not in character_list:
                    restricted_alphabet += i
        else:
            restricted_alphabet = character_list
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
    def get_password_character_choice(cls, length, character_list, character_selection_method="ban"):
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
        print(character_selection_method)
        alphabet = PassGen.get_alphabet_character_choice(character_list, character_selection_method)
        return ''.join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=10, character_list="abcd", character_selection_method="ban"))
