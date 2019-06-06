import eventlet
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import disconnect, emit
from whitenoise import WhiteNoise


eventlet.monkey_patch()


app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config['SECRET_KEY'] = 'Intel'
socketio = SocketIO(app=app)


COUNT = 0


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    emit('update_count', COUNT, broadcast=True)


@socketio.on("disconnect")
def handle_disconnect():
    disconnect()


@socketio.on("count_plus_one")
def plus_count():
    global COUNT
    COUNT += 1
    emit('update_count', COUNT, broadcast=True)


@ socketio.on("count_minus_one")
def minus_count():
    global COUNT
    COUNT -= 1
    emit('update_count', COUNT, broadcast=True)


@socketio.on("reset_count")
def reset_count():
    global COUNT
    COUNT = 0
    emit('update_count', COUNT, broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80, debug=False)
