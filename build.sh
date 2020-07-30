#!/usr/bin/bash

# delete old files
rm -rf build && rm -rf dist

# build exec
APP_NAME="NexAIDemo"
KEY="ABCDEFGHIJKLMNOP"
DIR_ROOT="src"


pyrcc5 -o src/res/resources.py src/resources.qrc
 

# append files
pyinstaller --name=${APP_NAME} -F --windowed \
--key ${KEY} ${DIR_ROOT}/main.py \
--add-data ${DIR_ROOT}/res:res

# run exec
#./dist/${APP_NAME}
