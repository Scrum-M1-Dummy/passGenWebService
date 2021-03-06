"""
If you are in the same directory as this file (app.py), you can run run the app using gunicorn:
    
    $ gunicorn --bind 0.0.0.0:<PORT> app:app

gunicorn can be installed via:

    $ pip install gunicorn

"""

from flask import Flask, jsonify, request, render_template

from sources.PassGen.PassGen import PassGen
from sources.keys import *
from sources.Data.DataGetter import DataGetter

app = Flask(__name__)
logger = None


@app.before_first_request
def before_first_request():
    """
    Hook to handle any initialization before the first request (e.g. load model,
    setup logging handler, etc.)
    """

    # TODO: any other initialization before the first request (e.g. load default model)
    pass


@app.route('/gen', methods=["GET"])
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
    method = request.args.get('method')
    if method is None:
        return render_template('error.html', title='Bonjour', description="stuff idk")
    length = 0

    if method == "words":
        length = int(request.args.get('lengthWord'))
        word_delimitor = request.args.get('word_delimitor')
        lang = request.args.get('lang')
        desired_entropy = int(request.args.get('desired_entropy'))
        if word_delimitor is None or word_delimitor=="colle":
            word_delimitor=""
        password, entropy = PassGen.get_password_words(length, lang, word_delimitor, desired_entropy=desired_entropy)
        return render_template('home.html', password=password, title='Bonjour', description="stuff idk", entropy=round(entropy.real, 3))
    elif method == "sentence":
        length = int(request.args.get('lengthWord'))
        word_delimitor = request.args.get('word_delimitor')
        desired_entropy = int(request.args.get('desired_entropy'))
        if word_delimitor is None:
            word_delimitor=""

        lang = request.args.get('lang')
        password, entropy = PassGen.get_password_sentence(length, lang, word_delimitor, desired_entropy=desired_entropy)
        return render_template('home.html', password=password, title='Bonjour', description="stuff idk", entropy=round(entropy.real, 3))
    elif method == "characters":
        '''character_list = request.args.get('characterList')
        character_selection_method = request.args.get('character_selection_method').lower()
        password = get_password_character_choice()'''
        length = int(request.args.get('lengthCharacter'))
        characterString = request.args.get('characterList')
        characterList=[]
        ct=0
        while ct<(len(characterString)):
            if characterString[ct]=="\\" and ct<(len(characterString)-1):
                st=""
                if characterString[ct+1]=="[":
                    tmp=ct+2
                    st="\\["
                    while tmp<(len(characterString)) and characterString[tmp]!="]":
                        st+=characterString[tmp]
                        tmp+=1
                    st+="]"
                    ct=tmp+1
                else:
                    st=characterString[ct]+characterString[ct+1]
                characterList.append(st)
                ct+=1
            else:
                characterList.append(characterString[ct])
            ct+=1
        character_selection_method = request.args.get('character_selection_method').lower()
        desired_entropy = int(request.args.get('desired_entropy'))
        print(desired_entropy)

        password, entropy = PassGen.get_password_character_choice(length=length, character_list=characterList,
                                                         desired_entropy=desired_entropy, character_selection_method=character_selection_method)
        return render_template('home.html', password=password, title='Bonjour', description="stuff idk",
                               entropy=round(entropy.real, 3))

@app.route("/test", methods=["GET"])
def test():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/test

    Returns the request and the password in the json format
    """
    # noinspection PyBroadException
    try:
        length = int(request.args.get('length'))
    except Exception as e:
        length = 10

    password = PassGen.get_password_words(length)
    # Get POST json data
    json = request.get_json()

    response = {STATUS: "Success",
                REQUEST: json,
                PASSWORD: password,
                }
    return jsonify(response)  # response must be json serializable!

@app.route("/index", methods=["GET"])
def index():
    return render_template("indexMultipleField.html")
