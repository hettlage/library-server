from flask import current_app, jsonify, render_template

from . import api_v1


@api_v1.errorhandler(500)
def internal_server_error(e):
    current_app.logger.error(str(e), exc_info=1)

    return render_error(500, 'Internal error: {message}'.format(message=e))


@api_v1.errorhandler(404)
def file_not_found_error(e):
    return render_error(404, 'Not found')


@api_v1.errorhandler(Exception)
def exception_raised(e):
    current_app.logger.error(str(e), exc_info=1)

    return render_error(500, 'Internal error: {message}'.format(message=e))


def render_error(status_code, message):
    error = {
        'status': status_code,
        'message': message
    }

    return jsonify(error), status_code
