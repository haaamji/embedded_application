from flask import Flask, render_template
# flask라이브러리 불러오기 
app = Flask(__name__)
import datetime
# flask객체 만들기
# print(__name__)
@app.route("/<username>")#<변수>
#서버에 루트주소로 들어오면(접근) hello실행
def hello(username = None): 
    #username 값이 없을 때(주소창에 아무것도 안넣을때) none값(초기값)
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M")
    templateData = { #딕셔너리 변수(변수여러개 한번에 처리)
        'name' : username,
        'time' : time
    }
    return render_template('index.html', **templateData) #딕셔너리 변수를 전달


#함수명을 blog라고 수정
@app.route("/about")
def about():
    return render_template('about.html')

#name이 main이면 app실행
if __name__ =="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
