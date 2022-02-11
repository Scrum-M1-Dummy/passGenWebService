import string
import secrets
from sources.Data.DataGetter import DataGetter

class PassGen:
    @classmethod
    def get_alphabet_character_choice(cls, characterList, ban=False):
        if not (ban):
            restrictedAlphabet = characterList
        else:
            wholeAlphabet = string.digits
            restrictedAlphabet = ""
            for i in wholeAlphabet:
                if i not in characterList:
                    restrictedAlphabet += i
        return restrictedAlphabet

    @classmethod
    def get_alphabet_french_words(cls):
        return DataGetter.get_french_words()

    @classmethod
    def get_password(cls, length):
        # alphabet = string.ascii_letters + string.digits
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for i in range(length))

    @classmethod
    def get_password_character_choice(clsclf, length, characterList, ban=False):
        alphabet = PassGen.get_alphabet_character_choice()
        return '-'.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    print(PassGen.get_password(10))