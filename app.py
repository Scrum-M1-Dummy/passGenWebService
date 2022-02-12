"""
If you are in the same directory as this file (app.py), you can run run the app using gunicorn:
    
    $ gunicorn --bind 0.0.0.0:<PORT> app:app

gunicorn can be installed via:

    $ pip install gunicorn

"""

from flask import Flask, jsonify, request, render_template

from sources.PassGen.PassGen import PassGen

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


@app.route('/', methods=["GET"])
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

    length = int(request.args.get('length'))
    if method == "words":
        password = PassGen.get_password_words(length)
        return render_template('home.html', password=password, title='Bonjour', description="stuff idk")
    elif method == "characters":
        character_list = request.args.get('characterList')
        character_selection_method = request.args.get('ban').lower()

        password = PassGen.get_password_character_choice(length=length,
                                                         character_list=character_list,
                                                         character_selection_method=character_selection_method)
        return render_template('home.html', password=password, title='Bonjour', description="stuff idk")


@app.route('/character_choice', methods=["GET"])
def get_password_character_choice():
    """
    TODO : Delete this entry point
    """
    length = int(request.args.get('length'))
    character_list = request.args.get('characterList')
    character_selection_method = request.args.get('ban').lower()
    print(character_selection_method)

    password = PassGen.get_password_character_choice(length=length,
                                                     character_list=character_list,
                                                     character_selection_method=character_selection_method)
    return render_template('home.html', password=password, title='Bonjour', description="stuff idk")


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

    response = {'STATUS': "Success",
                'request': json,
                'password': password,
                }
    return jsonify(response)  # response must be json serializable!
