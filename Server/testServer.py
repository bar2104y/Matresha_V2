from flask import Flask
from flask import render_template

app = Flask(__name__)
app.host = '0.0.0.0'
app.debug = True


@app.route('/')
@app.route('/<lang>')
def index(lang='RU'):
    return render_template('index.html', lang=lang)


if __name__ == "__main__":
    app.run()