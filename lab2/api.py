from flask import Flask
from nodes.directory import Directory
from nodes.binary_file import BinaryFile

app = Flask(__name__)
rootDirectory = Directory('root', 100)
name = 'test_binary'
fileInfo = 'test info for binary file!!!'
binaryFile = BinaryFile(name, rootDirectory, fileInfo)

@app.route('/directory', methods=['GET'])
def directoryGetAll():
    return

@app.route('/directory', methods=['POST'])
def directoryGetAll():
    return

@app.route('/directory', methods=['DELETE'])
def directoryGetAll():
    return

@app.route('/directory', methods=['PATCH'])
def directoryGetAll():
    return


@app.route('/binaryfile', methods=['GET'])
def directoryGetAll():
    return

@app.route('/binaryfile', methods=['POST'])
def directoryGetAll():
    return

@app.route('/binaryfile', methods=['DELETE'])
def directoryGetAll():
    return

@app.route('/binaryfile', methods=['PATCH'])
def directoryGetAll():
    return


@app.route('/logtextfile', methods=['GET'])
def directoryGetAll():
    return

@app.route('/logtextfile', methods=['POST'])
def directoryGetAll():
    return

@app.route('/logtextfile', methods=['DELETE'])
def directoryGetAll():
    return

@app.route('/logtextfile', methods=['PUT'])
def directoryGetAll():
    return

@app.route('/logtextfile', methods=['PATCH'])
def directoryGetAll():
    return


@app.route('/bufferfile', methods=['GET'])
def directoryGetAll():
    return

@app.route('/bufferfile', methods=['POST'])
def directoryGetAll():
    return

@app.route('/bufferfile', methods=['DELETE'])
def directoryGetAll():
    return

@app.route('/bufferfile', methods=['PUT'])
def directoryGetAll():
    return

@app.route('/bufferfile', methods=['PATCH'])
def directoryGetAll():
    return
 
if __name__ == '__main__':
    app.run(debug=True)