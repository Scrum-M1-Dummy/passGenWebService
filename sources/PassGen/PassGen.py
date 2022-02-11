import string
import secrets
from sources.Data.DataGetter import DataGetter

class PassGen:
    def gen_passwd(self):
        alphabet = DataGetter.get_french_words()
        return '-'.join(secrets.choice(alphabet) for i in range(8))


if __name__ == "__main__":
    pg = PassGen()
    print(pg.gen_passwd())