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
    bulletin_page = request.args.get('bulletin_page')
    file = 'bulletin/page/bulletin_1.html'
    if bulletin_id is not None:
        file = "bulletin/content/" + bulletin_id + ".html"
    if bulletin_page is not None:
        file = "bulletin/page/bulletin_" + bulletin_page + ".html"
    return render_template(file)


@app.route('/project')
def project():
    project_id = request.args.get('project_id')
    file = 'project.html'
    if project_id is not None:
        file = "project/" + project_id + ".html"
    return render_template(file)


@app.route('/recruitment')
def recruitment():
    return render_template("recruitment.html")


@app.route('/intro')
def intro():
    return render_template("intro.html")


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run()
