#!/usr/bin/env python3


from flask import Flask
import flask
from flask import request
from flask.json import jsonify
from flask_cors import CORS, cross_origin
import json
import os
import uuid
import os
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/home/ubuntu/s-index/data/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg'])

@app.route("/models/", methods=['GET'])
def pred():
    try:
        #warm_text = request.args.get('warm', default='roses are red')
        print('server working')
    except ValueError:
        return jsonify({"error": "input error"})
    try:
        generated = {'s-index': 5, 'feedback':'simle more', 'img-caption': 'Be a Warrior not a Worrier.'}
    except KeyError:
        return jsonify({"error": "result not fonud"})
    return jsonify({"result": generated})


@app.route("/upload", methods=["POST"])
def upload():
    #print(request)
    if request.method == "POST":
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        f = request.files['file']
        f.save('kkkk1.jpg')
        #content = request.files['file']
        #print(content)
        #content.save(secure_filename(f.filename))
        #content = request.get_json(silent=True)
        #print(content)
        #data = content['myPhoto']['buffer']['data']
        #size = content['myPhoto']['size']
        #data.save(os.path.join(app.config['UPLOAD_FOLDER'], 'efg.jpg'))
        #return jsonify(content)
        #content.save(os.path.join(app.config['UPLOAD_FOLDER'], 'abc.jpg'))
        gen = {'s-index': 5, 'feedback': 'simple', 'img-caption': 'Be a Warrior not a Worrier'}
        #print(size)
        return  jsonify(gen)

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(host='0.0.0.0', port='8899')
