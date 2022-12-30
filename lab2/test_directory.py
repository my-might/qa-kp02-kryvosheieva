from nodes.directory import Directory
from types import NoneType

class TestDirectory:
    def test_initDirectory(self):
        name = 'root'
        maxElements = 5
        directory = Directory(name, maxElements)

        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElements
        assert type(directory.father) is NoneType

    def test_deleteDirectory(self):
        name = 'root'
        maxElements = 5
        rootDirectory = Directory(name, maxElements)

        newDirectory = Directory('new', 1, rootDirectory)

        newDirectory.delete()
        del newDirectory

        assert 'newDirectory' not in locals()
        assert not rootDirectory.children.__contains__(newDirectory)

    def test_listDirectoryContent(self):
        name = 'root'
        maxElements = 5
        rootDirectory = Directory(name, maxElements)

        newDirectory = Directory('new', 1, rootDirectory)

        content = rootDirectory.listContent()

        assert content == [newDirectory]

    def test_moveDirectory(self):
        name = 'root'
        maxElements = 5
        rootDirectory = Directory(name, maxElements)

        firstDirectory = Directory('first', 1, rootDirectory)
        secondDirectory = Directory('second', 1, rootDirectory)

        rootDirectory.move(firstDirectory, secondDirectory)

        assert not rootDirectory.children.__contains__(firstDirectory)
        assert secondDirectory.children.__contains__(firstDirectory)

    def test_moveDirectorySelf(self):
        name = 'root'
        maxElements = 5
        rootDirectory = Directory(name, maxElements)

        firstDirectory = Directory('first', 1, rootDirectory)
        secondDirectory = Directory('second', 1, rootDirectory)

        firstDirectory.moveSelf(secondDirectory)

        assert not rootDirectory.children.__contains__(firstDirectory)
        assert secondDirectory.children.__contains__(firstDirectory)