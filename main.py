from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.gui import MeetsAiApp
from selenium import webdriver
import webbrowser
import ctypes
import sys
import threading
import chat

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
        self._running = False

    def run(self):
        if self.app.appButton.isChecked():
            self._driver = self.connectBrowser()
            if self._driver is not None:
                self._tabid = self.app.window.text()
                if len(self._tabid) <= 0 or not self._tabid.isdigit():
                    self._tabid = 1
                else:
                    self._tabid = int(self._tabid)
                
                if self._thread is None:
                    self._thread = threading.Thread(target=self.chat)

                self._thread.start()
                self._running = True
            else:
                print("ERROR")
        else:
            if self._running:
                self._thread.join()
                self._thread = None
                self._running = False

    def connectBrowser(self):
            try:
                d = open("data.txt").readlines(0)
                driver = webdriver.Remote(command_executor=d[0][:-1])
                driver.close()
                driver.session_id = d[1]
                return driver
            except Exception as e:
                self.app.appButton.setChecked(False)
                self.app.updateEffects()
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

    def reportBug(self):
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
        if self._running:
            self.app.appButton.setChecked(False)
            self._thread.join()
            self._thread = None
            self._running = False
            
        QCoreApplication.instance().quit()

def main():
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('christopherhosken.meetsai.app.2' )
    app = QApplication(sys.argv)
    window = MeetsAi()
    window.setWindowFlags(Qt.FramelessWindowHint)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()