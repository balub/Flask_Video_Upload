import os
import urllib.request
from app import app
from flask import Flask, request, redirect, jsonify, send_file, send_from_directory
from werkzeug.utils import secure_filename
import shutil

ALLOWED_EXTENSIONS = set(['mp4'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def convertVideo(file):  ##Function that will be called to do the convert shit
    print("Converting is happenning (not really)")
    shutil.copy(os.path.join(app.config['UPLOAD_FOLDER'])+f'\\{file.filename}', os.path.join(app.config['RESPONSE_FOLDER'])+f'\\{file.filename}')



@app.route('/upload', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        # file.save(os.path.join(app.config['RESPONSE_FOLDER'], filename))
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        convertVideo(
            file)  # # ideally pass the file as a parameter to the Function and get the converted video as the return
        try:
            resp = jsonify({'message': 'File successfully uploaded'})
            resp.status_code = 201
            dir = os.path.join(os.getcwd(), 'Response')
            return send_from_directory(dir, filename, as_attachment=True)
        except Exception as e:
            print(str(e))
            return jsonify({'Error': str(e)})
        return resp
    else:
        resp = jsonify({'message': 'Allowed file type is MP4 only'})
        resp.status_code = 400
        return resp


if __name__ == "__main__":
    app.run()
