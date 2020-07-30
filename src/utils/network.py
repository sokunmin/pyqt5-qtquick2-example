from PyQt5 import QtCore

from PyQt5.QtNetwork import  QHostAddress, QAbstractSocket, \
                               QNetworkInterface, QNetworkAddressEntry, \
                               QHostInfo, QNetworkConfiguration,QNetworkConfigurationManager
from PyQt5.QtCore import QThread, pyqtSignal



class ReadIpThread(QtCore.QThread):
    sig = pyqtSignal(str)

    def run(self):
        localHostName =  QHostInfo.localHostName()
        hostinfo= QHostInfo.fromName(localHostName)
        listaddress = hostinfo.addresses()

        for address in listaddress:
           if QHostAddress(address).protocol() == QAbstractSocket.IPv4Protocol:
               address = QHostAddress(address).toString()
        print(address)

        host_info = ""
        confList = QNetworkConfigurationManager().allConfigurations()
        print("confList = ", confList.__len__())
        for conf in confList:
            if  str(conf.bearerTypeName()) ==  "Ethernet":
               host_info += "\n"
               host_info += "name : " + QNetworkConfiguration(conf).name() + "\n"
               host_info += str(QNetworkConfiguration(conf).isValid()) + "\n"
               host_info += "bearerType: " + QNetworkConfiguration(conf).bearerTypeName() + "\n"

        list = QNetworkInterface.allInterfaces()
        for interface in list:
            host_info += "\n"
            host_info += "=============================\n"
            host_info += "name: " + interface.name() + "\n"
            host_info += QNetworkInterface(interface).hardwareAddress() + "\n"
            host_info += str(QNetworkInterface(interface).isValid()) + "\n"
            host_info += "---------\n"
            if QNetworkInterface(interface).flags() & QNetworkInterface.IsUp:
                host_info += "Interface: is up\n"
            if QNetworkInterface(interface).flags() & QNetworkInterface.IsLoopBack:
                host_info += "Interface: is loop back\n"  # 迴環地址
            if QNetworkInterface(interface).flags() & QNetworkInterface.IsRunning:
                host_info += "Interface: is running \n"   # 網絡已經啓動運行
            if  interface.flags() & QNetworkInterface.CanMulticast:
                host_info += "Interface: CanMulticast\n"  # 多播
            if  interface.flags() & QNetworkInterface.CanBroadcast:
                host_info += "Interface: CanBroadcast\n"
            host_info += "---------\n"

            entryList = QNetworkInterface(interface).addressEntries()
            for entry in entryList:
                address = entry.ip()
                if QHostAddress(address).protocol() == QAbstractSocket.IPv4Protocol:# and  \
                    # str(address.toString()) != "127.0.0.1":
                    host_info += "IP Address: " + QNetworkAddressEntry(entry).ip().toString() + "\n"
                    host_info += "Netmask: " + QNetworkAddressEntry(entry).netmask().toString() + "\n"
                    host_info += "Broadcast: " + QNetworkAddressEntry(entry).broadcast().toString() + "\n"
            host_info += "=============================\n"
        self.sig.emit(host_info)
