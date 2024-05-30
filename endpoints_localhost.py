"""
TODO
"""

import logging
import os

import flask

import endpoints.get_task
import endpoints.get_gold
import endpoints.get_oil
import endpoints.get_water
import endpoints.deposit_resource

if os.path.exists("logs/endpoints.log"):
    os.remove("logs/endpoints.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(message)s",
    handlers=[logging.FileHandler("logs/endpoints.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

app = flask.Flask(__name__)

app.register_blueprint(endpoints.get_task.bp)
app.register_blueprint(endpoints.get_gold.bp)
app.register_blueprint(endpoints.get_oil.bp)
app.register_blueprint(endpoints.get_water.bp)
app.register_blueprint(endpoints.deposit_resource.bp)
