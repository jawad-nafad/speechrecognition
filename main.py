import os 
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename 

path = os.getcwd()
upload_folder = path

allowed_extensions = {'wav','png','jpeg'}

app = Flask(__name__)
app.config['upload_folder'] = upload_folder

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        #check if post req has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect (request.url)
        file = request.files['file']
        #if user does not select any file, browser submits empty string

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['upload_folder'], filename))
            return redirect(url_for('upload_file', filename=filename))

    return '''
    <!doctype html>
    <title> Upload a file </title>
    <h1> upload a file </h1>
    <form method= post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''






if __name__=="__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)