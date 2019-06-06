import RPi.GPIO as GPIO
import time
import socketio
from socketio.exceptions import ConnectionError


def main():
    sio = None

    GPIO.setmode(GPIO.BOARD)

    # Setup PowerLED + input listener on PIN 3
    input_channel = 3
    GPIO.setup(input_channel, GPIO.IN)

    # Setup PowerSwitch RELAY control on PIN 12
    output_channel = 12
    GPIO.setup(output_channel, GPIO.OUT, initial=GPIO.LOW)

    count = 0

    while True:
        try:
            # Read voltage value from PIN 3
            input_voltage = GPIO.input(input_channel)

            if input_voltage == GPIO.HIGH:
                # Detect power on, count once
                count += 1
            else:
                # Reset count to zero if value is GPIO.LOW
                count = 0

            time.sleep(0.1)

            # Press Power Switch for 3 seconds when system is power on for 120 seconds.
            if count > 1200:
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
                if sio:
                    sio.emit("count_plus_one")
                else:
                    try:
                        sio = socketio.Client()
                        sio.connect("http://localhost/")
                        sio.emit("count_plus_one")
                    except ConnectionError:
                        sio = None
                count = 0
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit(0)


if __name__ == "__main__":
    main()
