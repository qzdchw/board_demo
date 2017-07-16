import pymysql
import bottle
import json
from bottle import run,get,post,request,static_file,route,template,view
l=0
@route('/login') 
def login_html():
	return static_file('login.html',root='.')
@route('/login/:filename') 
def login_css(filename):
	return static_file('test.css',root='.')
@route('/message/:filename') 
def message_css(filename):
    return static_file('base.css',root='.')
@post('/login')
@view('moban') 
def login_submit():
    name = request.forms.get('username')
    passwd = request.forms.get('password')
    db = pymysql.connect("localhost","root","magina646","board",port=3306,charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM USER "
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
          username = row[0]
          pswd = row[1]
          idname = row[2]
          if name == username and passwd == pswd:
            l=1
            db.close() 
            break
          else:
            continue
        if l==1:
          db = pymysql.connect("localhost","root","magina646","board",port=3306,charset="utf8")
          cursor = db.cursor()
          cursor.execute("SELECT * FROM MESSAGE")
          results = cursor.fetchall()
          tittle=[]
          text=[]
          for row in results:
            tittle.append(row[0])
            text.append(row[1])
            lenlen=len(text)
          #return template("moban",nid=tittle,ntext=text)
          data={'nid':results,'ntext':text,'lenlen':lenlen}
          return data
          db.close() 
        else:
          return "<p>密码错误</p>"
    except:
        return "<p>there is a bug</p>"
@post('/sign_in')
def register_submit():
	return static_file('register.html',root='.')
@post('/register')
def register_submit():

    #name = bottle.request.POST.get('username')
    #passwd = bottle.request.POST.get('password')
    #idname = bottle.request.POST.get('id_name')
    #name = request.forms.get('username')
    #passwd = request.forms.get('password')
    #idname = request.forms.get('id_name')
    #idname = request.forms.getunicode('id_name')
    #idname =idname.encode('utf-8')
    db = pymysql.connect("localhost","root","magina646","board",port=3306,charset="utf8")
    cursor = db.cursor()
    #sql = """INSERT INTO USER(username,password)VALUES ('%s', '%s')" % (name,passwd)"""
    cursor.execute('insert into user values("%s", "%s", "%s")' % (request.forms["username"],request.forms["password"],request.forms.getunicode('id_name')))
    db.commit()
    db.close()
    return "<p>name: %s</p>"%(request.forms.getunicode('id_name'))
    #return static_file('login.html',root='.')
@post('/back')
def register_submit():
	return static_file('login.html',root='.')
#@post('/message')
@route('/message', method='POST')
@view('moban')
def register_submit():
    text = request.forms.getunicode('text')
    tittle = request.forms.getunicode('id_name')
    db = pymysql.connect("localhost","root","magina646","board" ,port=3306,charset="utf8")
    cursor = db.cursor()
    cursor.execute('insert into message values("%s","%s")' % (tittle,text))
    db.commit()
    db.close()
    db = pymysql.connect("localhost","root","magina646","board",port=3306,charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM MESSAGE")
    results = cursor.fetchall()
    tittle=[]
    text=[]
    for row in results:
        tittle.append(row[0])
        text.append(row[1])
        lenlen=len(text)
    data={'nid':results,'ntext':text,'lenlen':lenlen}
    return data
    db.close()
run(host='localhost',port=9999,debug=True) #开启服务，打开debug模式
