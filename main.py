from PyQt5 import QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from gui import MeetsAiApp
import sys
import webbrowser
import ctypes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import threading
import config
import chat

myappid = 'christopherhosken.meetsai.app.2' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
class MeetsAi(QMainWindow, MeetsAiApp):
    def __init__(self):
        super(MeetsAi, self).__init__()
        self.app = MeetsAiApp()
        self.app.setupUI(self)
        self.app.navHeader.mouseMoveEvent = self.moveWindow
        self.app.closeButton.clicked.connect(self.closeApp)
        self.app.minButton.clicked.connect(self.showMinimized)
        self.app.bugButton.clicked.connect(self.reportBug)
        self.app.themeButton.clicked.connect(self.app.toggleTheme)
        self.app.appButton.clicked.connect(self.run)
        self.app.window.textChanged.connect(self.limitText)

        self._thread = None
        self._driver = None

    def run(self):
        if self.app.appButton.isChecked():
            self._driver = self.connectBrowser()
            if self._driver == None:
                print("ERROR")
            else:
                self._tabid = self.app.window.text()
                if len(self._tabid) <= 0 or not self._tabid.isdigit():
                    self._tabid = 1
                else:
                    self._tabid = int(self._tabid)
                
                if self._thread is not None:
                    self._thread.start()
                else:
                    self._thread = threading.Thread(target=self.chat)
                    self._thread.start()
        else:
            if self._thread is not None:
                self._thread.join()
                self._thread = None
            

    def connectBrowser(self):
            try:
                d = open("data.txt").readlines(0)
                driver = webdriver.Remote(command_executor=d[0][:-1])
                driver.close()
                driver.session_id = d[1]
                return driver
            except Exception as e:
                self.app.appButton.setChecked = False
                print(e)
                print("ERROR: Try running the browser.py file first.")
                return None

    def chat(self):
        while self.app.appButton.isChecked():
            callActive = self.app.callButton.isChecked()
            chatActive = self.app.chatButton.isChecked()
            t = self.app.slider.value() / 100

            updated, msg, res, conf, users = chat.chat(self._driver, self._tabid, callActive, chatActive, t)

            if updated:
                self.updateUI(msg, res, conf, users)

    def updateUI(self, msg, res, conf, users):
        self.app.updateDisplays(conf)
        self.app.messagePanel.setText(msg)
        self.app.responsePanel.setText(res)
        self.app.usersLabel.setText(users)

    def reportBug():
        webbrowser.open("https://github.com/Christopher-Hosken/meets-ai/issues")

    def limitText(self):
        text = self.app.window.text()
        if len(text) > 2:
            text = text[:2]
            self.app.window.setText(text)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def moveWindow(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def closeApp(self):
        self.app.appButton.setChecked(False)
        if self._thread is not None:
            self._thread.join()
            self._thread = None

        QCoreApplication.instance().quit()

def main():
    app = QApplication(sys.argv)
    window = MeetsAi()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()