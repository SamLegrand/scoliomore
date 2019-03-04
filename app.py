### TUTORIAL Len Feremans
###see tutor https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
from flask import Flask
from flask.templating import render_template
from flask import request, session, jsonify

### INITIALIZE SINGLETON SERVICES ###
app = Flask('scoliomore')

@app.route("/")
def main():
    return 'Hello World'

if __name__ == "__main__":
    app.run()
