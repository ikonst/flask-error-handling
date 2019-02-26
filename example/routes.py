from flask import abort, jsonify
from marshmallow import fields
from webargs.flaskparser import use_kwargs

from example.app import app
from example.exceptions import AppSpecificException


@app.route('/abort_422')
def abort_422_route():
    abort(422)


@app.route('/raise_app_specific_exception')
def raise_app_specific_exception_route():
    raise AppSpecificException()


@app.route('/raise_unexpected_exception')
def raise_unexpected_exception_route():
    int('foobar')  # raises ValueError


@app.route('/webargs_validation')
@use_kwargs({'number': fields.Number()})
def webargs_validation_route():
    return jsonify({})
