from flask import Flask, request, send_from_directory
import analyzer as core_analysis
import json

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')
# ana = core_analysis.HPAnalysis();

@app.route('/')
def get_home():
    return app.send_static_file('index.html')

@app.route('/pics/<path:path>')
def get_pics(path):
    return send_from_directory('pics', path)

@app.route('/<path:path>')
def get_static(path):
    return send_from_directory('static', path)

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
    app.run()
