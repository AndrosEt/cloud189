#!/usr/bin/env python3

import sys
from cloud189.cli.cli import Commander
from cloud189.cli.utils import print_logo, check_update, error
from flask import Flask, jsonify, request, redirect
from cloud189.api.core import Cloud189
from time import sleep
import json
import numpy as np


# You can change this to any folder on your system
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)


commander = Commander()



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def listToJson(lst):
    keys = [str(x) for x in np.arange(len(lst))]
    list_json = dict(zip(keys, lst))
    str_json = json.dumps(list_json, ensure_ascii=False)  # json转为string
    return str_json



@app.route('/v1/getList', methods=['GET'])
def get_file_list():
    # Check if a valid image file was uploaded
    print('get the file list')
    if request.method == 'GET':

        result = commander.ls(['-l'], -13)

        print(result)

        return result

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''


@app.route('/v1/fileurl', methods=['GET'])
def get_file_url():
    # Check if a valid image file was uploaded
    print('get the file url')
    if request.method == 'GET':
        url = request.args.get('url')
        print(url)

        result = commander.get_url(url)

        print(result)

        return result

    # If no valid image file was uploaded, show the file upload form:
    return '''
    <!doctype html>
    <title>Is this a picture of Obama?</title>
    <h1>Upload a picture and see if it's a picture of Obama!</h1>
    <form method="POST" enctype="multipart/form-data">
      <input type="file" name="file">
      <input type="submit" value="Upload">
    </form>
    '''

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    print(f"Arguments count: {sys.argv[1]}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")
    commander.login("", sys.argv[1], sys.argv[2])
    app.run(host='0.0.0.0', port=1281, debug=True)
