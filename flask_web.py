#!/usr/bin/python
# -*- coding: utf8 -*-


from flask import Flask, render_template, request, send_file 
import MySQLdb as mysql
import json
from flask.ext.wtf import Form
from wtforms import  StringField, SubmitField
from wtforms.validators import Required
from flask.ext.bootstrap import Bootstrap


con = mysql.connect(user='root',passwd='212331',host='localhost',db='memory')
con.autocommit(True)
cur = con.cursor()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap=Bootstrap(app)


@app.route('/',methods=['GET','POST'])
def index():
        global NameForm
        name = None
        class NameForm(Form):
             name = StringField('what is your name ?', validators=[Required()])
             submit = SubmitField('Submit')
        form = NameForm()
        if form.validate_on_submit():
           name = form.name.data
           form.name.data = ''
        return  render_template('user.html',form=form,name=name)

@app.route('/jk')
def jk():
    return  render_template('index.html')


tmp_time = 0
@app.route('/data')
def data():
    global tmp_time
    if tmp_time>0:
        sql = 'select * from memory where time>%s' % (tmp_time/1000)
    else:
        sql = 'select * from memory'
    cur.execute(sql)
    arr = []
    for i in cur.fetchall():
        arr.append([i[1]*1000,i[0]])
    if len(arr)>0:
         tmp_time = arr[-1][0]
    return json.dumps(arr)


if __name__=='__main__':
    app.run(host='0.0.0.0',port=9092,debug=True)


