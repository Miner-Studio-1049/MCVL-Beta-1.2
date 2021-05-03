import traceback
from easygui import msgbox
try:
    from ui_MCVL import Ui_MainWindow
    import sys
    import os
    import json
    import time
    import random as r
    import JRRP
    import urllib.request
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
    import Downloader

    Version = ["Beta 1.2","Beta"]
    Updata_log = """1、完善查找功能<br>
TIP：部分功能需<a href="http://www.minerstudio.xyz/community/forum.php?mod=viewthread&tid=13&extra=">安装Everything</a>"""
    Ver = {}
    file = ""
    for path in __file__.split("\\")[:-1]:
        file += str(path)
        file += "\\"

    def SaveJson(self):
        global file
        text = [self.minecrafpathenit.text(),
                self.javapathenit.text(),
                self.MCVer.text(),
                self.PlayerName.text()]
        with open("%sgames.json"    %   file,"r") as f:
            j = json.loads(f.read())
        j["Minecraft_Version_Name"] = text[-2]
        j[".minecraft_Path"] = text[0]
        j["Java_Path"] = text[1]
        j["User_Name"] = text[-1]
        with open("%sgames.json"    %   file,"w",encoding = "utf-8") as f:
            f.write(str(json.dumps(j)))
        

    def Launch(file,self):
        json_file = open(str(file)+"games.json","r")
        game_json = json.loads(json_file.read())       # 获得游戏配置
        json_file.close()
        self.progressBar.setValue(25)
        l_batch_file = open("%sLatestLaunch.bat"    %   file,"r")
        batch = l_batch_file.read()
        l_batch_file.close()     # 获得启动代码
        self.progressBar.setValue(30)
        # 替换字符
        batch = batch.replace(r"%版本名%",game_json["Minecraft_Version_Name"])
        batch = batch.replace(r"%版本路径%",game_json[".minecraft_Path"]+os.sep+game_json["Minecraft_Version_Name"])
        batch = batch.replace(r"%JAVA路径%",game_json["Java_Path"])
        batch = batch.replace(r"%.minecraft文件夹路径%",game_json[".minecraft_Path"])
        batch = batch.replace(r"%用户名%",game_json["User_Name"])
        print(batch)
        self.progressBar.setValue(60)
        # 写入代码
        with open("%sLauncher.bat"  %   file,"w") as f:
            f.write(batch)
        self.progressBar.setValue(100)
        com = os.popen("%sLauncher.bat"   %   file,"r")
        with open(str(int(time.time()))+".log","w") as f:
            f.write(com.read())

    class Dmoe(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super().__init__()
            global file
            self.setupUi(self)
            # 绑定事件
            self.StartGames.clicked.connect(self.launch)       # Tab_1>启动游戏 | 按钮 
            self.F5Json.clicked.connect(self.F5)        # Tab_1>刷新配置 | 按钮
            self.SaveJson.clicked.connect(self.save)        # Tab_1>保存配置 | 按钮
            self.F5GG.clicked.connect(self.F5gg)        # Tab_4>刷新公告 | 按钮
            self.F5RPZ.clicked.connect(self.F5RPZN)         # Tab_4>刷 新 / 重 新 测 试 | 按钮
            self.lookRPZcode.clicked.connect(self.lookcode)      # Tab_4>查看识别码 | 按钮
            self.ZSBLIST.doubleClicked.connect(self.downloadZCB)
            self.KZBLIST.doubleClicked.connect(self.downloadKZB)
            self.OLDLIST.doubleClicked.connect(self.downloadOLD)
            self.mcpathfine.clicked.connect(self.openmcpath)
            self.javapathsearch.clicked.connect(self.jpsf)
            self.mcversionnamefind.clicked.connect(self.mvsf)
            self.show()     # 结束
            Dmoe.init(self)
        def launch(self):
            global file
            self.progressBar.setValue(0)
            SaveJson(self)
            self.progressBar.setValue(10)
            file1 = file
            self.progressBar.setValue(15)
            Launch(file1,self)
        def F5(self):
            global file
            with open("%sgames.json"    %   file,"r",encoding="utf-8") as f:
                pz = json.loads(f.read())
                self.minecrafpathenit.setText(pz[".minecraft_Path"])
                self.javapathenit.setText(pz["Java_Path"])
                self.MCVer.setText(pz["Minecraft_Version_Name"])
                self.PlayerName.setText(pz["User_Name"])
                QMessageBox.information(self,"MCVL提示","配置更新完成")
        def save(self):
            SaveJson(self)
            QMessageBox.information(self,"MCVL提示","配置保存完成")
        def F5gg(self):
            try:
                text = Downloader.get_record("https://minerstudio.oss-cn-shenzhen.aliyuncs.com/MCVL_Info.json")
                self.GGtext.setText(text["Tips"])
            except:
                 e=traceback.format_exc()
                 self.GGtext.setText(e)
        def F5RPZN(self):
            self.lcdNumber.display(JRRP.Jrrp())
        def lookcode(self):
            try:
                code = JRRP.getcode()
            except:
                QMessageBox.critical(self, "读取错误","识别码读取出错！" )
            else:
                QMessageBox.information(self, "MCVL","您的识别码是："+str(code)) 
        def init(self):
            try:
                json = Downloader.get_record("https://mc.mirrors.tmysam.top/mc/game/version_manifest.json")
            except:
                json = Downloader.get_record("https://launchermeta.mojang.com/mc/game/version_manifest.json")
            self.QT_Text.setText(str(json))
            self.ZSB_New_L.setText("最新版本："+str(json['latest']['release']))
            self.KZB_New_L.setText("最新快照："+str(json['latest']['snapshot']))
            Ver_List = json['versions']
            global Ver
            Ver['snapshot'] = []
            Ver['release'] = []
            Ver['old_alpha'] = []
            Ver_name = {}
            Ver_name['snapshot'] = []
            Ver_name['release'] = []
            Ver_name['old_alpha'] = []
            for ver in Ver_List:
                if ver["type"] == 'snapshot':
                    Ver_name['snapshot'] += [ver["id"]]
                    Ver['snapshot'] += [ver]
                elif ver["type"] == 'release':
                    Ver_name['release'] += [ver["id"]]
                    Ver['release'] += [ver]
                elif ver["type"] == "old_alpha":
                     Ver['old_alpha'] += [ver]
                     Ver_name['old_alpha'] += [ver["id"]]
                else:
                    pass
            print(Ver)
            list1 = Ver_name["release"]
            print(list1)
            model1 = QStringListModel()
            model1.setStringList(list1)
            self.ZSBLIST.setModel(model1)

            list2 = Ver_name['snapshot']
            print(list2)
            model2 = QStringListModel()
            model2.setStringList(list2)
            self.KZBLIST.setModel(model2)

            list3 = Ver_name["old_alpha"]
            print(list2)
            model3 = QStringListModel()
            model3.setStringList(list3)
            self.OLDLIST.setModel(model3)

            NewMCVL = Downloader.get_record("https://minerstudio.oss-cn-shenzhen.aliyuncs.com/MCVL_Info.json")
            # print(NewMCVL[Version[1]])
            if NewMCVL["New_Version"][Version[1]]["id"] != Version[0]:
                QMessageBox.information(self,"更新提示","您的MCVL版本已过期，MCVL "+Version[1]+"更新渠道最新版本为："+str(NewMCVL["New_Version"][Version[1]]["id"])+"（发布时间"+str(NewMCVL["New_Version"][Version[1]]["time"])+"），当前版本为："+Version[0])

            self.Name.setText("全名：Miner MineCraft Java Version Launcher For Windows " + Version[1])
            self.Version.setText("版本：" + Version[0])
            self.setWindowTitle("MCVL " + Version[1])
            self.VersionInStart.setText("MCVL " + Version[0])
            self.AboutTitle.setText("MCVL " + Version[1])

            try:
                global file
                import json as j
                with open("%sgames.json"    %   file,"r",encoding="utf-8") as f:
                    pz = j.loads(f.read())
                    self.minecrafpathenit.setText(pz[".minecraft_Path"])
                    self.javapathenit.setText(pz["Java_Path"])
                    self.MCVer.setText(pz["Minecraft_Version_Name"])
                    self.PlayerName.setText(pz["User_Name"])
            except:
                with open("%sgames.json"    %   file,"w",encoding="utf-8") as f:
                    f.write(r'{"Minecraft_Version_Name": "", ".minecraft_Path": "", "Java_Path": "", "User_Name": "MCVL\u7528\u6237"}')

            if True:
                ver = str(JRRP.read_reg(r"Software\\MCVL","Version"))
                # print(ver)
                update_log=f'''MCVL已更新至 <strong>{str(Version[0])}</strong><hr>
    {Updata_log}'''
                if ver != str(Version[0]) and (ver != None):
                    QMessageBox.about(self,"更新提示",update_log)
                    os.popen('reg add HKCU\\Software\\MCVL /v Version /t REG_SZ /d "'+str(Version[0])+'" /f')
                QMessageBox.information(self,"提示","此版本为测试版本，更新提示等服务出错属于正常现象")
                
        def downloadZCB(self,index):
            # print(index.row())
            global Ver
            print(Ver['release'][index.row()])
            Downloader.verinof(Ver['release'][index.row()])
        def downloadKZB(self,index):
            # print(index.row())
            global Ver
            print(Ver['snapshot'][index.row()])
            Downloader.verinof(Ver['snapshot'][index.row()])
        def downloadOLD(self,index):
            # print(index.row())
            global Ver
            print(Ver["old_alpha"][index.row()])
            Downloader.verinof(Ver["old_alpha"][index.row()])
        def openmcpath(self):
            #print(1)
            '''
            dialog = QFileDialog()
            dialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
            # 设置显示文件的模式，这里是详细模式
            dialog.setViewMode(QFileDialog.Detail)
            if dialog.exec_():
                # print(dialog.selectedFiles())
                self.minecrafpathenit.setText(dialog.selectedFiles()[0])
            '''
            try:
                print("正在连接Everything服务器...")
                paths=Downloader.get_record("http://localhost:2442/?search=.minecraft&json=1&path_column=1&sort=path")
                rests=paths["totalResults"]
                if rests==0:
                    QMessageBox.critical(self,"自动查找.minecraft","查找失败，您没有.minecraft文件夹")
                    return
                resls=[]
                for i in paths["results"]:
                    if i["name"]==".minecraft" and i["type"]=="folder":
                        resls.append(i["path"]+"\\.minecraft")
                rests=len(resls)
                c=QInputDialog.getItem(self, "自动查找.minecraft", f'共查找{rests}个.minecraft文件夹\n到请选择一个', resls, 0, False)
                if c[1]:
                    self.minecrafpathenit.setText(c[0])
            except:
                QMessageBox.critical(self,"自动查找.minecraft","查找失败，您的设备可能未安装Everything或者配置有误，请查看安装教程：<a href='http://www.minerstudio.xyz/community/forum.php?mod=viewthread&tid=13&extra='>点击查看</a>")
                dialog = QFileDialog()
                dialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
               # 设置显示文件的模式，这里是详细模式
                dialog.setViewMode(QFileDialog.Detail)
                if dialog.exec_():
                    # print(dialog.selectedFiles())
                    self.minecrafpathenit.setText(dialog.selectedFiles()[0])
        def jpsf(self):
            try:
                print("正在连接Everything服务器...")
                paths=Downloader.get_record("http://localhost:2442/?search=javaw.exe&json=1&path_column=1&sort=path")
                rests=paths["totalResults"]
                if rests==0:
                    QMessageBox.critical(self,"自动查找Java","查找失败，您的设备没有安装Java，请先安装")
                    return
                resls=[]
                for i in paths["results"]:
                    if i["type"]=="file" and i["name"]=="javaw.exe":
                        resls.append(i["path"]+"\\javaw.exe")
                rests=len(resls)
                c=QInputDialog.getItem(self, "自动查找Java", f'共查找{rests}个Java\n到请选择一个Java', resls, 0, False)
                if c[1]:
                    self.javapathenit.setText(c[0])
            except:
                QMessageBox.critical(self,"自动查找Java","查找失败，您的设备可能未安装Everything或者配置有误，请查看安装教程：<a href='http://www.minerstudio.xyz/community/forum.php?mod=viewthread&tid=13&extra='>点击查看</a>")
                dialog = QFileDialog()
                dialog.setFileMode(QFileDialog.FileMode.DirectoryOnly)
               # 设置显示文件的模式，这里是详细模式
                dialog.setViewMode(QFileDialog.Detail)
                if dialog.exec_():
                    # print(dialog.selectedFiles())
                    self.javapathenit.setText(dialog.selectedFiles()[0])
        def mvsf(self):
            try:
                path=self.minecrafpathenit.text()
                ps=os.listdir(path+"\\versions")
                c=QInputDialog.getItem(self, "自动查找MC版本", f'共查找{len(ps)}个MC版本\n到请选择一个版本', ps, 0, False)
                if c[1]:
                    self.MCVer.setText(c[0])
            except:
                QMessageBox.critical(self,"自动查找MC版本","无效的文件夹路径或文件夹中没有MC版本")
    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = Dmoe()
        sys.exit(app.exec_())
except SystemExit:
    pass
except:
    e=traceback.format_exc()
    msgbox(msg=f"""    MCVL遇到了一些问题，以停止运行。您可以手动检查MCVL版本或将一下代码通过反馈至MCVL开发组（相关负责人：小邓学编程）。
终止信息：
    {str(e)}""")
    exit()
