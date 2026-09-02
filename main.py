import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # Had saiz fail 50MB

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mastering')
def mastering():
    filename = request.args.get('filename', '')
    return render_template('mastering.html', filename=filename)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'audio_file' not in request.files:
        return redirect(url_for('index'))
    file = request.files['audio_file']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('mastering', filename=filename))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    
