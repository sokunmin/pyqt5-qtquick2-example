# This Python file uses the following encoding: utf-8
import sys
import os
from PyQt5.QtQuick import QQuickView
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSignal, pyqtSlot, pyqtProperty
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
from res import resources  # load resources built by pyside2-rcc
from utils.network import ReadIpThread


def get_resource_path(rel_path=''):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel_path)
    return os.path.join(os.path.abspath("."), rel_path)


class NexApplication(QQmlApplicationEngine):

    def __init__(self, parent=None):
        super().__init__(parent)
        #    engine.load(QUrl('qrc:/res/qml/main.qml'))
        qmlFilePath = os.path.join(get_resource_path(os.path.dirname(__file__)), "res", "qml", "window.qml")
        print('> QML file = ', qmlFilePath)
        qmlFile = QUrl.fromLocalFile(qmlFilePath)
        self.load(qmlFile)
        window = self.rootObjects()[0]
        self.ipButton = window.findChild(QObject, "readIpButton")
        self.ipButton.clicked.connect(self.read_ip)
        self.ipTextArea = window.findChild(QObject, "ipTextArea")
        self.t = ReadIpThread()
        self.t.sig.connect(self.receive_info)

    def read_ip(self):
        print('> clicked')
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.ipButton.setEnabled(False)
        self.t.start()

    def receive_info(self, text):
        print('> received = ', text)
        QApplication.restoreOverrideCursor()
        self.ipTextArea.append(text)
        self.ipButton.setEnabled(True)


if __name__ == "__main__":

    # Set the QtQuick Style
    # Acceptable values: Default, Fusion, Imagine, Material, Universal.
    os.environ['QT_QUICK_CONTROLS_STYLE'] = (sys.argv[1]
                                             if len(sys.argv) > 1 else "Material")

    # As Qt Charts utilizes Qt Graphics View Framework for drawing, QApplication must be used.
    # The project created with the wizard is usable with Qt Charts after the QGuiApplication is replaced with QApplication.
    app = QApplication(sys.argv)
    engine = NexApplication()
    if not engine.rootObjects():
        sys.exit(-1)

    # Send QT_QUICK_CONTROLS_STYLE to main qml (only for demonstration)
    # For more details and other methods to communicate between Qml and Python:
    #   http://doc.qt.io/archives/qt-4.8/qtbinding.html

    qtquick2Themes = engine.rootObjects()[0].findChild(
        QObject,
        'qtquick2Themes'
    )
    print('>>', qtquick2Themes)
    qtquick2Themes.setProperty('text', os.environ['QT_QUICK_CONTROLS_STYLE'])
    sys.exit(app.exec_())

