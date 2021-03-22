import sys
from PySide2.QtCore import Qt, Slot
from PySide2.QtGui import QPainter, QFontDatabase, QIcon, QPixmap, QImage, QFont
from PySide2.QtWidgets import (QAction, QApplication, QHeaderView, QHBoxLayout, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget, QGroupBox, QPlainTextEdit, QCheckBox, QToolBar, QAction)
from PySide2.QtCharts import QtCharts
from pyside_material import apply_stylesheet

import allfiles

# class WidgetMainMenu(QWidget):

class ShortcutBlock(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setLayout()

class WidgetMainMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.a = QFontDatabase()
        print(self.a.families())
        print(self.a.writingSystemSample(QFontDatabase.Arabic))

        #focus qeuee
        #Texts
        #Margin
        #child widget access
        #Top Bar
        #multiple windows handling (one open, main close all close, 
        #nice Layouts
        #Rights
        #emoji and other langs (encoding)

        self.MainToolbar = QToolBar()
        self.DonateButton = QPushButton()
        
        self.DonateButton.setStatusTip("FUCKING")
        # self.DonateButton.setBackgroundRole(QIcon(QPixmap(":/Bitcoin.png")))
        self.DonateButton.setFont(QFont("Vazir"))
        self.DonateButton.setMinimumSize(50,100)
        self.DonateButton.setText("FUCckK")

        self.MainToolbar.addWidget(self.DonateButton)

        self.ActiveSessionShortCutGroup = QGroupBox()
        # self.ActiveSessionShortCutGroup
        self.ActiveSessionShortCutGroup.setTitle("Shortcuts")
        self.ActiveSessionShortCutGroupVBox = QVBoxLayout()
        self.ActiveSessionShortCutGroupVBox.setContentsMargins(15,15,15,15)

        def ShortCutVBox(text):
            ShortCutInputButton = QPushButton()
            ShortCutResetButton = QPushButton("Reset")
            ShortCutText = QLabel(text)
            ShortCutResetButton.setMaximumWidth(100)
            ShortCutButtonsHBox = QHBoxLayout()
            ShortCutButtonsHBox.setContentsMargins(10,10,10,10)
            ShortCutButtonsHBox.addWidget(ShortCutInputButton)
            ShortCutButtonsHBox.addWidget(ShortCutResetButton)
            ShortCutBlockVBox = QVBoxLayout()
            ShortCutBlockVBox.addWidget(ShortCutText)
            ShortCutBlockVBox.addLayout(ShortCutButtonsHBox)
            return ShortCutBlockVBox

        CipherShortCutBlockVBox=ShortCutVBox("Enter Ciphering ShortCut (Also Decode in Smart Mode)")
        DecipherShortCutBlockVBox=ShortCutVBox("Enter Deciphering ShortCut (Also Code in Smart Mode - could be left empty)")

        self.ActiveSessionShortCutGroupVBox.addLayout(CipherShortCutBlockVBox)
        self.ActiveSessionShortCutGroupVBox.addLayout(DecipherShortCutBlockVBox)
        self.ActiveSessionShortCutGroup.setLayout(self.ActiveSessionShortCutGroupVBox)

        self.SettingsGroup = QGroupBox()
        self.SettingsGroupVBox = QVBoxLayout()

        self.OnOffDeamonBox = QCheckBox("Start This service and Open Angel Gates to your Privacy, KINDA! :)")
        self.StartUpDeamonBox = QCheckBox("Start CryptoCut Deamon at the System Boot up")
        self.EncryptNotifBox = QCheckBox("Show a Notification After (De/En)crpt of Texts And Show its Successful or Not")
        self.VirtualKeyboardBox = QCheckBox("Open Virtual Keyboard for Keylogger Suspection Situations")
        self.SaftyTweaksBox = QCheckBox("Our Small Tweaks would be Applied on Standard Methods to Make them even better")
        self.SuperSafeModeBox = QCheckBox("Open a Box with Password Input Mode to write text in and Paste in last Focused Region")
        self.RapidModeBox = QCheckBox("Paste Text Back in place and Delete the text")
        self.TrayDeamonBox = QCheckBox("Show Application Icon in Tray for Ease of Access")
        self.SmartModeBox = QCheckBox("Automatically Detect Its a Cipher or a Normal Text and Work with one Shortcut")
        
        self.SettingsGroupVBox.addWidget(self.OnOffDeamonBox)
        self.SettingsGroupVBox.addWidget(self.StartUpDeamonBox)
        self.SettingsGroupVBox.addWidget(self.EncryptNotifBox)
        self.SettingsGroupVBox.addWidget(self.VirtualKeyboardBox)
        self.SettingsGroupVBox.addWidget(self.SaftyTweaksBox)
        self.SettingsGroupVBox.addWidget(self.SuperSafeModeBox)
        self.SettingsGroupVBox.addWidget(self.RapidModeBox)
        self.SettingsGroupVBox.addWidget(self.TrayDeamonBox)
        self.SettingsGroupVBox.addWidget(self.SmartModeBox)

        self.SettingsGroup.setTitle("Settings")
        self.SettingsGroup.setLayout(self.SettingsGroupVBox)

        self.apply = QPushButton("Apply Setting")
        self.reset = QPushButton("Reset to Default")
        self.apply.setMinimumWidth(150)
        self.reset.setMinimumWidth(150)
        self.apply.setMinimumHeight(35)
        self.reset.setMinimumHeight(35)

        self.Container = QHBoxLayout()

        self.Container.addWidget(self.apply)
        self.Container.addWidget(self.reset)
        self.Container.minimumHeightForWidth(20)

        self.Main = QVBoxLayout()
        self.Main.setMargin(10)
        self.Main.addWidget(self.MainToolbar)
        self.Main.addWidget(self.ActiveSessionShortCutGroup)
        self.Main.addWidget(self.SettingsGroup)
        self.TestPlainTextEdit = QPlainTextEdit("Test CryptoCut HERE")
        self.TestPlainTextEdit.setMinimumHeight(200)
        self.Main.addWidget(self.TestPlainTextEdit)
        self.Main.addLayout(self.Container)
        #self.table_view.setSizePolicy(size)
        # Set the layout to the QWidget
        self.setLayout(self.Main)

        # Signals and Slots
        # self.add.clicked.connect(self.add_element)
        # self.quit.clicked.connect(self.quit_application)
        # self.clear.clicked.connect(self.clear_table)
        # self.description.textChanged[str].connect(self.check_disable)
        # self.price.textChanged[str].connect(self.check_disable)

        

    @Slot()
    def add_element(self):
        des = self.description.text()
        price = self.price.text()

        self.table.insertRow(self.items)
        description_item = QTableWidgetItem(des)
        price_item = QTableWidgetItem("{:.2f}".format(float(price)))
        price_item.setTextAlignment(Qt.AlignRight)

        self.table.setItem(self.items, 0, description_item)
        self.table.setItem(self.items, 1, price_item)

        self.description.setText("")
        self.price.setText("")

        self.items += 1

    @Slot()
    def check_disable(self, s):
        if not self.description.text() or not self.price.text():
            self.add.setEnabled(False)
        else:
            self.add.setEnabled(True)

    @Slot()
    def plot_data(self):
        # Get table information
        series = QtCharts.QPieSeries()
        for i in range(self.table.rowCount()):
            text = self.table.item(i, 0).text()
            number = float(self.table.item(i, 1).text())
            series.append(text, number)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.legend().setAlignment(Qt.AlignLeft)
        self.chart_view.setChart(chart)

    @Slot()
    def quit_application(self):
        QApplication.quit()

    def fill_table(self, data=None):
        data = self._data if not data else data
        for desc, price in data.items():
            description_item = QTableWidgetItem(desc)
            price_item = QTableWidgetItem("{:.2f}".format(price))
            price_item.setTextAlignment(Qt.AlignRight)
            self.table.insertRow(self.items)
            self.table.setItem(self.items, 0, description_item)
            self.table.setItem(self.items, 1, price_item)
            self.items += 1

    @Slot()
    def clear_table(self):
        self.table.setRowCount(0)
        self.items = 0


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("CryptoCut - Home")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.setCentralWidget(widget)
        appIcon = QIcon(QPixmap(":/Logo.ico"))
        self.setWindowIcon(appIcon)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)
    # QWidget
    widgetmainmenu = WidgetMainMenu()
    # QMainWindow using QWidget as central widget
    mainwindow = MainWindow(widgetmainmenu)
    mainwindow.show()
    # apply_stylesheet(app, theme='dark_teal.xml')
    # Execute application
    sys.exit(app.exec_())
