import os
from flask import render_template, request, redirect, url_for
# from werkzeug import secure_filename
from flask import Flask
from flask import request
from flask import jsonify
import random

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def index():
    temp = "?q=" + str(random.randint(0, 100000))
    return render_template("FileReader.html", temp=temp)


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
            print(os.path.join(uploads_dir, file.filename))
            file.save(os.path.join(uploads_dir, file.filename))

        # return redirect(url_for('upload'))


        import Faze4
        import copy
        print("f2:", Faze4.fazeTwoSuspected)
        print("f3:", Faze4.fazeThreeSuspected)
        print("f4:", Faze4.fazeFourSuspected)
        rand = "?q=" + str(random.randint(0, 100000))
        return render_template('index.html', rand=rand, f1=Faze4.personDictionary, f2=Faze4.fazeTwoSuspected,
                               f3=Faze4.fazeThreeSuspected, f4=Faze4.fazeFourSuspected)

    return render_template('FileReader.html')


@app.route('/person')
@app.route('/person/<idNumber>')
def show_person(idNumber):
    return "Hello"


@app.route('/graph')
def show_graph():
    import Faze4
    graph = {}
    nodes = []
    links = []
    for item in Faze4.list_of_paths:
        key = item[0]
        temp_dic = {"name": Faze4.personDictionary[str(key)].name, "label": Faze4.personDictionary[str(key)].familyName,
                    "id": key, "job": "suspected"}
        nodes.append(temp_dic)
        for i in range(1, len(item)):
            temp_dic = {"name": Faze4.personDictionary[str(item[i])].name, "label": Faze4.personDictionary[str(item[i])].familyName, "id": item[i], "job": Faze4.personDictionary[str(item[i])].job}
            nodes.append(temp_dic)
        for i in range(len(item)-1):
            temp_dic = {"source": item[i+1], "target": item[i], "type": "", "since": 0}
            links.append(temp_dic)
    graph["nodes"] = nodes
    graph["links"] = links
    rand = "?q=" + str(random.randint(0, 100000))
    return render_template("graph.html", dic=str(graph), rand=rand)


app.run(debug=True, port=8000, host='127.1.1.0')
