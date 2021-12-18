from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUiType
from os import path
import sys
import requests
from fake_useragent import UserAgent




FORM_CLASS,_ = loadUiType(path.join(path.dirname(__file__),"main.ui"))


class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()
        
    
    def Handel_UI(self):
        self.setWindowTitle("Twitter Email Available Checker - By: Mohammad Akour")
        self.setFixedSize(468,450)

    def Handel_Buttons(self):
        self.start.clicked.connect(self.Download)
        self.browse.clicked.connect(self.Handel_Browse)

        
        # الخروج من البرنامج
        self.closed.clicked.connect(self.quitpro)
    # الخروج من البرنامج
    def quitpro():
        sys.exit()
        
   
    def Handel_Browse(self):
        
        save_place = QFileDialog.getOpenFileName(self , caption="فتح ملف الحسابات" )[0]
        self.location.setText(save_place)
        
    def Download(self):
        tagrget = self.location.text()
        if tagrget == '':
                    QMessageBox.warning(self,"خطأ", "لم تقم بإضافة ملف الحسابات !")
        with open(tagrget, 'r') as fp:
            for count, line in enumerate(fp):
                pass
        count += 1
        
        ua = UserAgent()
        userAgent = ua.random
        myfile = open(tagrget, "r")
        myline = myfile.readlines()
        num = 0
        # 
        for x in myline:
            try:
                QApplication.processEvents()
                r = requests.Session()
                url = "https://api.twitter.com/i/users/email_available.json?email="+x
                user_agent = userAgent
                Host = "api.twitter.com"
                Accept = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
                r.headers = {'User-Agent': user_agent}
                r.headers = {'Host': Host}
                r.headers = {'Accept': Accept}
                req = r.get(url).json()
                text = str(req)
                if text.find("'valid': False") == True:
                    self.available.insertPlainText(x)
                    
                else:
                    self.notavailable.insertPlainText(x)
            except ValueError:
                QMessageBox.warning(self,"خطأ !", "قام تويتر بحظر العملية، حاول بعد ساعة من الآن")
                sys.exit()
        QMessageBox.information(self,"نجاح !", "تم الانتهاء من فحص الايميلات بنجاح.")

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()







