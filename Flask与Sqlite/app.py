import os
import sys
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy  # 导入扩展类
app = Flask(__name__)


# 数据库配置
WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控

db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app
'''
模型类要声明继承 db.Model。
每一个类属性（字段）要实例化 db.Column
'''
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份

@app.route('/')
def index():
    user=User.query.first()
    movies=Movie.query.all()
    return render_template("index.html",user=user,movies=movies)
if __name__ == '__main__':
    app.run()