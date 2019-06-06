import RPi.GPIO as GPIO
import time
import socketio
from socketio.exceptions import ConnectionError


GPIO.setmode(GPIO.BOARD)

# Setup PowerLED + input listener on PIN 3
input_channel = 3
GPIO.setup(input_channel, GPIO.IN)

# Setup PowerSwitch RELAY control on PIN 12
output_channel = 12
GPIO.setup(output_channel, GPIO.OUT, initial=GPIO.LOW)


sio = socketio.Client()


@sio.on("force_shutdown")
def force_shutdown():
    # Simulate Force Shutdown
    GPIO.output(output_channel, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(output_channel, GPIO.LOW)

    # Wait 10 seconds and boot system up again
    time.sleep(10)
    GPIO.output(output_channel, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(output_channel, GPIO.LOW)

    # Update success operation count to Flask WebServer
    sio.emit("count_plus_one")


if __name__ == "__main__":
    try:
        sio.connect("http://localhost/")
        sio.wait()
    except ConnectionError:
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
