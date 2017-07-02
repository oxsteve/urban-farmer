import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Some constants
ON = GPIO.LOW
OFF = GPIO.HIGH

# All pumps
wateringPumps = {
    "tomato": {"name": "Tomaten", "pin": 17, "state": OFF}
}

# Set each pin as an output and make it low:
for pump in wateringPumps:
    pin = wateringPumps[pump]["pin"]
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, OFF)


@app.route("/")
def main():
    return render_template('main.html')


@app.route("/watering/<pump>/<action>")
def watering(pump, action):
    # Convert the pin from the URL into an integer:
    changePin = wateringPumps[pump]["pin"]
    name = wateringPumps[pump]["name"]
    if action == "on":
        GPIO.output(changePin, ON)
        wateringPumps[pump]["state"] = ON
        return "Pumpe fuer " + name + " eingeschaltet."
    if action == "off":
        GPIO.output(changePin, OFF)
        wateringPumps[pump]["state"] = OFF
        return "Pumpe fuer " + name + " ausgeschaltet."
    if action == "status":
        return str(wateringPumps[pump]["state"])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
