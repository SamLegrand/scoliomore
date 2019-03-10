from flask import Flask
from flask import render_template
from flask import session, request, json, redirect
from datetime import datetime

app = Flask(__name__)
app.secret_key = "abcdefgsecretkey123420"

## API ##

@app.route("/api/login", methods=["POST"])
def api_login():
    login = request.form.get("username")
    password = request.form.get("password")
    print("username: ", login, " , pass: ", password)

    if login == "tuur.frederickx" and password == "scoliomore":
        session['username'] = login
        return json.dumps({"Status": "Success"})
    elif login != "tuur.frederickx":
        return json.dumps({"Status": "ErrorUser"})
    elif password != "scoliomore":
        return json.dumps({"Status": "ErrorPassword"})

@app.route('/logout')
def api_logout():
    session.pop('username')
    return redirect('/')


## Routes ##

@app.route('/')
def render_home():
    return render_template('index.html', session=session)

@app.route('/login')
def render_login():
    if 'username' in session:
        return redirect('/')
    return render_template('login.html', session=session)

@app.route('/register')
def render_register():
    if 'username' in session:
        return redirect('/')
    return render_template('register.html', session=session)

@app.route('/calendar')
def render_calendar():
    day = datetime.today().weekday()
    if 'username' in session:
        return render_template('calendar.html', session=session, day=day)
    else:
        return redirect('/')

@app.route('/video/<int:video_id>')
def render_video(video_id):
    return render_template('show_video.html', session=session, video_id=video_id)



if __name__ == '__main__':
    app.run()
