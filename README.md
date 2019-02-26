# flask-error-handling

Many Flask projects want to handle some exceptions in a generic way. This sample shows how to use Flask's `@app.errorhandler` to set up global error handlers for your Flask app. This pattern respects the [propagate_exceptions](http://flask.pocoo.org/docs/1.0/config/#PROPAGATE_EXCEPTIONS) flag, which greatly simplifies debugging [test](http://flask.pocoo.org/docs/1.0/testing/) failures.
