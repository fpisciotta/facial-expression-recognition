from flask import Flask, request, render_template
from flask_uploads import UploadSet, configure_uploads, ALL
import analyzer as core_analysis
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/templates')
app.config['UPLOADED_FILES_DEST'] = 'uploads'
files = UploadSet('files', ALL)
configure_uploads(app, files)

# the core engine to analyze images
# ana = core_analysis.HPAnalysis();

# @app.route('/')
# def get_home():
#     return app.send_static_file('index.html')

@app.route('/', methods=['GET', 'POST'])
def post_image():
    if request.method == 'POST' and 'media' in request.files:
        filename = files.save(request.files['media'])
        print(filename)
        
    # return app.send_static_file('index.html')
    return render_template('index.html')


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)
