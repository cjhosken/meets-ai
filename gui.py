from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from pyqtgraph.graphicsItems.ScatterPlotItem import Symbols

class MeetsAiApp(object):
    _theme = "dark"
    _baseColor = "#FFFFFF"
    _headerColor = "#FFFFFF"
    _panelColor = "#FFFFFF"
    _upperPanelColor = "#FFFFFF"
    _textColor = "#FFFFFF"
    _disabledTextColor = "#FFFFFF"
    _activeTextColor = "#FFFFFF" 
    _hoverColor = "rgba(255, 255, 255, 0.1)"

    _font = QtGui.QFont()
    _font.setFamily("Segoe UI")
    _font.setWeight(100)

    _headerShadow = QtGui.QColor(0, 0, 0, 255)
    _shadow = QtGui.QColor(0, 0, 0, 30)
    _glow = QtGui.QColor(0, 180, 255)
    _glowColor = "#00B4FF"
    _glowTransparent = "rgba(0, 180, 255, 128)"

    _logo = QtGui.QIcon()

    _logoIconPath = ""
    _minIconPath = ""
    _closeIconPath = ""
    _bugIconPath = ""
    _themeIconPath = ""
    _startIconPath = ""
    _stopIconPath = ""

    _data = [0, 0]
    _datalabel =[0, 1]

    _pen = pg.mkPen(color=(0, 180, 255), width=1, style=QtCore.Qt.SolidLine)
    _symPen = pg.mkPen(color=(0, 180, 255), width=1, style=QtCore.Qt.SolidLine)
    _symBrush = pg.mkBrush(color=(0, 180, 255, 128))

    def setupUI(self, root):
        self.root = root

        self.root.setObjectName("root")
        self.root.setEnabled(True)
        self.root.resize(900, 800)
        self.root.setMinimumSize(QtCore.QSize(900, 800))
        self.root.setMaximumSize(QtCore.QSize(900, 800))
        self.root.setFont(self._font)
        self.root.setWindowTitle("Meets Ai")

        self.rootWidget = QtWidgets.QWidget(self.root)
        self.rootWidget.setObjectName("rootWidget")
        self.rootWidget.setGeometry(QtCore.QRect(0, 0, 900, 800))

        self.navHeader = QtWidgets.QFrame(self.rootWidget)
        self.navHeader.setObjectName("NavHeader")
        self.navHeader.setGeometry(0, 0, 900, 90)

        self.logo = QtWidgets.QPushButton(self.navHeader)
        self.logo.setObjectName("logo")
        self.logo.setGeometry(QtCore.QRect(0, 0, 100, 100))

        self.title = QtWidgets.QLabel(self.navHeader)
        self.title.setObjectName("title")
        self.title.setText("Meets Ai")
        self.title.setGeometry(QtCore.QRect(100, 15, 200, 60))
        self.title.setFont(self._font)

        self.closeButton = QtWidgets.QPushButton(self.navHeader)
        self.closeButton.setObjectName("closeButton")
        self.closeButton.setGeometry(QtCore.QRect(860, 0, 40, 40))

        self.minButton = QtWidgets.QPushButton(self.navHeader)
        self.minButton.setObjectName("minButton")
        self.minButton.setGeometry(QtCore.QRect(820, 0, 40, 40))

        self.hLine = QtWidgets.QFrame(self.navHeader)
        self.hLine.setObjectName("hLine")
        self.hLine.setGeometry(QtCore.QRect(790, 40, 110, 2))

        self.bugButton = QtWidgets.QPushButton(self.navHeader)
        self.bugButton.setObjectName("bugButton")
        self.bugButton.setGeometry(QtCore.QRect(820, 42, 40, 40))

        self.themeButton = QtWidgets.QPushButton(self.navHeader)
        self.themeButton.setObjectName("themeButton")
        self.themeButton.setGeometry(QtCore.QRect(860, 42, 40, 40))

        self.messagePanel = QtWidgets.QLabel(self.rootWidget)
        self.messagePanel.setObjectName("messagePanel")
        self.messagePanel.setText("")
        self.messagePanel.setGeometry(QtCore.QRect(25, 110, 600, 70))

        self.usersLabel = QtWidgets.QLabel(self.rootWidget)
        self.usersLabel.setObjectName("usersLabel")
        self.usersLabel.setText("0")
        self.usersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.usersLabel.setGeometry(QtCore.QRect(580, 115, 35, 30))

        self.responsePanel = QtWidgets.QLabel(self.rootWidget)
        self.responsePanel.setObjectName("responsePanel")
        self.responsePanel.setText("")
        self.responsePanel.setGeometry(QtCore.QRect(25, 200, 600, 70))

        self.graphPanel = QtWidgets.QFrame(self.rootWidget)
        self.graphPanel.setObjectName("hLine")
        self.graphPanel.setGeometry(QtCore.QRect(25, 290, 600, 380))


        self.graph = pg.PlotWidget(self.graphPanel)
        self.graph.setObjectName("graph")
        self.graph.setGeometry(QtCore.QRect(-15, 20, 560, 360))
        self.graph.getPlotItem().getViewBox().setLimits(xMin=0.0, xMax=10, yMin=0.0, yMax=1)
        self.graph.getPlotItem().getAxis('left').setWidth(50)
        self.graph.getPlotItem().layout.setContentsMargins(25, 25, 25, 25)
        self.graph.getPlotItem().getAxis('bottom').setWidth(500)
        self.graph.getPlotItem().getViewBox().setMouseEnabled(False, False)
        self.graph.getPlotItem().getViewBox().viewRect()

        self.settingsPanel = QtWidgets.QFrame(self.rootWidget)
        self.settingsPanel.setObjectName("settingsPanel")
        self.settingsPanel.setGeometry(QtCore.QRect(25, 690, 600, 80))

        self.settingsLabel = QtWidgets.QLabel(self.settingsPanel)
        self.settingsLabel.setObjectName("settingsLabel")
        self.settingsLabel.setText("Settings")
        self.settingsLabel.setAlignment(QtCore.Qt.AlignVCenter)
        self.settingsLabel.setGeometry(QtCore.QRect(0, 5, 200, 70))

        self.sLine = QtWidgets.QFrame(self.settingsPanel)
        self.sLine.setObjectName("sLine")
        self.sLine.setGeometry(QtCore.QRect(120, 20, 1, 40))

        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self.settingsPanel)
        self.slider.setObjectName("slider")
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setGeometry(QtCore.QRect(150, 0, 360, 80))

        self.window = QtWidgets.QLineEdit(self.settingsPanel)
        self.window.setObjectName("window")
        self.window.setGeometry(QtCore.QRect(520, 12, 65, 54))

        self.sLine2 = QtWidgets.QFrame(self.settingsPanel)
        self.sLine2.setObjectName("sLine2")
        self.sLine2.setGeometry(QtCore.QRect(537, 55, 31, 1))

        self.barPanel = QtWidgets.QFrame(self.rootWidget) 
        self.barPanel.setObjectName("barPanel")
        self.barPanel.setGeometry(QtCore.QRect(650, 110, 225, 455))

        self.bLine = QtWidgets.QFrame(self.barPanel)
        self.bLine.setObjectName("bLine")
        self.bLine.setGeometry(QtCore.QRect(20, 30, 185, 2))

        self.bLabelMax = QtWidgets.QLabel(self.barPanel)
        self.bLabelMax.setObjectName("bLabelMax")
        self.bLabelMax.setText("1.0")
        self.bLabelMax.setGeometry(25, 40, 50, 30)

        self.bar = QtWidgets.QFrame(self.barPanel)
        self.bar.setObjectName("barPanel")
        self.bar.setGeometry(QtCore.QRect(75, 50, 75, 340))

        self.bLine2 = QtWidgets.QFrame(self.barPanel)
        self.bLine2.setObjectName("bLine2")
        self.bLine2.setGeometry(QtCore.QRect(20, 400, 185, 2))

        self.bLabel = QtWidgets.QLabel(self.barPanel)
        self.bLabel.setObjectName("bLabel")
        self.bLabel.setText('Confidence')
        self.bLabel.setGeometry(QtCore.QRect(20, 410, 185, 30))
        self.bLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.bLabelMin = QtWidgets.QLabel(self.barPanel)
        self.bLabelMin.setObjectName("bLabelMin")
        self.bLabelMin.setText("0.0")
        self.bLabelMin.setGeometry(25, 360, 50, 30)

        self.chatButton = QtWidgets.QPushButton(self.rootWidget)   
        self.chatButton.setObjectName("chatButton")
        self.chatButton.setGeometry(QtCore.QRect(650, 580, 112.5, 90))
        self.chatButton.setFont(self._font)
        self.chatButton.setText("Chat")
        self.chatButton.setCheckable(True)
        self.chatButton.clicked.connect(self.updateGlow)

        self.callButton = QtWidgets.QPushButton(self.rootWidget)
        self.callButton.setObjectName("callButton")
        self.callButton.setGeometry(QtCore.QRect(762.5, 580, 112.5, 90))
        self.chatButton.setFont(self._font)
        self.callButton.setCheckable(True)
        self.callButton.setText("Call")
        self.callButton.clicked.connect(self.updateGlow)

        self.appButton = QtWidgets.QPushButton(self.rootWidget)
        self.appButton.setObjectName("appButton")
        self.appButton.setGeometry(QtCore.QRect(650, 690, 225, 80))
        self.appButton.setCheckable(True)
        self.appButton.clicked.connect(self.updateGlow)

        self.getTheme()
        self.updateTheme()

    def toggleTheme(self):
        if self._theme == "dark":
            self._theme = "light"
        elif self._theme == "light":
            self._theme = "dark"

        self.getTheme()
        self.updateTheme()

    def getTheme(self):
        if self._theme == "dark":
            self._baseColor = "#232323"
            self._headerColor = "#1F1F1F"
            self._panelColor = "#2E2E2E"
            self._textColor = "#FFFFFF"
            self._disabledTextColor = "#7D7D7D"
            self._activeTextColor = "#FFFFFF"
            self._logoIconPath = "icons/dark/logo_white.svg"
            self._minIconPath = "icons/dark/minimize_white.svg"
            self._closeIconPath = "icons/dark/close_white.svg"
            self._bugIconPath = "icons/dark/bug_white.svg"
            self._themeIconPath ="icons/dark/light_mode_white.svg"
            self._startIconPath = "icons/dark/start_white.svg"
            self._stopIconPath = "icons/dark/stop_white.svg"
            self._hoverColor = "rgba(255, 255, 255, 0.1)"
            self._headerShadow = QtGui.QColor(0, 0, 0, 255)
            self._shadow = QtGui.QColor(0, 0, 0, 60)
            self._upperPanelColor = "#373737"

        elif self._theme == "light":
            self._baseColor = "#EBEBEB"
            self._headerColor = "#FFFFFF"
            self._panelColor = "#FFFFFF"
            self._textColor = "#000000"
            self._disabledTextColor = "#C0C0C0"
            self._activeTextColor = "#FFFFFF"
            self._logoIconPath = "icons/light/logo_black.svg"
            self._minIconPath = "icons/light/minimize_black.svg"
            self._closeIconPath = "icons/light/close_black.svg"
            self._bugIconPath = "icons/light/bug_black.svg"
            self._themeIconPath ="icons/light/dark_mode_black.svg"
            self._startIconPath = "icons/light/start_black.svg"
            self._stopIconPath = "icons/light/stop_black.svg"
            self._hoverColor = "rgba(0, 0, 0, 0.1)"
            self._shadow = QtGui.QColor(0, 0, 0, 30)
            self._headerShadow = self._shadow
            self._upperPanelColor = "#FFFFFF"
        
        self.updateGlow()
        self.updateDisplays(0.0)

    def updateTheme(self):
        self.root.setWindowIcon(QtGui.QIcon(self._logoIconPath))
        self.rootWidget.setStyleSheet(
            f"background: {self._baseColor};"
            "font-size: 25px;"
        )

        navShadow = QtWidgets.QGraphicsDropShadowEffect(self.navHeader)
        navShadow.setOffset(0, 0)
        navShadow.setBlurRadius(25)
        navShadow.setColor(self._headerShadow)
        self.navHeader.setGraphicsEffect(navShadow)

        self.navHeader.setStyleSheet(
            f"background: {self._headerColor};\n"
            f"border-bottom-left-radius: 50px;"
        )

        logoIcon = QtGui.QIcon()
        logoIcon.addPixmap(QtGui.QPixmap(self._logoIconPath))
        self.logo.setIcon(logoIcon)
        self.logo.setIconSize(QtCore.QSize(100, 100))
        self.logo.setStyleSheet(
            "background: transparent;"
        )

        self.title.setStyleSheet(
            f"color: {self._textColor};\n"
            "font-weight: 100;\n"
            "font-size: 45px;"
        )

        closeIcon = QtGui.QIcon()
        closeIcon.addPixmap(QtGui.QPixmap(self._closeIconPath))
        self.closeButton.setIcon(closeIcon)
        self.closeButton.setIconSize(QtCore.QSize(55, 55))
        self.closeButton.setStyleSheet(
            "#closeButton:hover { \n"
            f"background-color: {self._hoverColor};\n"
            "}"
        )

        minIcon = QtGui.QIcon()
        minIcon.addPixmap(QtGui.QPixmap(self._minIconPath))
        self.minButton.setIcon(minIcon)
        self.minButton.setIconSize(QtCore.QSize(30, 30))
        self.minButton.setStyleSheet(
            "#minButton:hover { \n"
            f"background-color: {self._hoverColor};\n"
            "}"
        )

        self.hLine.setStyleSheet(f"background: {self._textColor};")

        bugIcon = QtGui.QIcon()
        bugIcon.addPixmap(QtGui.QPixmap(self._bugIconPath))
        self.bugButton.setIcon(bugIcon)
        self.bugButton.setIconSize(QtCore.QSize(30, 30))
        self.bugButton.setStyleSheet(
            "#bugButton:hover { \n"
            f"background-color: {self._hoverColor};\n"
            "}"
        )

        themeIcon = QtGui.QIcon()
        themeIcon.addPixmap(QtGui.QPixmap(self._themeIconPath))
        self.themeButton.setIcon(themeIcon)
        self.themeButton.setIconSize(QtCore.QSize(30, 30))
        self.themeButton.setStyleSheet(
            "#themeButton:hover { \n"
            f"background-color: {self._hoverColor};\n"
            "}"
        )

        messageShadow = QtWidgets.QGraphicsDropShadowEffect(self.messagePanel)
        messageShadow.setOffset(0, 0)
        messageShadow.setBlurRadius(15)
        messageShadow.setColor(self._shadow)
        self.messagePanel.setGraphicsEffect(messageShadow)

        self.messagePanel.setStyleSheet(
            f"background: {self._panelColor};\n"
            f"color: {self._textColor};\n"
            "border-radius: 15px;\n"
            "padding: 10px;\n"
            "font-weight: 100;"
        )

        responseShadow = QtWidgets.QGraphicsDropShadowEffect(self.responsePanel)
        responseShadow.setOffset(0, 0)
        responseShadow.setBlurRadius(15)
        responseShadow.setColor(self._shadow)
        self.responsePanel.setGraphicsEffect(responseShadow)

        self.responsePanel.setStyleSheet(
            f"background: {self._panelColor};\n"
            f"color: {self._textColor};\n"
            "border-radius: 15px;\n"
            "padding: 10px;\n"
            "font-weight: 100;"
        )

        self.usersLabel.setStyleSheet(
            f"background: {self._upperPanelColor};\n"
            f"color: {self._textColor};\n"
            "border-radius: 15px;\n"
            "font-weight: 100;\n"
            "font-size: 15px;"
        )

        self.graphPanel.setStyleSheet(
            f"background: {self._panelColor};\n"

            "border-radius: 15px;\n"
        )

        graphShadow = QtWidgets.QGraphicsDropShadowEffect(self.graphPanel)
        graphShadow.setOffset(0, 0)
        graphShadow.setBlurRadius(15)
        graphShadow.setColor(self._shadow)
        self.graphPanel.setGraphicsEffect(graphShadow)

        self.graph.setBackground(None)

        self.settingsPanel.setStyleSheet(
            f"background: {self._panelColor};\n"
            "border-radius: 15px;\n"
            "padding: 15px;\n"
        )

        settingsShadow = QtWidgets.QGraphicsDropShadowEffect(self.settingsPanel)
        settingsShadow.setOffset(0, 0)
        settingsShadow.setBlurRadius(15)
        settingsShadow.setColor(self._shadow)
        self.settingsPanel.setGraphicsEffect(settingsShadow)

        self.settingsLabel.setStyleSheet(
            "font-weight: 100;\n"
            f"color: {self._textColor};\n"
            "background: transparent;"
        )

        self.sLine.setStyleSheet(
            f"background: {self._textColor};\n"
        )

        self.slider.setStyleSheet(
            "#slider:groove {"
            f"""background-color: {self._panelColor}; 
            """
            "}\n"

            "#slider:handle {"
            f"""background: #FFFFFF;
            width: 50px;
            border-radius: 25px;
            border: 1px solid {self._baseColor};
            """
            "}\n"

            "#slider:add-page {"
            f"""
            background: {self._upperPanelColor};
            border-radius: 0;
            border-bottom-right-radius: 25px;
            border-top-right-radius: 25px;
            """
            "}\n"

            "#slider:sub-page {"
            f"""
            background: {self._glowTransparent};
            border: 1px solid {self._glowColor};
            border-radius: 0;
            border-bottom-left-radius: 25px;
            border-top-left-radius: 25px;
            """
            "}\n"
        )

        windowShadow = QtWidgets.QGraphicsDropShadowEffect(self.window)
        windowShadow.setOffset(0, 0)
        windowShadow.setBlurRadius(15)
        windowShadow.setColor(self._shadow)
        self.window.setGraphicsEffect(windowShadow)

        self.window.setStyleSheet(
            f"background: {self._upperPanelColor};\n"
            "border: none;"
            "font-weight: 100;\n"
            f"color: {self._textColor};\n"
        )


        self.sLine2.setStyleSheet(
            f"background: {self._textColor};"
        )

        self.barPanel.setStyleSheet(
            f"background: {self._panelColor};\n"
            "border-radius: 15px;\n" 
        )

        self.bLine.setStyleSheet(
            f"background: {self._textColor};\n"
        )

        self.bLabelMax.setStyleSheet(
            f"color: {self._textColor};\n"
            "font-weight: 100;"
            f"background: transparent;\n"
        )

        barShadow = QtWidgets.QGraphicsDropShadowEffect(self.barPanel)
        barShadow.setOffset(0, 0)
        barShadow.setBlurRadius(15)
        barShadow.setColor(self._shadow)
        self.barPanel.setGraphicsEffect(barShadow)

        self.bar.setStyleSheet(
            f"background: {self._glowTransparent};\n"
            f"border: 1px solid {self._glowColor};\n"
            "border-top-left-radius: 10px;\n"
            "border-top-right-radius: 10px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-bottom-right-radius: 0px;\n"
        )

        barGlow = QtWidgets.QGraphicsDropShadowEffect(self.bar)
        barGlow.setOffset(0, 0)
        barGlow.setBlurRadius(15)
        barGlow.setColor(self._glow)
        self.bar.setGraphicsEffect(barGlow)

        self.bLabelMin.setStyleSheet(
            f"color: {self._textColor};\n"
            "font-weight: 100;\n"
            f"background: transparent;\n"
        )

        self.bLine2.setStyleSheet(
            f"background: {self._textColor};\n"
        )

        self.bLabel.setStyleSheet(
            "text-align: center;\n"
            f"color: {self._textColor};\n"
            "font-weight: 100;\n"
            f"background: transparent;\n"
        )

        self.chatButton.setStyleSheet(
            "#chatButton {"
            f"""border-bottom-left-radius: 25px;
            border-top-left-radius: 25px;\n"""
            f"""background: {self._panelColor};
            color: {self._disabledTextColor};
            font-weight: 100;\n"""
            "font-size: 25px;}\n"

            "#chatButton:hover {"
            f"background: {self._hoverColor};"
            "}\n"

            "#chatButton:checked {"
            f"""border: 1px solid {self._glowColor};
            border-right: none;
            color: {self._activeTextColor};
            background: {self._glowTransparent};"""
            "}\n"

            "#chatButton:checked:hover {"
            f"background: {self._glowColor};"
            "}\n"
        )

        self.callButton.setStyleSheet(
            "#callButton {"
            f"""border-bottom-right-radius: 25px;
            border-top-right-radius: 25px;\n"""
            f"""background: {self._panelColor};
            color: {self._disabledTextColor};
            font-weight: 100;\n"""
            "font-size: 25px;}"

            "#callButton:hover {"
            f"background: {self._hoverColor};"
            "}\n"

            "#callButton:checked {"
            f"""border: 1px solid {self._glowColor};
            border-left: none;
            color: {self._activeTextColor};
            background: {self._glowTransparent};"""
            "}\n"

            "#callButton:checked:hover {"
            f"background: {self._glowColor};"
            "}\n"
        )

        self.appButton.setStyleSheet(
            "#appButton {"
            f"background: {self._panelColor};"
            "border-radius: 40px;}\n"

            "#appButton:hover {"
            f"background: {self._hoverColor};"
            "}\n"

            "#appButton:checked {"
            f"""border: 1px solid {self._glowColor};
            background: {self._glowTransparent};"""
            "}\n"

            "#appButton:checked:hover {"
            f"background: {self._glowColor};"
            "}\n"
        )

    def updateGlow(self):
        if self.appButton.isChecked():
            stopIcon = QtGui.QIcon()
            stopIcon.addPixmap(QtGui.QPixmap(self._stopIconPath))
            self.appButton.setIcon(stopIcon)
            appButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.appButton)
            appButtonGlow.setOffset(0, 0)
            appButtonGlow.setBlurRadius(25)
            appButtonGlow.setColor(self._glow)
            self.appButton.setGraphicsEffect(appButtonGlow)
        else:
            runIcon = QtGui.QIcon()
            runIcon.addPixmap(QtGui.QPixmap(self._startIconPath))
            self.appButton.setIcon(runIcon)
            appButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.appButton)
            appButtonShadow.setOffset(0, 0)
            appButtonShadow.setBlurRadius(25)
            appButtonShadow.setColor(self._shadow)
            self.chatButton.setGraphicsEffect(appButtonShadow)
            self.appButton.setGraphicsEffect(None)
        self.appButton.setIconSize(QtCore.QSize(40, 40))
        
        if self.chatButton.isChecked():
            chatButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.chatButton)
            chatButtonGlow.setOffset(0, 0)
            chatButtonGlow.setBlurRadius(25)
            chatButtonGlow.setColor(self._glow)
            self.chatButton.setGraphicsEffect(chatButtonGlow)
        else:
            chatButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.chatButton)
            chatButtonShadow.setOffset(0, 0)
            chatButtonShadow.setBlurRadius(25)
            chatButtonShadow.setColor(self._shadow)
            self.chatButton.setGraphicsEffect(chatButtonShadow)
        
        if self.callButton.isChecked():
            callButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.callButton)
            callButtonGlow.setOffset(0, 0)
            callButtonGlow.setBlurRadius(25)
            callButtonGlow.setColor(self._glow)
            self.callButton.setGraphicsEffect(callButtonGlow)
        else:
            callButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.callButton)
            callButtonShadow.setOffset(0, 0)
            callButtonShadow.setBlurRadius(25)
            callButtonShadow.setColor(self._shadow)
            self.callButton.setGraphicsEffect(callButtonShadow)

    def updateDisplays(self, c):
        h = 340*c
        y = (50 + 340*(1-c))
        self.bar.setGeometry(QtCore.QRect(75, y, 75, h))
        self.updateGraph(c)

    def updateGraph(self, c):
        self._data = self._data[1:]
        self._data.append(c)

        self._datalabel = self._datalabel[1:]
        self._datalabel.append(self._datalabel[len(self._datalabel) - 1] + 1)
        

        self.graph.plot(self._datalabel, self._data, pen=self._pen, symbol='o', symbolSize=5, symbolPen=self._symPen, symbolBrush=self._symBrush)