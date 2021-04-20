from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import ui.theme as theme
import config

class MeetsAiApp(object):
    if config._defaultTheme == "dark":
        _theme = theme.DarkTheme()
    else:
        _theme = theme.LightTheme()

    _graphData = [0, 0]
    _graphDataLabel = [0, 1]

    def setupUI(self, root):
        self.root = root

        self.root.setObjectName("root")
        self.root.setEnabled(True)
        self.root.resize(900, 800)
        self.root.setMinimumSize(QtCore.QSize(900, 800))
        self.root.setMaximumSize(QtCore.QSize(900, 800))
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
        self.chatButton.setText("Chat")
        self.chatButton.setCheckable(True)
        self.chatButton.clicked.connect(self.updateEffects)

        self.callButton = QtWidgets.QPushButton(self.rootWidget)
        self.callButton.setObjectName("callButton")
        self.callButton.setGeometry(QtCore.QRect(762.5, 580, 112.5, 90))
        self.callButton.setCheckable(True)
        self.callButton.setText("Call")
        self.callButton.clicked.connect(self.updateEffects)

        self.appButton = QtWidgets.QPushButton(self.rootWidget)
        self.appButton.setObjectName("appButton")
        self.appButton.setGeometry(QtCore.QRect(650, 690, 225, 80))
        self.appButton.setCheckable(True)
        self.appButton.clicked.connect(self.updateEffects)

        self.updateTheme()
        self.updateEffects()
        self.updateDisplays(0.0)

    def toggleTheme(self):
        if self._theme._theme == "dark":
            self._theme = theme.LightTheme()
        else:
            self._theme = theme.DarkTheme()

        self.updateTheme()
        self.updateEffects()

    def updateTheme(self):
        self.root.setWindowIcon(self._theme._logoIcon)
        self.root.setFont(self._theme._font)
        self.rootWidget.setStyleSheet(
            f"background: {self._theme._base};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        navShadow = QtWidgets.QGraphicsDropShadowEffect(self.navHeader)
        navShadow.setOffset(0, 0)
        navShadow.setBlurRadius(25)
        navShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.navHeader.setGraphicsEffect(navShadow)

        self.navHeader.setStyleSheet(
            f"background: {self._theme._base};\n"
            f"border-bottom-left-radius: 50px;"
        )

        self.logo.setIcon(self._theme._logoIcon)
        self.logo.setIconSize(QtCore.QSize(100, 100))
        self.logo.setStyleSheet(
            "background: transparent;"
        )

        self.title.setFont(self._theme._font)
        self.title.setStyleSheet(
            f"color: {self._theme._primary}; \n"
            f"font-size: {self._theme._fontTitleSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.closeButton.setIcon(self._theme._closeIcon)
        self.closeButton.setIconSize(QtCore.QSize(55, 55))
        self.closeButton.setStyleSheet(
            "#closeButton:hover { \n"
            f"background-color: {self._theme._hoverAccent};\n"
            "}"
        )

        self.minButton.setIcon(self._theme._minimizeIcon)
        self.minButton.setIconSize(QtCore.QSize(30, 30))
        self.minButton.setStyleSheet(
            "#minButton:hover { \n"
            f"background-color: {self._theme._hover};\n"
            "}"
        )

        self.hLine.setStyleSheet(f"background: {self._theme._primary};")

        self.bugButton.setIcon(self._theme._bugIcon)
        self.bugButton.setIconSize(QtCore.QSize(30, 30))
        self.bugButton.setStyleSheet(
            "#bugButton:hover { \n"
            f"background-color: {self._theme._hover};\n"
            "}"
        )

        self.themeButton.setIcon(self._theme._modeIcon)
        self.themeButton.setIconSize(QtCore.QSize(30, 30))
        self.themeButton.setStyleSheet(
            "#themeButton:hover { \n"
            f"background-color: {self._theme._hover};\n"
            "}"
        )

        messageShadow = QtWidgets.QGraphicsDropShadowEffect(self.messagePanel)
        messageShadow.setOffset(0, 0)
        messageShadow.setBlurRadius(15)
        messageShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.messagePanel.setGraphicsEffect(messageShadow)
        self.messagePanel.setFont(self._theme._font)
        self.messagePanel.setStyleSheet(
            f"background: {self._theme._panel};\n"
            f"color: {self._theme._primary};\n"
            "border-radius: 15px;\n"
            "padding: 10px;\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        responseShadow = QtWidgets.QGraphicsDropShadowEffect(self.responsePanel)
        responseShadow.setOffset(0, 0)
        responseShadow.setBlurRadius(15)
        responseShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.responsePanel.setGraphicsEffect(responseShadow)
        self.responsePanel.setFont(self._theme._font)
        self.responsePanel.setStyleSheet(
            f"background: {self._theme._panel};\n"
            f"color: {self._theme._primary};\n"
            "border-radius: 15px;\n"
            "padding: 10px;\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.usersLabel.setFont(self._theme._font)
        self.usersLabel.setStyleSheet(
            f"background: {self._theme._subpanel};\n"
            f"color: {self._theme._primary};\n"
            "border-radius: 15px;\n"
            f"font-size: {self._theme._fontSmallTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.graphPanel.setStyleSheet(
            f"background: {self._theme._panel};\n"
            "border-radius: 15px;"
        )

        graphShadow = QtWidgets.QGraphicsDropShadowEffect(self.graphPanel)
        graphShadow.setOffset(0, 0)
        graphShadow.setBlurRadius(15)
        graphShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.graphPanel.setGraphicsEffect(graphShadow)

        self.graph.setBackground(None)

        self.settingsPanel.setStyleSheet(
            f"background: {self._theme._panel};\n"
            f"color: {self._theme._primary};\n"
            "border-radius: 15px;\n"
            "padding: 15px;\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        settingsShadow = QtWidgets.QGraphicsDropShadowEffect(self.settingsPanel)
        settingsShadow.setOffset(0, 0)
        settingsShadow.setBlurRadius(15)
        settingsShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.settingsPanel.setGraphicsEffect(settingsShadow)

        self.settingsLabel.setFont(self._theme._font)
        self.settingsLabel.setStyleSheet(
            "background: transparent;\n"
            f"color: {self._theme._primary};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.sLine.setStyleSheet(
            f"background: {self._theme._primary};"
        )

        self.slider.setStyleSheet(
            "#slider:groove { \n"
            f"background-color: {self._theme._panel};"
            "}\n"

            "#slider:handle { \n"
            f"background: {self._theme._primaryHighlight};\n"
            "width: 50px;\n"
            "border-radius: 25px;\n"
            f"border: 1px solid {self._theme._hover};"
            "}\n"

            "#slider:add-page { \n"
            f"background: {self._theme._subpanel};\n"
            "border-radius: 0;\n"
            "border-bottom-right-radius: 25px;\n"
            "border-top-right-radius: 25px;\n"
            "}\n"

            "#slider:sub-page { \n"
            f"background: {self._theme._accentDim};\n"
            f"border: 1px solid {self._theme._accent};\n"
            "border-radius: 0;\n"
            "border-bottom-left-radius: 25px;\n"
            "border-top-left-radius: 25px;\n"
            "}"
        )

        self.window.setFont(self._theme._font)
        self.window.setStyleSheet(
            f"background: {self._theme._subpanel};\n"
            "border: none;\n"
            f"color: {self._theme._primary};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.sLine2.setStyleSheet(
            f"background: {self._theme._primary};"
        )

        self.barPanel.setStyleSheet(
            f"background: {self._theme._panel};\n"
            "border-radius: 15px;" 
        )

        self.bLine.setStyleSheet(
            f"background: {self._theme._primary};"
        )

        self.bLabelMax.setFont(self._theme._font)
        self.bLabelMax.setStyleSheet(
            f"background: transparent;\n"
            f"color: {self._theme._primary};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        barShadow = QtWidgets.QGraphicsDropShadowEffect(self.barPanel)
        barShadow.setOffset(0, 0)
        barShadow.setBlurRadius(15)
        barShadow.setColor(QtGui.QColor(self._theme._shadow))
        self.barPanel.setGraphicsEffect(barShadow)

        self.bar.setStyleSheet(
            f"background: {self._theme._accentDim};\n"
            f"border: 1px solid {self._theme._accent};\n"
            "border-top-left-radius: 10px;\n"
            "border-top-right-radius: 10px;\n"
            "border-bottom-left-radius: 0px;\n"
            "border-bottom-right-radius: 0px;"
        )
        self.bLabelMin.setFont(self._theme._font)
        self.bLabelMin.setStyleSheet(
            "background: transparent;\n"
            f"color: {self._theme._primary};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.bLine2.setStyleSheet(
            f"background: {self._theme._primary};\n"
        )

        self.bLabel.setFont(self._theme._font)
        self.bLabel.setStyleSheet(
            "background: transparent;\n"
            f"color: {self._theme._primary};\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};"
        )

        self.chatButton.setFont(self._theme._font)
        self.chatButton.setStyleSheet(
            "#chatButton { \n"
            f"background: {self._theme._panel};\n"
            f"color: {self._theme._hover};\n"
            "border-bottom-left-radius: 25px;\n"
            "border-top-left-radius: 25px;\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};\n"
            "}\n"

            "#chatButton:hover { \n"
            f"background: {self._theme._hover}; \n"
            "}\n"

            "#chatButton:checked { \n"
            f"background: {self._theme._accentDim};\n"
            f"color: {self._theme._primaryHighlight};\n"
            f"border: 1px solid {self._theme._accent};\n"
            "border-right: none;\n"
            "}\n"

            "#chatButton:checked:hover { \n"
            f"background: {self._theme._accent};\n"
            "}"
        )

        self.callButton.setFont(self._theme._font)
        self.callButton.setStyleSheet(
            "#callButton { \n"
            f"background: {self._theme._panel};\n"
            f"color: {self._theme._hover};\n"
            "border-bottom-right-radius: 25px;\n"
            "border-top-right-radius: 25px;\n"
            f"font-size: {self._theme._fontTextSize};\n"
            f"font-weight: {self._theme._fontWeight};\n"
            "}\n"

            "#callButton:hover { \n"
            f"background: {self._theme._hover}; \n"
            "}\n"

            "#callButton:checked { \n"
            f"background: {self._theme._accentDim};\n"
            f"color: {self._theme._primaryHighlight};\n"
            f"border: 1px solid {self._theme._accent};\n"
            "border-right: none;\n"
            "}\n"

            "#callButton:checked:hover { \n"
            f"background: {self._theme._accent};\n"
            "}"
        )

        self.appButton.setStyleSheet(
            "#appButton { \n"
            f"background: {self._theme._panel};\n"
            "border-radius: 40px;\n"
            "}\n"

            "#appButton:hover {"
            f"background: {self._theme._hover};\n"
            "}\n"

            "#appButton:checked { \n"
            f"border: 1px solid {self._theme._accent};\n"
            f"background: {self._theme._accentDim};\n"
            "}\n"

            "#appButton:checked:hover { \n"
            f"background: {self._theme._accent};\n"
            "}"
        )

    def updateEffects(self):
        if self.appButton.isChecked():
            self.appButton.setIcon(self._theme._stopIcon)
            appButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.appButton)
            appButtonGlow.setOffset(0, 0)
            appButtonGlow.setBlurRadius(25)
            appButtonGlow.setColor(QtGui.QColor(self._theme._accent))
            self.appButton.setGraphicsEffect(appButtonGlow)
        else:
            self.appButton.setIcon(self._theme._startIcon)
            appButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.appButton)
            appButtonShadow.setOffset(0, 0)
            appButtonShadow.setBlurRadius(25)
            appButtonShadow.setColor(QtGui.QColor(self._theme._shadow))
            self.appButton.setGraphicsEffect(appButtonShadow)
        self.appButton.setIconSize(QtCore.QSize(40, 40))
        
        if self.chatButton.isChecked():
            chatButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.chatButton)
            chatButtonGlow.setOffset(0, 0)
            chatButtonGlow.setBlurRadius(25)
            chatButtonGlow.setColor(QtGui.QColor(self._theme._accent))
            self.chatButton.setFont(self._theme._font)
            self.chatButton.setGraphicsEffect(chatButtonGlow)
        else:
            chatButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.chatButton)
            chatButtonShadow.setOffset(0, 0)
            chatButtonShadow.setBlurRadius(25)
            chatButtonShadow.setColor(QtGui.QColor(self._theme._shadow))
            self.chatButton.setFont(self._theme._font)
            self.chatButton.setGraphicsEffect(chatButtonShadow)
        
        if self.callButton.isChecked():
            callButtonGlow = QtWidgets.QGraphicsDropShadowEffect(self.callButton)
            callButtonGlow.setOffset(0, 0)
            callButtonGlow.setBlurRadius(25)
            callButtonGlow.setColor(QtGui.QColor(self._theme._accent))
            self.callButton.setFont(self._theme._font)
            self.callButton.setGraphicsEffect(callButtonGlow)
        else:
            callButtonShadow = QtWidgets.QGraphicsDropShadowEffect(self.callButton)
            callButtonShadow.setOffset(0, 0)
            callButtonShadow.setBlurRadius(25)
            callButtonShadow.setColor(QtGui.QColor(self._theme._shadow))
            self.callButton.setFont(self._theme._font)
            self.callButton.setGraphicsEffect(callButtonShadow)

    def updateDisplays(self, c):
        y = 50 + 340 * (1 - c)
        self.bar.setGeometry(QtCore.QRect(75, y, 75, (340 * c)))
        self.updateGraph(c)

    def updateGraph(self, c):
        self._graphData = self._graphData[1:]
        self._graphData.append(c)

        self._graphDataLabel = self._graphDataLabel[1:]
        self._graphDataLabel.append(self._graphDataLabel[len(self._graphDataLabel) - 1] + 1)
        
        self.graph.plot(self._graphDataLabel, self._graphData, pen=self._theme._gPen, symbol='o', symbolSize=5, symbolPen=self._theme._pPen, symbolBrush=self._theme._pBrush)