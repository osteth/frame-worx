#!/usr/bin/env python

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4 import QtGui
from flask import Flask,render_template,request
from multiprocessing import Process

portnum = '5555'

def appserver():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index',methods=['GET','POST'])
    def index():
        if request.method == 'GET':
            return render_template('home.html')
        
    @app.route('/page2',methods=['GET','POST'])
    def page2():
        if request.method == 'GET':
            return render_template('page2.html')
    
    @app.route('/page3',methods=['GET','POST'])
    def page3():
        if request.method == 'GET':
            return render_template('page3.html')

    app.run(host='0.0.0.0',port = portnum,debug=False)

def appview():

    view = QtGui.QApplication(sys.argv)
    view.setWindowIcon(QtGui.QIcon('icon.png'))



    web = QWebView()
    web.load(QUrl("http://0.0.0.0:" + portnum))
    web.showMaximized()
    

    sys.exit(view.exec_())

if __name__=='__main__':
     p1 = Process(target = appserver)
     p1.start()
     p2 = Process(target = appview)
     p2.start()