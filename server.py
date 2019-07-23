from flask import Flask, request, render_template
import os
from werkzeug import secure_filename

UPLOAD_FOLDER = '/tmp'
app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'verysecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024

@app.route('/upload')
def upload_file():
    return render_template('upload.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['test']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
        print(f.filename)
        return 'file uploaded successfully'

if __name__ == "__main__":
    app.run(debug=True)
