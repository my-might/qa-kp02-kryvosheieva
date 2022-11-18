from nodes.directory import Directory
from nodes.binary_file import BinaryFile

class TestBinaryFile:
    rootDirectory = Directory('root', 10)

    def test_initBinaryFile(self):
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, self.rootDirectory, fileInfo)

        assert binaryFile.name == name
        assert binaryFile.father == self.rootDirectory
        assert binaryFile.info == fileInfo
        assert self.rootDirectory.children.__contains__(binaryFile)

    def test_deleteBinaryFile(self):
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, self.rootDirectory, fileInfo)

        binaryFile.delete()

        assert not self.rootDirectory.children.__contains__(binaryFile)

    def test_readBinaryFile(self):
        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, self.rootDirectory, fileInfo)

        assert binaryFile.readFile() == fileInfo

    def test_moveBinaryFile(self):
        firstDirectory = Directory('first', 1, self.rootDirectory)

        name = 'test_binary'
        fileInfo = 'test info for binary file!!!'
        binaryFile = BinaryFile(name, firstDirectory, fileInfo)

        binaryFile.move(self.rootDirectory)

        assert not firstDirectory.children.__contains__(binaryFile)
        assert self.rootDirectory.children.__contains__(binaryFile)