import logging
from typing import Any as EndpointResult

from flask import jsonify
from werkzeug.exceptions import BadRequest, UnprocessableEntity, InternalServerError

from example.app import app
from example.exceptions import ExampleException

logger = logging.getLogger()


# This shows how to handle standard HTTP errors.
# For example, UnprocessableEntity would result from abort(422) (or from webargs.use).
@app.errorhandler(UnprocessableEntity)
def handle_validation_error(err: UnprocessableEntity) -> EndpointResult:
    messages = getattr(err, 'data', {}).get('messages')
    if messages:  # webargs.flaskparser.use_args/kwargs
        data = {
            'error_code': 'webargs_422',
            'messages': messages,
        }
    else:
        data = {
            'error_code': 'some_422',
        }
    return jsonify(data), err.code


# This shows how to handle an app-specific exception that isn't derived from werkzeug.exceptions.HTTPException.
@app.errorhandler(ExampleException)
def handle_expected_exception(e: ExampleException) -> EndpointResult:
    return jsonify({
        'error_code': 'example',
    }), BadRequest.code


# This shows how to handle an unexpected exception.
# In this handler, the argument will NOT be an 'InternalServerError' but rather the unexpected exception itself.
# (If you know what you expect, see 'handle_expected_exception' example.)
@app.errorhandler(InternalServerError)
def handle_unexpected_error(e: Exception) -> EndpointResult:
    logger.exception('Unknown error', exc_info=e)
    return jsonify({
        'error_code': 'custom_error',
        'error_type': str(type(e)),
    }), InternalServerError.code
