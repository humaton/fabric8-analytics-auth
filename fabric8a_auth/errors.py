"""Errors."""
class HTTPError(Exception):
    """Representation of HTTP error.

    This is a class that represents an HTTP error that occured somewhere.
    Each blueprint should have a function called `coreapi_http_error_handler`,
    which will accept instance of this class and return a response to its
    liking.

    This error is caught by `@app.errorhandler`, so all of raised HTTPError
    instances will be caught and handled there.
    """

    def __init__(self, status_code, error):
        """Call the superclass constructor and set status code and error attributes."""
        Exception.__init__(self)
        self.status_code = status_code
        self.error = error

class AuthError(HTTPError):
    """Authentication error.

    This error can be caught and handled by Flask's `@app.errorhandler`.

    Example:
        @app.errorhandler(AuthError)
        def api_401_handler(err):
            return flask.jsonify(error=err.error), err.status_code
    """

    def __init__(self, status_code=401, error='authentication error'):
        """Constructor.

        :param status_code:, int, HTTP status code
        :param error: str, error description
        """
        super().__init__(self)
        self.status_code = status_code
        self.error = error

    def __repr__(self):
        return 'AuthError(status_code={s},error={e})'.format(s=self.status_code, e=self.error)

    def __str__(self):
        return 'AuthError({s}): {e}'.format(s=self.status_code, e=self.error)
