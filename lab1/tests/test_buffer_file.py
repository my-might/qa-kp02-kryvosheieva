from nodes.directory import Directory
from nodes.buffer_file import BufferFile

class TestBufferFile:
    rootDirectory = Directory('root', 10)

    def test_initBufferFile(self):
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, self.rootDirectory)

        assert bufferFile.name == name
        assert bufferFile.queue == []
        assert bufferFile.father == self.rootDirectory
        assert bufferFile.MAX_BUF_FILE_SIZE == maxSize
        assert self.rootDirectory.children.__contains__(bufferFile)

    def test_deleteBufferFile(self):
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, self.rootDirectory)

        bufferFile.delete()

        assert not self.rootDirectory.children.__contains__(bufferFile)

    def test_moveBufferFile(self):
        firstDirectory = Directory('first', 1, self.rootDirectory)

        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, self.rootDirectory)

        bufferFile.move(self.rootDirectory)

        assert not firstDirectory.children.__contains__(bufferFile)
        assert self.rootDirectory.children.__contains__(bufferFile)
    
    def test_pushConsumeBufferFile(self):
        name = 'test_buffer'
        maxSize = 5
        bufferFile = BufferFile(name, maxSize, self.rootDirectory)

        lineToPush = 'info to add in buffer file)'
        bufferFile.pushElement(lineToPush)

        assert bufferFile.queue.__contains__(lineToPush)
        assert bufferFile.consumeElement() == lineToPush