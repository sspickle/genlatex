from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

bp = Blueprint('ui', __name__)

@bp.route('/')
def index():
    return render_template('ui/index.html')
