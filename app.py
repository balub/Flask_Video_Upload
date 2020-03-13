from flask import Flask
import os
import os.path

dir = os.path.join(os.getcwd(), 'RecievedFiles')
if not os.path.exists(dir):
    os.makedirs(dir)
UPLOAD_FOLDER = dir # Path to Folder where the recieved mp4 file will be stored
print(dir)

res = os.path.join(os.getcwd(), 'Response')
if not os.path.exists(res):
    os.makedirs(res)
RESPONSE_FOLDER = res
print(res)

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESPONSE_FOLDER'] = RESPONSE_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

