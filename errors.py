from flask import Blueprint, redirect, render_template, request

blueprint = Blueprint('errors', __name__, template_folder='templates')


@blueprint.app_errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', title='404', url=request.base_url)