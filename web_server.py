from flask import Flask, render_template_string, request
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

HTML = '''
<html>
<body>
  <h1>Control LED</h1>
  <form action="/on" method="post">
    <button type="submit">Turn LED On</button>
  </form>
  <form action="/off" method="post">
    <button type="submit">Turn LED Off</button>
  </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/on', methods=['POST'])
def led_on():
    GPIO.output(17, GPIO.HIGH)
    return index()

@app.route('/off', methods=['POST'])
def led_off():
    GPIO.output(17, GPIO.LOW)
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
