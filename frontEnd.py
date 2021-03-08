import os 
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename 
from fileProcessor import transcribing


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
            var = transcribing(filename)
            #{{var['transcription']}}
            result = var['transcription']
            return render_template('index.html', result=result)

          

            #filename = request.args.get('<filename>','')
            #transcribing(var)
        

    return render_template('index.html')
'''
@app.route('/<var>')
def tt(var):                
    return transcribing(var)
'''
'''@app.route('/<filename>')
def processing(filename):
    filename=upload_folder()
    transcribing(filename)
    return render_template('index.html')'''





if __name__=="__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
    

    