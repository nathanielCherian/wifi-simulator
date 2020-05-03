from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, emit
from simi import runSim
app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)


@app.route('/')
def home():
    return render_template('home.html')



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

