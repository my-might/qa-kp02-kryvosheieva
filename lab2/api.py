from flask import Flask
from nodes.directory import Directory
from nodes.binary_file import BinaryFile

app = Flask(__name__)
rootDirectory = Directory('root', 100)
name = 'test_binary'
fileInfo = 'test info for binary file!!!'
binaryFile = BinaryFile(name, rootDirectory, fileInfo)

@app.route('/directory', methods=['GET'])
def directory_get_all():
    return

@app.route('/directory', methods=['POST'])
def directory_post():
    return

@app.route('/directory', methods=['DELETE'])
def directory_delete():
    return

@app.route('/directory', methods=['PATCH'])
def directory_patch():
    return


@app.route('/binaryfile', methods=['GET'])
def binaryfile_get():
    return

@app.route('/binaryfile', methods=['POST'])
def binaryfile_post():
    return

@app.route('/binaryfile', methods=['DELETE'])
def binaryfile_delete():
    return

@app.route('/binaryfile', methods=['PATCH'])
def binaryfile_patch():
    return


@app.route('/logtextfile', methods=['GET'])
def logtextfile_get():
    return

@app.route('/logtextfile', methods=['POST'])
def logtextfile_post():
    return

@app.route('/logtextfile', methods=['DELETE'])
def logtextfile_delete():
    return

@app.route('/logtextfile', methods=['PUT'])
def logtextfile_put():
    return

@app.route('/logtextfile', methods=['PATCH'])
def logtextfile_patch():
    return


@app.route('/bufferfile', methods=['GET'])
def bufferfile_get():
    return

@app.route('/bufferfile', methods=['POST'])
def bufferfile_post():
    return

@app.route('/bufferfile', methods=['DELETE'])
def bufferfile_delete():
    return

@app.route('/bufferfile', methods=['PUT'])
def bufferfile_put():
    return

@app.route('/bufferfile', methods=['PATCH'])
def bufferfile_patch():
    return
 
if __name__ == '__main__':
    app.run(debug=True)