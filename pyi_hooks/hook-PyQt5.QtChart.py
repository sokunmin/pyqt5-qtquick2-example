#-----------------------------------------------------------------------------
# Copyright (c) 2013-2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------


hiddenimports = ['PyQt5.sip',
                 'PyQt5.QtQuick'
                ]

from PyInstaller.utils.hooks import (
    qt5_qml_dir,
    qt5_qml_data,
    qt5_qml_plugins_binaries,
    qt5_qml_plugins_datas
)

# TODO: we should parse the Qml files to see what we need to import.
dirs = ['Qt',
        #'QtAudioEngine',
        #'QtGraphicalEffects',
        #'QtMultiMedia',
        'QtQml',
        'QtQuick',
        'QtQuick.2',
        #'QtSensors',
        #'QtTest',
        'QtCharts'
        ]

qmldir = qt5_qml_dir('PyQt5')

# Add base qml directories
datas = [qt5_qml_data(qmldir, dir) for dir in dirs]

# Add qmldir and *.qmltypes files
for dir in dirs:
    datas.extend(qt5_qml_plugins_datas(qmldir, dir))

# Add binaries
binaries = []
for dir in dirs:
    binaries.extend(qt5_qml_plugins_binaries(qmldir, dir))