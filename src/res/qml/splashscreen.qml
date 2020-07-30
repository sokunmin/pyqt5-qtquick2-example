import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Window 2.2

Window {
    id: splashScreen
    modality: Qt.ApplicationModal
    flags: Qt.SplashScreen
    width: Screen.width
    height: Screen.height

    Image {
        id: image
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
        width: 1920
        height: 1080
        source: "/res/images/nex_wallpaper.jpg"
    }
    Component.onCompleted: visible = true
}
