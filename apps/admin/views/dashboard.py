from flask import render_template
from .. import admin 

@admin.route('/admin')
def dashboard():
    return render_template('admin/dashboard.html')
