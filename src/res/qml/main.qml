import QtQml 2.2
import QtQuick 2.6

Item {
    Loader {
        id: mainWindowLoader
        objectName: "mainWindow"
        active: false
        source: "qrc:/res/qml/window.qml"
        asynchronous: true
        onLoaded: {
            item.visible = true;
            item.visibility = "FullScreen";
            splashScreenLoader.item.visible = false;
            splashScreenLoader.source = "";
        }
    }

    Loader {
        id: splashScreenLoader
        source: "qrc:/res/qml/splashscreen.qml"
        onLoaded: {
            mainWindowLoader.active = true;            
        }
    }
}
