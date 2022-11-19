class BinaryFile:
    def __init__(self, fileName, father = None, info = None):
        self.name = fileName
        self.father = father
        self.info = info
        print('binary file %s created!', self.name)
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('binary file %s deleted!', self.name)
        return

    def readFile(self):
        return self.info

    def move(self, path):
        if (path.children.count() == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('binary file %s moved!', self.name)
        return