"""
Defines endpoint /get_endpoint_logs
"""

import json

import flask

bp = flask.Blueprint("get_endpoint_logs", __name__)


@bp.route("/get_endpoint_logs", methods=["GET"])
def get_endpoint_logs():
    page: int = int(flask.request.args["page"])
    return flask.Response(
        json.dumps(
            {
                "logs": "TODO",
                "page": 1,
                "total_pages": 69,
            }
        ),
        status=200,
    )
