#!/usr/bin/env python3
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from PyQt4 import QtGui
from flask import Flask,render_template,request
from multiprocessing import Process

portnum = '5556'

def appserver():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index',methods=['GET','POST'])
    def index():
        if request.method == 'GET':
            return render_template('home.html')

    app.run(host='0.0.0.0',port = portnum,debug=False)

def appview():

    class Guiwindow(QtGui.QWidget):
    
        def __init__(self):
            super(Guiwindow, self).__init__()
        
            self.initUI()
        
            
        def initUI(self):
            
            self.setGeometry(150, 100, 1024, 600)
            self.setWindowTitle('Demonbox Configuration manager')
            self.setWindowIcon(QtGui.QIcon('icon.png'))        
            web = QWebView()
            web.load(QUrl("http://0.0.0.0:" + portnum))
            web.show()
            self.show()
            
        
    app = QtGui.QApplication(sys.argv)
    ex = Guiwindow()
    sys.exit(app.exec_())

if __name__=='__main__':
     p1 = Process(target = appserver)
     p1.start()
     p2 = Process(target = appview)
     p2.start()