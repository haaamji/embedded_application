from flask import Flask, render_template
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

pins = {
    10 : {'name':'Yello', 'state':GPIO.LOW },
    11 : {'name':'BLUE', 'state':GPIO.LOW },
    12 : {'name':'RED', 'state':GPIO.LOW }
    }

for pin in pins:
    GPIO.setup(pin , GPIO.OUT)
    GPIO.output(pin , GPIO.LOW)
    
@app.route("/")
def main():
    for pin in pins:
       pins[pin]['state'] = GPIO.input(pin) #읽은 값 state에 저장
    temp = {
        'pins' : pins
        }
    return render_template('app.html', **temp)

@app.route("/<changePin>/<action>")
def action(changePin, action):
    pin = int(changePin)
    
    if action == 'on':
        GPIO.output(pin, GPIO.HIGH)
    if action == 'off':
        GPIO.output(pin, GPIO.LOW)
    
    for pin in pins:
       pins[pin]['state'] = GPIO.input(pin)
    temp = {
        'pins' : pins
        }      
    return render_template('app.html', **temp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)