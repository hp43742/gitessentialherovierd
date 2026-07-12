
from flask import Flask

app = Flask('my flask app')

@app.route('/')
def index():
    return 'Hurray! Flask is working!'

# This program explains routes with parameters

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}! Welcome to API Development'  



# working with integer routes
@app.route('/square/<int:number>')
def square(number):
    return f'The square of {number} is {number**2}'



# working with Dictionary routes

http_status = {
    200: "OK - The request was successful",
    404: "Not Found - The requested resource does not exist",
    500: "Internal Server Error - The server encountered an unexpected condition"
}

@app.route('/status/<int:code>')    
def status(code):
    message = http_status.get(code, "Unknown Status Code")
    return f'Status Code: {code} - {message}'

@app.errorhandler(404)
def page_not_found(error):
    return "Invalid URL. Please check the route and try again.", 404




# RENDERING HTML FILES USING FLASK

from flask import Flask , render_template


app = Flask('my flask app')


@app.route('/')
def index():
    return render_template('index.html')


app.run(debug=True)
