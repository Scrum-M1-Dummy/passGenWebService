"""
If you are in the same directory as this file (app.py), you can run run the app using gunicorn:
    
    $ gunicorn --bind 0.0.0.0:<PORT> app:app

gunicorn can be installed via:

    $ pip install gunicorn

"""
import os
from pathlib import Path
import logging
from sources.Main.utilitaires.logger import LoggingLogger
from sources.Main.utilitaires.keys import *
import json as jsn

from IPython.core.display import JSON
from flask import Flask, jsonify, request, abort
import sklearn
import pandas as pd
import numpy as np
import joblib
import datetime

from sources.LANG.log_string import *
from sources.LANG.msg_string import *
import sources

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
    global logger, cmm
    logging.basicConfig(filename=LOG_FILE,
                        level=logging.INFO,
                        format="{'time':'%(asctime)s', 'name': '%(name)s', 'level': '%(levelname)s', 'message': %(message)s, 'transmission': %(transmission)s,'file': '%(caller_file)s', 'function': '%(caller_func)s'}")
    logger = LoggingLogger()
    logger.log(LOG_LOGGER_INITIALIZED())

    # DONE: any other initialization before the first request (e.g. load default model)
    pass


@app.route("/logs", methods=["GET"])
def logs():
    """Reads data from the log file and returns them as the response"""
    # pour tester dans un navigateur:
    # http://0.0.0.0:8080/logs

    logger.log(LOG_REQUEST_RECEIVED())
    logger.log(LOG_SENDING_LOGS_TO_CLIENT())  # before doing it in order to include it in the return for consistency

    raw_logs = []
    with open(LOG_FILE, 'r') as log_file:
        c_log = log_file.readline()
        while c_log:
            raw_logs.append(c_log.strip('\n\r'))
            c_log = log_file.readline()

    logs = []
    in_irregular_log = False
    irregular_log_index = 0
    for log_line in raw_logs:
        if log_line[0] == '{':
            in_irregular_log = False
            nan = None
            logs.append(eval(log_line))  # évalue le dico
        else:
            if not in_irregular_log:
                irregular_log_index = 0
                logs.append({'time': 'UNKNOWN', 'name': 'app', 'level': 'Python Traceback', 'message': log_line})
                in_irregular_log = True
            else:
                logs[-1]['message' + str('{0:03}'.format(irregular_log_index))] = log_line
                irregular_log_index += 1

    response = logs  # raw format for easy display in firefox

    return jsonify(response)  # response must be json serializable!


@app.route("/test", methods=["POST"])
def test():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/test

    Returns the request
    """

    # Get POST json data
    json = request.get_json()
    logger.log(LOG_REQUEST_RECEIVED(), transmission=json)

    response = {STATUS: SUCCESS,
                'request': json,
                }
    logger.log(LOG_SENDING_RESPONSE_TO_CLIENT(), transmission=json)
    return jsonify(response)  # response must be json serializable!


@app.route("/set_log_lang", methods=["POST"])
def set_log_lang():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/set_log_lang

    Returns the log language after setting it
    """

    json = request.get_json()
    logger.log(LOG_REQUEST_RECEIVED(), transmission=json)

    if not 'LANG' in json:
        response = {STATUS: WARNING,
                    MESSAGE: MSG_MISSING_KEY('LANG', example='\'LANG_LOG_FRA\'')
                    }
        logger.log_warn(LOG_MISSING_KEY('LANG'), transmission=response)
    else:
        try:
            launch_log_lang(json['LANG'])
            response = {STATUS: SUCCESS,
                        MESSAGE: MSG_LOG_LANG_CHANGED_SUCCESSFULLY(get_lang_log_source()),
                        'LANG': get_lang_log_source()}
            logger.log(LOG_LOG_LANG_CHANGED_SUCCESSFULLY(get_lang_log_source()), transmission=response)
        except Exception as e:
            response = {STATUS: ERROR,
                        MESSAGE: MSG_LOG_LANG_CHANGE_ERROR(get_lang_log_source()),
                        'LANG': get_lang_log_source()}
            logger.log_err({MESSAGE: LOG_LOG_LANG_CHANGE_ERROR(get_lang_log_source()),
                            ERROR: str(e)},
                           transmission=response)

    return jsonify(response)  # response must be json serializable!


@app.route("/set_lang", methods=["POST"])
def set_lang():
    """
    Handles POST requests made to http://IP_ADDRESS:PORT/set_lang

    Returns the language of the responses to the client after setting it
    """

    json = request.get_json()
    logger.log(LOG_REQUEST_RECEIVED(), transmission=json)

    if not 'LANG' in json:
        response = {STATUS: WARNING,
                    MESSAGE: MSG_MISSING_KEY('LANG', example='\'LANG_LOG_FRA\'')
                    }
        logger.log_warn(LOG_MISSING_KEY('LANG'), transmission=response)
    else:
        try:
            launch_msg_lang(json['LANG'])
            response = {STATUS: SUCCESS,
                        MESSAGE: MSG_MSG_LANG_CHANGED_SUCCESSFULLY(get_lang_msg_source()),
                        'LANG': get_lang_msg_source()}
            logger.log(LOG_MSG_LANG_CHANGED_SUCCESSFULLY(get_lang_msg_source()), transmission=response)
        except Exception as e:
            response = {STATUS: ERROR,
                        MESSAGE: MSG_MSG_LANG_CHANGE_ERROR(get_lang_msg_source()),
                        'LANG': get_lang_log_source()}
            logger.log_err({MESSAGE: LOG_MSG_LANG_CHANGE_ERROR(get_lang_msg_source()),
                            ERROR: str(e)},
                           transmission=response)

    return jsonify(response)  # response must be json serializable!
