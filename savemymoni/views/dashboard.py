from flask import Blueprint
from flask import render_template


mod = Blueprint('dashboard', __name__)

@mod.route('/', methods=['GET', 'POST'])
def dashboard_index():
	return render_template('base.html')
