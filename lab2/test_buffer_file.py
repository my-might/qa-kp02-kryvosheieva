from nodes.directory import Directory
from nodes.buffer_file import BufferFile

class TestBufferFile:

    def test_initBufferFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, rootDirectory)

        assert bufferFile.name == name
        assert bufferFile.queue == []
        assert bufferFile.father == rootDirectory
        assert bufferFile.MAX_BUF_FILE_SIZE == maxSize
        assert rootDirectory.children.__contains__(bufferFile)

    def test_deleteBufferFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, rootDirectory)

        bufferFile.delete()
        del bufferFile

        assert 'bufferFile' not in locals()
        assert not rootDirectory.children.__contains__(bufferFile)

    def test_moveBufferFile(self):
        rootDirectory = Directory('root', 10)
        firstDirectory = Directory('first', 1, rootDirectory)

        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, rootDirectory)

        bufferFile.move(rootDirectory)

        assert not firstDirectory.children.__contains__(bufferFile)
        assert rootDirectory.children.__contains__(bufferFile)
    
    def test_pushConsumeBufferFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, rootDirectory)

        lineToPush = 'info to add in buffer file)'
        bufferFile.pushElement(lineToPush)

        assert bufferFile.queue.__contains__(lineToPush)
        assert bufferFile.consumeElement() == lineToPush