from flask import Flask, request, send_file, jsonify
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'codes'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/",methods = ["GET"])
def hello():
    return jsonify({"message": "server is running"})

@app.route('/download/<filename>', methods = ['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return 'File Not Found', 404

