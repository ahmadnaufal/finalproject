from flask import Flask
from flask import render_template, url_for
app = Flask(__name__)


@app.route("/")
def index():
    props = {
        'css': [
            url_for('static', filename='css/bootstrap.min.css'),
            url_for('static', filename='css/style.css')
        ],
        'js': [
            url_for('static', filename='js/jquery.min.js'),
            url_for('static', filename='js/main.js'),
            url_for('static', filename='js/bootstrap.min.js')
        ]
    }

    return render_template("index.html", props=props)


if __name__ == '__main__':
    app.run()
