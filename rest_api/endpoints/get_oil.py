"""
Defines endpoint /get_oil
"""

import json
import random
import time

import flask

import config

bp = flask.Blueprint("get_oil", __name__)


@bp.route("/get_oil", methods=["GET"])
def get_oil():
    time.sleep(config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.jsonify(
        {
            "resource": "oil",
            "amount": random.randint(0, 5),
        }
    )
