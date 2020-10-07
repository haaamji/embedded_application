from flask import Flask, render_template
import datetime
import RPi.GPIO as GPIO
# flask라이브러리 불러오기 
app = Flask(__name__)

#BCM모드
GPIO.setmode(GPIO.BCM)
# flask객체 만들기
# print(__name__)
@app.route("/")#<변수>
#서버에 루트주소로 들어오면(접근) hello실행
def hello(): 
    #username 값이 없을 때(주소창에 아무것도 안넣을때) none값(초기값)
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    templateData = { #딕셔너리 변수(변수여러개 한번에 처리)
        'title' : "안녕하세요!",
        'time' : time
    }
    return render_template('main.html', **templateData) #딕셔너리 변수를 전달


@app.route("/<pin>")#<핀번호>
def readPin():
    try:
        GPIO.setup(int(pin), GPIO.IN)
        if GPIO.input(int(pin)) == True:
            response = "핀 넘버 "+pin+"은 HIGH"
        else:
            response = "핀 넘버" + pin+ "은 LOW"
    except:
        response = "핀을 읽는 데 문제가 있음" +pin+ "번 핀"
    templateData ={
        'pin' :"핀 상태" + pin,
        'response' : response
    } 
    return render_template('pin.html', **templateData)
#name이 main이면 app실행
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
