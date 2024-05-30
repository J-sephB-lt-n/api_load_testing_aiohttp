"""
Defines endpoint /deposit_resource
"""

import json
import random
import time

import flask

import config

bp = flask.Blueprint("deposit_resource", __name__)


@bp.route("/deposit_resource", methods=["POST"])
def deposit_resource():
    input_json = flask.request.get_json()
    time.sleep(config.ENDPOINT_PROCESS_TIME_NSECS["/get_task"])
    return flask.jsonify(
        {
            "resource": input_json["resource"],
            "deposit_status": "SUCCESS",
            "amount": input_json["amount"],
        }
    )
