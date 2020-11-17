from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/bulletin')
def bulletin():
    bulletin_id = request.args.get('bulletin_id')
    file = 'bulletin.html'
    if bulletin_id is not None:
        file = "bulletin/" + bulletin_id + ".html"
    return render_template(file)

@app.route('/project')
def project():
    project_id = request.args.get('project_id')
    file = 'project.html'
    if project_id is not None:
        file = "project/" + project_id + ".html"
    return render_template(file)

@app.route('/intro')
def intro():
    return render_template("intro.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run()