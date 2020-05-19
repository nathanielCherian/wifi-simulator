from flask import Flask, render_template, url_for, session, redirect
from flask_socketio import SocketIO, emit
from datetime import timedelta
from simi import runSim
from forms import loginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
app.config['password'] = 'password'
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=5)
socketio = SocketIO(app)


@app.route('/')
def home():
    if session.get('password') == app.config['password']:
        return render_template('home.html')
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    form=loginForm()
    if form.validate_on_submit():

        if form.password.data == app.config['password']:
            session['password'] = app.config['password'] 
            session.permanent = True
            return redirect(url_for('home'))

    return render_template('login.html', form=form)



def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    data = runSim(json)
    json = {'set1':data[0], 'set2':data[1], 'set3':data[2], 'set4':data[3]}
    emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
	socketio.run(app, debug=True, host='0.0.0.0')

