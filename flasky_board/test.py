import pymysql
from flask import Flask,render_template,request,redirect,session,flash,jsonify,json,url_for
import json
app = Flask(__name__)
@app.route('/login')
def login_html():
    	return render_template('login.html')
@app.route('/login_test', methods=['POST', 'GET'])
def login_submit():
	name = request.form['username']
	passwd = request.form['password']
	db = pymysql.connect("localhost","root","magina646","board",port=3306,charset="utf8")
	cursor = db.cursor()
	sql = "SELECT * FROM USER "
	#try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
	  username = row[0]
	  pswd = row[1]
	  if name == username and passwd == pswd:
		 
		  return render_template('message.html')
		  db.close() 
	  else:
	  	return "<p>密码错误</p>"
    #except:
        #return "<p>there is a bug</p>"
@app.route('/message_json')
def message_json():
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
  data={'nid':tittle,'ntext':text,'lenlen':lenlen}
  return jsonify(data)
  db.close()
  #return render_template('message.html')
if __name__=="__main__":
    app.debug = True
    app.run()
