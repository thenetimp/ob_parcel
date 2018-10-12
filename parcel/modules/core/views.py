# users/views.py
import os
from flask import Flask, flash, request, redirect, render_template, url_for, Blueprint, session, current_app as app
from werkzeug.utils import secure_filename

core_views = Blueprint('core_views', __name__)

##############################
# login user page
##############################
@core_views.route('/')
def page_index():
    return render_template('v1/index.html')
    

@core_views.route('/upload', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
    
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('core_views.upload_file',
                                    filename=filename))
                                    
    return "done"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

