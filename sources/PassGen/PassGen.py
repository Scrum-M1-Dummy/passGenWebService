import string
import secrets
from sources.Data.DataGetter import DataGetter


class PassGen:
    @classmethod
    def get_alphabet_character_choice(cls, character_list, character_selection_method="ban"):
        # character_selection_method :
        # only : use only characters in the list
        # ban : remove characters from the list
        # must : characters from the list are needed
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
        return DataGetter.get_french_words()

    @classmethod
    def get_password_words(cls, length):
        # alphabet = string.ascii_letters + string.digits
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for _ in range(length))

    @classmethod
    def get_password_character_choice(cls, length, character_list, character_selection_method="ban"):
        print(character_list)
        print(character_selection_method)
        alphabet = PassGen.get_alphabet_character_choice(character_list, character_selection_method)
        return ''.join(secrets.choice(alphabet) for _ in range(length))


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=10, character_list="abcd", character_selection_method="ban"))
