from nodes.directory import Directory
from nodes.log_text_file import LogTextFile

class TestLogTextFile:
    rootDirectory = Directory('root', 10)

    def test_initLogTextFile(self):
        name = 'test_log_text'
        logTextFile = LogTextFile(name, self.rootDirectory)

        assert logTextFile.name == name
        assert logTextFile.info == ''
        assert logTextFile.father == self.rootDirectory
        assert self.rootDirectory.children.__contains__(logTextFile)

    def test_deleteLogTextFile(self):
        name = 'test_log_text'
        logTextFile = LogTextFile(name, self.rootDirectory)

        logTextFile.delete()

        assert not self.rootDirectory.children.__contains__(logTextFile)

    def test_readLogTextFile(self):
        name = 'test_log_text'
        logTextFile = LogTextFile(name, self.rootDirectory)

        assert logTextFile.readFile() == ''

    def test_moveLogTextFile(self):
        firstDirectory = Directory('first', 1, self.rootDirectory)

        name = 'test_log_text'
        logTextFile = LogTextFile(name, self.rootDirectory)

        logTextFile.move(self.rootDirectory)

        assert not firstDirectory.children.__contains__(logTextFile)
        assert self.rootDirectory.children.__contains__(logTextFile)
    
    def test_appendLineLogTextFile(self):
        name = 'test_log_text'
        logTextFile = LogTextFile(name, self.rootDirectory)

        lineToAdd = 'info to add in log text file)'
        logTextFile.appendLine(lineToAdd)

        assert logTextFile.info == lineToAdd
        assert logTextFile.readFile() == lineToAdd