from nodes.binary_file import BinaryFile
from nodes.directory import Directory

class TestBinaryFile:

    def test_initBinaryFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, rootDirectory, fileInfo)

        assert binaryFile.name == name
        assert binaryFile.father == rootDirectory
        assert binaryFile.info == fileInfo
        assert binaryFile in rootDirectory.children

    def test_deleteBinaryFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, rootDirectory, fileInfo)

        binaryFile.delete()
        del binaryFile

        assert 'binaryFile' not in locals()

    def test_readBinaryFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, rootDirectory, fileInfo)

        assert binaryFile.readFile() == fileInfo

    def test_moveBinaryFile(self):
        rootDirectory = Directory('root', 10)
        firstDirectory = Directory('first', 1, rootDirectory)

        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, firstDirectory, fileInfo)

        binaryFile.move(rootDirectory)

        assert not firstDirectory.children.__contains__(binaryFile)
        assert rootDirectory.children.__contains__(binaryFile)