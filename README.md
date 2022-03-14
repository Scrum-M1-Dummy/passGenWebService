# PassGenWebService

Ce service web permet de générer un mot de passe en utilisant diverses méthodes de génération. 

## Méthode de génération par caractères

> Option **Caractère**
> 

Il y a 4 paramètres utilisés lors de cette génération dont 2 exclusif à cette méthode.  

Cette méthode de génération de mot de passe a trois sous méthode:

- “BlackList:” cette méthode va utiliser tous les caractères sauf ceux présent dans la liste de caractères pour générer le mot de passe
- “A inclure”: cette méthode va inclure obligatoirement les caractères de la liste dans le mot de passe
- “WhiteList”: cette méthode va utiliser uniquement les caractères présent dans la liste pour générer le mot de passe

Le paramètre “liste de caractère” permet de spécifier suivant la sous méthode de génération utilisée une liste de caractères. 

<aside>
💡 Possibilités:

- “\d”: ajoute un chiffre peu importe lequel
- “\c”: ajoute un caractère en minuscule peu importe lequel
- “\C”: ajoute un caractère en majuscule peu importe lequel
- “\s”: ajoute un caractère spécial peu importe lequel
- n’importe quel caractère ASCII

Exemple de liste:

> abc\d
> 

Avec la sous méthode inclure, cela va inclure dans le mot de passe les lettres “a”,”b”,”c” et un chiffre au hasard.

</aside>

## Méthode de génération par mots

> Option **Mots**
> 

Cette méthode permet de générer des mots de passe contenant des mots au hasard.

- “Langue des mots” : indique la langue des mots du mot de passe à produire parmi les langues suivantes :
    - Français
    - Anglais
- Caractère de séparation : indique le caractère à utiliser pour séparer les mots

## Méthode de génération de phrase

> Option **Phrase**
> 

Cette méthode permet de générer des mots de passes qui ressemblent plus ou moins à des phrases ayant une signification.

- “Langue des mots” : indique la langue des mots du mot de passe à produire parmi les langues suivantes :
    - Français
    - Anglais
- Caractère de séparation : indique le caractère à utiliser pour séparer les mots

## Documentation développeur

### Application

```python
def home():
    """
    home page
    Charge une page affichant le mot de passe généré selon les informations transmise via la méthode get
    paramètres de la requête:
    _mot de passe contenant des mots_
    method = "words"
    length: int

    _mot de passe contenant des caractères_
    method = "words"
    length: int
    characterList: string
    ban: "only", "ban", "must"
    """
```

### Entropie

```python
def get_password_entropy(self, passtest, characterList):
        """
        @param passtest: mot de passe à tester
        @param characterList: liste des caractères possible dans le choix du mot de passe
        @return: l'entropie du mot de passe
        """
```

### Liste de mot

```python
def get_words_from_file(fileName,sepLines=False)
```

<aside>
💡 String fileName:nom du fichier contenant une liste de mots

</aside>

<aside>
💡 Boolean sepLines(defaut:False):Definit si les mots sont séparer par des lignes ou non

</aside>

Retourne une liste de mots a utilisé selon un fichier .txt qui définit une liste de mots(par exemple un dictionaire) et une liste de stop words(nommé *fileName*.stop)

### Génération de mot de passe à partir de caractères

```python
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
```

```python
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
```