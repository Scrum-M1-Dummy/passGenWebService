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


from flask import Flask, jsonify, request

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

@app.route("/test", methods=["GET"])
def test():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/test

    Returns the request
    """

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(8))

    # Get POST json data
    json = request.get_json()

    response = {'Access-Control-Allow-Origin': "*",
                'STATUS': "Success",
                'request': json,
                'password': password,
                }
    return jsonify(response)  # response must be json serializable!
