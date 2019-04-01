from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Wellcome to  Flask"

@app.route('/home')
def hello2():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
# 制定url规则

@app.route('/index/<name>') #对所有的index/XX的路径做出响应
def hello3(name):
    return name
if __name__ == '__main__':
    app.run()

