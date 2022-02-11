"""
If you are in the same directory as this file (app.py), you can run run the app using gunicorn:
    
    $ gunicorn --bind 0.0.0.0:<PORT> app:app

gunicorn can be installed via:

    $ pip install gunicorn

"""
import logging
import os
import secrets
import string

from sources.PassGen.PassGen import PassGen


from flask import Flask, jsonify, request,render_template

from sources.LANG.log_string import *
from sources.LANG.msg_string import *

# Chemin du fichier de log
LOG_FILE = os.environ.get("FLASK_LOG", "flask.log")

app = Flask(__name__)
logger = None

@app.before_first_request
def before_first_request():
    """
    Hook to handle any initialization before the first request (e.g. load model,
    setup logging handler, etc.)
    """

    # DONE: any other initialization before the first request (e.g. load default model)
    pass


@app.route('/', methods=["GET"])
def home():
    length = int(request.args.get('length'))
    password = PassGen.get_password(length)
    return render_template('home.html', password=password, title='Bonjour', description="stuff idk")

@app.route('/character_choice', methods=["GET"])
def get_password_character_choice():
    length = int(request.args.get('length'))
    characterList = request.args.get('characterList')
    characterSelectionMethod = request.args.get('ban').lower()
    print(characterSelectionMethod)

    password = PassGen.get_password_character_choice(length=length, characterList=characterList, characterSelectionMethod=characterSelectionMethod)
    return render_template('home.html', password=password, title='Bonjour', description="stuff idk")

@app.route("/test", methods=["GET"])
def test():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/test

    Returns the request
    """

    length = int(request.args.get('length'))
    password=PassGen.get_password(length)
    # Get POST json data
    json = request.get_json()

    response = {'Access-Control-Allow-Origin': "*",
                'STATUS': "Success",
                'request': json,
                'password': password,
                }
    return jsonify(response)  # response must be json serializable!

