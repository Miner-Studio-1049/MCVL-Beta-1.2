import urllib.request
import json
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from ui_verinof import *
import sys
import urllib.request

J = None

def get_record(url):
    headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    req=urllib.request.Request(url=url,headers=headers) 
    resp = urllib.request.urlopen(req)
    ele_json = json.loads(resp.read())
    return ele_json

class Demo(QDialog, Ui_Verinof):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Server.clicked.connect(self.downserver)
        self.down.clicked.connect(self.download)
        self.show()
        Demo.init(self)
    def init(self):
        global J
        self.Ver.setText("版本："+J["id"])
        self.label.setText("类型："+J["type"])
        self.Time.setText("发布时间："+J['releaseTime'])
    def downserver(self):
        global J
        try:
            verjson = get_record(J["url"])
        except:
            QMessageBox.critical(self,"Download Error","找不到此版本的服务端文件")
            return None
        try:
            req = urllib.request.urlopen(str(verjson["downloads"]["server"]["url"]))
            with open(J["id"] + "_server.jar","wb") as f:
                f.write(req.read())
            QMessageBox.information(self, "MCVL","下载完成！")
        except:
            QMessageBox.critical(self,"Download Error","下载失败")
            return None
    def download(self):
        global J
        verjson = get_record(J["url"])
        req = urllib.request.urlopen(str(verjson["downloads"]["client"]["url"]))
        with open(J["id"]+".jar","wb") as f:
            f.write(req.read())
        QMessageBox.information(self, "MCVL","下载完成！") 
def verinof(Json):
    global J
    J = Json
    #app = QApplication(sys.argv)
    window = Demo()  #注意这里你打错了
    window.exec_()
