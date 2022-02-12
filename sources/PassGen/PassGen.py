import string
import secrets
from sources.Data.DataGetter import DataGetter


class PassGen:
    @classmethod
    def get_alphabet_character_choice(cls, characterList, characterSelectionMethod="ban"):
        # characterSelectionMethod :
        # only : use only characters in the list
        # ban : remove characters from the list
        # must : characters from the list are needed
        if characterSelectionMethod == "ban":
            wholeAlphabet = string.digits + string.ascii_letters
            restrictedAlphabet = ""
            for i in wholeAlphabet:
                if i not in characterList:
                    restrictedAlphabet += i
        else:
            restrictedAlphabet = characterList
        return restrictedAlphabet

    @classmethod
    def get_alphabet_french_words(cls):
        return DataGetter.get_french_words()

    @classmethod
    def get_password_words(cls, length):
        # alphabet = string.ascii_letters + string.digits
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for i in range(length))

    @classmethod
    def get_password_character_choice(cls, length, characterList, characterSelectionMethod="ban"):
        print(characterList)
        print(characterSelectionMethod)
        alphabet = PassGen.get_alphabet_character_choice(characterList, characterSelectionMethod)
        return ''.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=10, characterList="helo", characterSelectionMethod="ban"))