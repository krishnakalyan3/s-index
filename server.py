#!/usr/bin/env python3


from flask import Flask
from flask import request
from flask.json import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/models/")
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


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8889')