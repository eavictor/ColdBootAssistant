import socketio
from socketio.exceptions import ConnectionError


HOST = "http://192.168.1.1"
DELAY = 30


sio = socketio.Client()


def connect_socketio():
    while True:
        try:
            sio.connect(HOST)
            break
        except ConnectionError:
            continue


def boot_complete():
    sio.emit("boot_complete", {"delay": DELAY})


if __name__ == "__main__":
    connect_socketio()
    boot_complete()
