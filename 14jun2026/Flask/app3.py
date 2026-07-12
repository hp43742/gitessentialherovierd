
# RENDERING HTML FILES USING FLASK

from flask import Flask , render_template


app = Flask('my flask app')


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
