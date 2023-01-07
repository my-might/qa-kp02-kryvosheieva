from flask import Flask, jsonify, request
from nodes.directory import Directory
from nodes.binary_file import BinaryFile
from nodes.log_text_file import LogTextFile
from nodes.buffer_file import BufferFile

app = Flask(__name__)
rootDirectory = Directory('root', 100)

def get_key(path):
    path = path.split('/')
    if path[0] != 'root':
        raise ValueError
    key = [rootDirectory]
    if len(path) > 1:
        for pathElem in path[1:]:
            key = list(filter(lambda c: c.name == pathElem, key[0].children))
            if len(key) == 0:
                raise ValueError
    return key[0]

@app.route('/directory', methods=['GET'])
def directory_get_all():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    return jsonify({
        'name':key.name,
        'children':list(map(lambda c: c.name, key.children))
    }), 200

@app.route('/directory', methods=['POST'])
def directory_post():
    body = request.json
    if not body or not 'name' in body or not 'max_elems' in body or not 'father' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['father'])
    except:
        return 'Invalid path', 404
    try:
        Directory(body['name'], body['max_elems'], key)
    except SystemError as error:
        return str(error), 400

    return 'Directory created!', 200

@app.route('/directory', methods=['DELETE'])
def directory_delete():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    if path == 'root':
        return 'Cannot delete root', 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    key.delete()
    return 'Directory deleted!', 200

@app.route('/directory', methods=['PATCH'])
def directory_patch():
    pathToMove = request.args.get('move_to')
    nodeToMove = request.args.get('move_from')
    if pathToMove == None or nodeToMove == None:
        return "Empty path or node", 400
    nodeSplit = nodeToMove.split('/')
    if len(nodeSplit) == 1:
        return "Cannot move root", 400
    try:
        keyPath = get_key(pathToMove)
        keyNode = get_key(nodeToMove)
    except:
        return 'Invalid path', 404
    try:
        keyNode.father.move(keyNode, keyPath)
    except SystemError as error:
        return str(error), 400

    return 'Directory moved!', 200


@app.route('/binaryfile', methods=['GET'])
def binaryfile_get():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    return jsonify({
        'name': key.name,
        'content': key.readFile()
    }), 200

@app.route('/binaryfile', methods=['POST'])
def binaryfile_post():
    body = request.json
    if not body or not 'name' in body or not 'info' in body or not 'father' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['father'])
    except:
        return 'Invalid path', 404
    try:
        BinaryFile(body['name'], key, body['info'])
    except SystemError as error:
        return str(error), 400

    return 'Binary file created!', 200

@app.route('/binaryfile', methods=['DELETE'])
def binaryfile_delete():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    key.delete()
    return 'Binary file deleted!', 200

@app.route('/binaryfile', methods=['PATCH'])
def binaryfile_patch():
    pathToMove = request.args.get('move_to')
    nodeToMove = request.args.get('move_from')
    if pathToMove == None or nodeToMove == None:
        return "Empty path or node", 400
    nodeSplit = nodeToMove.split('/')
    try:
        keyPath = get_key(pathToMove)
        keyNode = get_key(nodeToMove)
    except:
        return 'Invalid path', 404
    try:
        keyNode.move(keyPath)
    except SystemError as error:
        return str(error), 400

    return 'Binary file moved!', 200


@app.route('/logtextfile', methods=['GET'])
def logtextfile_get():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    return jsonify({
        'name': key.name,
        'content': key.readFile()
    }), 200

@app.route('/logtextfile', methods=['POST'])
def logtextfile_post():
    body = request.json
    if not body or not 'name' in body or not 'father' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['father'])
    except:
        return 'Invalid path', 404
    try:
        LogTextFile(body['name'], key)
    except SystemError as error:
        return str(error), 400

    return 'Log text file created!', 200

@app.route('/logtextfile', methods=['DELETE'])
def logtextfile_delete():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    key.delete()
    return 'Log text file deleted!', 200

@app.route('/logtextfile', methods=['PUT'])
def logtextfile_put():
    body = request.json
    if not body or not 'path' in body or not 'info' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['path'])
    except:
        return 'Invalid path', 404
    key.appendLine(body['info'])
    return 'Log text file modified!', 200

@app.route('/logtextfile', methods=['PATCH'])
def logtextfile_patch():
    pathToMove = request.args.get('move_to')
    nodeToMove = request.args.get('move_from')
    if pathToMove == None or nodeToMove == None:
        return "Empty path or node", 400
    try:
        keyPath = get_key(pathToMove)
        keyNode = get_key(nodeToMove)
    except:
        return 'Invalid path', 404
    try:
        keyNode.move(keyPath)
    except SystemError as error:
        return str(error), 400

    return 'Log text file moved!', 200


@app.route('/bufferfile', methods=['GET'])
def bufferfile_get():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    try:
        element = key.consumeElement()
    except SystemError as error:
        return str(error), 404
    return jsonify({
        'name': key.name,
        'content': element
    }), 200

@app.route('/bufferfile', methods=['POST'])
def bufferfile_post():
    body = request.json
    if not body or not 'name' in body or not 'max_size' in body or not 'father' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['father'])
    except:
        return 'Invalid path', 404
    try:
        BufferFile(body['name'], body['max_size'], key)
    except SystemError as error:
        return str(error), 400

    return 'Buffer file created!', 200

@app.route('/bufferfile', methods=['DELETE'])
def bufferfile_delete():
    path = request.args.get('path')
    if path == None:
        return "Empty path", 400
    try:
        key = get_key(path)
    except:
        return 'Invalid path', 404
    key.delete()
    return 'Buffer file deleted!', 200

@app.route('/bufferfile', methods=['PUT'])
def bufferfile_put():
    body = request.json
    if not body or not 'path' in body or not 'info' in body:
        return 'Invalid request body', 400
    try:
        key = get_key(body['path'])
    except:
        return 'Invalid path', 404
    try:
        key.pushElement(body['info'])
    except SyntaxError as error:
        return str(error), 400

    return 'Buffer file modified!', 200

@app.route('/bufferfile', methods=['PATCH'])
def bufferfile_patch():
    pathToMove = request.args.get('move_to')
    nodeToMove = request.args.get('move_from')
    if pathToMove == None or nodeToMove == None:
        return "Empty path or node", 400
    try:
        keyPath = get_key(pathToMove)
        keyNode = get_key(nodeToMove)
    except:
        return 'Invalid path', 404
    try:
        keyNode.move(keyPath)
    except SystemError as error:
        return str(error), 400

    return 'Buffer file moved!', 200

@app.route('/reset', methods=['PUT'])
def reset():
    rootDirectory = Directory('root', 100)
    return '', 200
 
if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)