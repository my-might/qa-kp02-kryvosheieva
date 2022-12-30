from nodes.directory import Directory
from nodes.log_text_file import LogTextFile

class TestLogTextFile:

    def test_initLogTextFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_log_text'
        logTextFile = LogTextFile(name, rootDirectory)

        assert logTextFile.name == name
        assert logTextFile.info == ''
        assert logTextFile.father == rootDirectory
        assert rootDirectory.children.__contains__(logTextFile)

    def test_deleteLogTextFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_log_text'
        logTextFile = LogTextFile(name, rootDirectory)

        logTextFile.delete()
        del logTextFile

        assert 'logTextFile' not in locals()
        assert not rootDirectory.children.__contains__(logTextFile)

    def test_readLogTextFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_log_text'
        logTextFile = LogTextFile(name, rootDirectory)

        assert logTextFile.readFile() == ''

    def test_moveLogTextFile(self):
        rootDirectory = Directory('root', 10)
        firstDirectory = Directory('first', 1, rootDirectory)

        name = 'test_log_text'
        logTextFile = LogTextFile(name, rootDirectory)

        logTextFile.move(rootDirectory)

        assert not firstDirectory.children.__contains__(logTextFile)
        assert rootDirectory.children.__contains__(logTextFile)
    
    def test_appendLineLogTextFile(self):
        rootDirectory = Directory('root', 10)
        name = 'test_log_text'
        logTextFile = LogTextFile(name, rootDirectory)

        lineToAdd = 'info to add in log text file)'
        logTextFile.appendLine(lineToAdd)

        assert logTextFile.info == lineToAdd
        assert logTextFile.readFile() == lineToAdd