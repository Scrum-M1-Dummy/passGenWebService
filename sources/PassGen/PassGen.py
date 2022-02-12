import string
import secrets
from sources.Data.DataGetter import DataGetter


class PassGen:
    @classmethod
    def get_alphabet_character_choice(cls, character_list, ban=False):
        if ban:
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
        return '-'.join(secrets.choice(alphabet) for i in range(length))

    @classmethod
    def get_password_character_choice(cls, length, character_list, ban=False):
        print(character_list)
        print(ban)
        alphabet = PassGen.get_alphabet_character_choice(character_list, ban)
        return ''.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=10, character_list="helo", ban=False))
