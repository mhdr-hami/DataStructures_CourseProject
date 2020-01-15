import os
from flask import render_template, request, redirect, url_for
from werkzeug import secure_filename
from flask import Flask
from flask import request
import runpy

app = Flask(__name__)



@app.route('/')
def index():
    return render_template("FileReader.html")

@app.route('/Loading', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        try:
            uploads_dir = os.path.join(app.root_path, 'data')
            os.makedirs(uploads_dir, exist_ok=True)
        except OSError as error:
            print("Upload_exception")

        # save the single "profile" file
        # profile = request.files['profile']
        # profile.save(os.path.join(uploads_dir, secure_filename(profile.filename)))

        # save each "charts" file
        for file in request.files.getlist('TheDataset'):
            # file.save(os.path.join(uploads_dir, file.name))
            print(os.path.join(uploads_dir, secure_filename(file.filename)))
            file.save(os.path.join(uploads_dir, secure_filename(file.filename)))

        # return redirect(url_for('upload'))

        import Faze4
        print("f2:", Faze4.fazeTwoSuspected)
        print("f3:", Faze4.fazeThreeSuspected)
        print("f4:",Faze4.fazeFourSuspected)
        return render_template('index.html')

    return render_template('FileReader.html')

app.run(debug=True, port=8000, host='0.0.0.0')
