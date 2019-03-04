from flask import Flask
from flask import render_template
from flask import jsonify, session, request, redirect

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
    