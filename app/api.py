# -*- coding: utf-8 -*-

import json
import logging

from flask import Flask


app = Flask(__name__)


def rest_success(obj):
    return json.dumps(obj), 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route("/", methods=["GET"])
def api_home():
    logging.info("API / executing")
    obj = {
        "status": "OK"
    }
    return rest_success(obj)
    