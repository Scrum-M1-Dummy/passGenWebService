import string
import secrets
from sources.Data.DataGetter import DataGetter

class PassGen:
    @classmethod
    def get_password(cls, length):
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for i in range(length))


if __name__ == "__main__":
    print(PassGen.get_password(10))