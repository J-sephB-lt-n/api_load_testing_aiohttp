"""
TODO
"""

import flask

import endpoints.get_task
import endpoints.get_gold
import endpoints.get_oil
import endpoints.get_water
import endpoints.deposit_resource

app = flask.Flask(__name__)

app.register_blueprint(endpoints.get_task.bp)
app.register_blueprint(endpoints.get_gold.bp)
app.register_blueprint(endpoints.get_oil.bp)
app.register_blueprint(endpoints.get_water.bp)
app.register_blueprint(endpoints.deposit_resource.bp)
