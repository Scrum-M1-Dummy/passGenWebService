from cmath import log
import string
import secrets
from sources.Data.DataGetter import DataGetter

class PassGen:
    @classmethod
    def get_alphabet_character_choice(cls, characterList, ban=False):
        if not (ban):
            restrictedAlphabet = characterList
        else:
            wholeAlphabet = string.digits + string.ascii_letters
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
    def get_password_entropy(self,passtest,characterList):
        L = len(passtest)
        R = len(characterList)
        E = L * log(R)/log(2)
        return E
    @classmethod
    def get_password_character_choice(cls, length, characterList, desired_entropy,ban=False):
        print(characterList)
        print(ban)
        alphabet = PassGen.get_alphabet_character_choice(characterList, ban)
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        while(PassGen.get_password_entropy(password,characterList).real < desired_entropy):
            password = ''.join(secrets.choice(alphabet) for i in range(length))
        return ''.join(secrets.choice(alphabet) for i in range(length))




if __name__ == "__main__":
    print(PassGen.get_password_character_choice(length=10, characterList="helo", ban=False))