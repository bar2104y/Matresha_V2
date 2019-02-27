from flask import Flask
from flask import render_template

app = Flask(__name__)
app.host = '0.0.0.0'
app.port = 8080
app.debug = True


@app.route('/')
@app.route('/<lang>')
def index(lang='RU'):
	return render_template('index.html', lang=lang)

@app.route('/robotid/<id>/GoRoom/<AudNumber>')
def goAudiories(id=0, AudNumber=1111):
	print("id = ", id)
	print('Num = ', AudNumber)
	return "123"




if __name__ == "__main__":
	app.run()