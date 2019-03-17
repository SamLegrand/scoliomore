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

@app.route('/faq')
def render_faq():
    return render_template('faq.html', session=session)

@app.route('/calendar')
def render_calendar():
    day = datetime.today().weekday()
    if 'username' in session:
        return render_template('calendar.html', session=session, day=day)
    else:
        return redirect('/')

@app.route('/video/<int:video_id>')
def render_video(video_id):
    info = dict()
    if video_id is 1:
        info['video_name'] = 'Tuur%201.mp4'
        info['uh'] = 'Patiënt in handen- en knieënstand.'
        info['uv'] = 'Patiënt maakt afwisselend een holle en een bolle rug (geleidelijk). '
        info['set'] = ': 2 x 15 keer.'
        info['title'] = 'Oefening 1'
    elif video_id is 2:
        info['video_name'] = 'Thibaut%201.mp4'
        info['uh'] = 'Patiënt gesteund op ellebogen en voeten (schouders, heupen, knieën en enkels op één lijn)'
        info['uv'] = 'Afwisselend linker- en rechtervoet heffen (extensie/gestrekt houden van de heup).'
        info['uvlo'] = 'bekkengordel dient tijdens de oefening horizontaal te blijven!'
        info['set'] = '2 x 10 keer afwisselen.'
        info['title'] = 'Oefening 2'
    elif video_id is 3:
        info['video_name'] = 'Stijn%201.mp4'
        info['uh'] = 'Patiënt in handen- en knieënstand.'
        info['uv'] = 'Patiënt steekt één been naar achter, tegelijkertijd steekt hij/zij de hetero-laterale (aan de andere kant) arm naar voor (+ afwisselen).'
        info['uvlo'] = 'zowel de schouder- als de bekkengordel dienen tijdens heel de oefening horizontaal te blijven!'
        info['set'] = '2 x 16 keer afwisselen.'
        info['title'] = 'Oefening 3'
    elif video_id is 4:
        info['video_name'] = 'Tuur%202.mp4'
        info['uh'] = 'Patiënt in gestrekte kniezit op de zitbal (= onderbenen gesteund op de zitbal, heupen in extensie/gestrekt).'
        info['uv'] = 'Patiënt brengt met beide handen een gewichtje van beneden naar boven (en terug).'
        info['set'] = '2 x 8 keer.'
        info['title'] = 'Oefening 4'
    elif video_id is 5:
        info['video_name'] = 'Thibaut%202.mp4'
        info['uh'] = 'Patiënt gesteund op ellebogen (op de grond) en onderbenen (op de zitbal).'
        info['uhlo'] = 'schouders, heupen, knieën en enkels bevinden zich op één lijn.'
        info['uv'] = 'Afwisselend linker- en rechtervoet heffen (extensie/gestrekt houden van de heup).'
        info['uvlo'] = 'zowel de schouder- als de bekkengordel dienen tijdens heel de oefening horizontaal te blijven!'
        info['set'] = '3 x 6 keer afwisselen.'
        info['title'] = 'Oefening 5'
    elif video_id is 6:
        info['video_name'] = 'Jarne%202.mp4'
        info['uh'] = 'Patiënt in ruglig, met de bovenrug gesteund op de zitbal , de voeten op de grond. Knieën, heupen en schouders op één lijn.'
        info['uv'] = 'Afwisselend linker- en rechtervoet heffen.'
        info['uvlo'] = 'de bekkengordel dient tijdens heel de oefening horizontaal te blijven!'
        info['set'] = '4 x 6 keer wisselen van voet.'
        info['title'] = 'Oefening 6'
    return render_template('show_video.html', session=session, info=info)

if __name__ == '__main__':
    app.run()
