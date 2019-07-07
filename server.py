import os
import secrets
from jinja2 import StrictUndefined
from flask import (Flask, render_template, request, flash, redirect, session, url_for, abort, jsonify)
from sqlalchemy import desc
from flask_debugtoolbar import DebugToolbarExtension
from flask_bcrypt import Bcrypt
from flask_login import (LoginManager, login_user, logout_user, login_required, current_user)
import pprint
import json
with open('config/config.json', 'r') as f:
    config = json.load(f)

# ======================================================================
app = Flask(__name__)
Bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# Required to use Flask sessions and the debug toolbar
app.secret_key = config["secret_key"]["thomas"]

# Raises an error in Jinja2 for to debug
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def home():
    """Homepage."""
    return render_template('home.html')

@app.route('/resume')
def resume():
    """Resume."""
    return render_template('resume.html')

@app.route('/contact')
def contact():
    """Contact."""
    return render_template('contact.html')

# ======================================================================

if __name__ == "__main__":
    app.debug = True

    DebugToolbarExtension(app)
    app.run(host="0.0.0.0")