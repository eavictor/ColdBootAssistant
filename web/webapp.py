import eventlet
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask_socketio import disconnect, emit
from whitenoise import WhiteNoise
import time


eventlet.monkey_patch()


app = Flask(__name__)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config['SECRET_KEY'] = 'Intel'
socketio = SocketIO(app=app)


COUNT = 0


@app.route("/", methods=["GET"])
def index():
    """Send HTML file"""
    return render_template("index.html")


@socketio.on("connect")
def handle_connect():
    """
    Send current count to html page when anyone connect.
    """
    emit('update_count', COUNT, broadcast=True)


@socketio.on("disconnect")
def handle_disconnect():
    disconnect()


@socketio.on("count_plus_one")
def plus_count():
    """
    Callback function for coldboot.py / force_shutdown.py
    Update count number on html page.
    """
    global COUNT
    COUNT += 1
    emit('update_count', COUNT, broadcast=True)


@ socketio.on("count_minus_one")
def minus_count():
    """
    User manual minus count (for those who's hands are not clean).
    """
    global COUNT
    COUNT -= 1
    emit('update_count', COUNT, broadcast=True)


@socketio.on("reset_count")
def reset_count():
    """
    User manual reset count.
    """
    global COUNT
    COUNT = 0
    emit('update_count', COUNT, broadcast=True)


@socketio.on("boot_complete")
def boot_complete():
    """
    1. Receive boot complete signal from pc_boot_complete.py on target PC.
    2. Send force shutdown command to force_shutdown.py service.
    3. force_shutdown.py callback 'count_plus_one' to update count.
    """
    emit("force_shutdown", broadcast=True)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80, debug=False)
