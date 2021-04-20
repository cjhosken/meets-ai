from PyQt5 import QtCore, QtGui
import pyqtgraph as pg

class Theme:
    def __init__(self) -> None:
        self._font = QtGui.QFont()
        self._font.setFamily("Segoe UI")
        self._fontTitleSize = "45px"
        self._fontTextSize = "24px"
        self._fontSmallTextSize = "15px"
        self._fontWeight = "100"

        self._theme = ""
        self._base = ""
        self._panel = ""
        self._subpanel = ""
        self._primary = ""
        self._primaryHighlight = ""
        self._accent = ""
        self._accentDim = ""
        self._hover = ""
        self._hoverAccent = ""
        self._shadow = ""

        self._logoIcon = ""
        self._minimizeIcon = ""
        self._closeIcon = ""
        self._bugIcon = ""
        self._modeIcon = ""
        self._startIcon = ""
        self._stopIcon = ""

        self.getGraphTheme()

    def getGraphTheme(self):
        self._gPen = pg.mkPen(color=self._accent, width=1, style=QtCore.Qt.SolidLine)
        self._pPen = pg.mkPen(color=self._accent, width=1, style=QtCore.Qt.SolidLine)
        self._pBrush = pg.mkBrush(color=self._accentDim)

class DarkTheme(Theme):
    def __init__(self):
        self._font = QtGui.QFont()
        self._font.setFamily("Segoe UI")
        self._fontTitleSize = "45px"
        self._fontTextSize = "24px"
        self._fontSmallTextSize = "15px"
        self._fontWeight = "100"

        self._theme = "dark"
        self._base = "#1e1e1e"
        self._panel = "#2d2d2d"
        self._subpanel = "#373737"
        self._primary = "#ffffff"
        self._primaryHighlight = "#ffffff"
        self._accent = "#00b4ff"
        self._accentDim = "#15658c"
        self._hover = "#858585"
        self._hoverAccent = "#a82121"
        self._shadow = "#0f0f0f"

        self._logoIcon = QtGui.QIcon("ui/icons/dark/logo_white.svg")
        self._minimizeIcon = QtGui.QIcon("ui/icons/dark/minimize_white.svg")
        self._closeIcon = QtGui.QIcon("ui/icons/dark/close_white.svg")
        self._bugIcon = QtGui.QIcon("ui/icons/dark/bug_white.svg")
        self._modeIcon = QtGui.QIcon("ui/icons/dark/light_mode_white.svg")
        self._startIcon = QtGui.QIcon("ui/icons/dark/start_white.svg")
        self._stopIcon = QtGui.QIcon("ui/icons/dark/stop_white.svg")

        self.getGraphTheme()

class LightTheme(Theme):
    def __init__(self):
        self._font = QtGui.QFont()
        self._font.setFamily("Segoe UI")
        self._fontTitleSize = "45px"
        self._fontTextSize = "24px"
        self._fontSmallTextSize = "15px"
        self._fontWeight = "100"

        self._theme = "light"
        self._base = "#ffffff"
        self._panel = "#ffffff"
        self._subpanel = "#e0e0e0"
        self._primary = "#1e1e1e"
        self._primaryHighlight = "#ffffff"
        self._accent = "#00b4ff"
        self._accentDim = "#52bef1"
        self._hover = "#cccccc"
        self._hoverAccent = "#bf1c2a"
        self._shadow = "#bfbfbf"

        self._logoIcon = QtGui.QIcon("ui/icons/light/logo_black.svg")
        self._minimizeIcon = QtGui.QIcon("ui/icons/light/minimize_black.svg")
        self._closeIcon = QtGui.QIcon("ui/icons/light/close_black.svg")
        self._bugIcon = QtGui.QIcon("ui/icons/light/bug_black.svg")
        self._modeIcon = QtGui.QIcon("ui/icons/light/dark_mode_black.svg")
        self._startIcon = QtGui.QIcon("ui/icons/light/start_black.svg")
        self._stopIcon = QtGui.QIcon("ui/icons/light/stop_black.svg")

        self.getGraphTheme()