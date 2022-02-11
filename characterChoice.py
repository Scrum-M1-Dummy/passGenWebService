import secrets
import string

def characterChoice(characterList,ban=False):
    if not(ban):
        restrictedAlphabet = characterList
    else:
        wholeAlphabet = string.digits
        restrictedAlphabet = ""
        for i in wholeAlphabet:
            if i not in characterList:
                restrictedAlphabet += i
    password = ''.join(secrets.choice(restrictedAlphabet) for i in range(8))
    return password