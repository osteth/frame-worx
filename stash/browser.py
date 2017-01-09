
import sys
from PyQt4 import QtGui
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *

portnum = '5554'

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(150, 100, 1024, 600)
        self.setWindowTitle('Demonbox Configuration manager')
        self.setWindowIcon(QtGui.QIcon('icon.png'))        
        web = QWebView()
        web.load(QUrl("http://0.0.0.0:1000"))
        web.show()
        self.show()
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    