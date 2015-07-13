from flask import Flask

__version__ = "0.0.1"

app = Flask(__name__)

app.config.from_object('websiteconfig')

app.secret_key = 'why would I tell you my secret key?'

from savemymoni.views import dashboard

app.register_blueprint(dashboard.mod)