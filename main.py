import RPi.GPIO as GPIO
import time


def main():
    time.sleep(10)  # wait 10 seconds for initialize

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
            # Read voltage value from PIN 4
            input_voltage = GPIO.input(input_channel)

            if input_voltage == GPIO.LOW:
                # Detect power off, count once
                count += 1
            else:
                # Reset count to zero if value is GPIO.HIGH
                count = 0

            time.sleep(0.1)

            # Press Power Switch for 0.3 seconds when system is powered off for 3 seconds.
            if count >= 30:
                # Short circuit [PowerSW +] and [PowerSW -] (trigger cold boot)
                GPIO.output(output_channel, GPIO.HIGH)
                # Human push button power button usually between 0.3~0.6 seconds.
                time.sleep(0.3)
                # Release [PowerSW +] and [PowerSW -] short circuit (reset to open circuit)
                GPIO.output(output_channel, GPIO.LOW)
                count = 0
        except KeyboardInterrupt:
            GPIO.cleanup()
            exit(0)


if __name__ == "__main__":
    main()
