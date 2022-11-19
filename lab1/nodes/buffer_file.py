class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.name = fileName
        self.MAX_BUF_FILE_SIZE = maxSize
        self.father = father
        self.queue = []
        if father != None:
            self.father.children.append(self)
        print('buffer file %s created!', self.name)
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('buffer file %s deleted!', self.name)
        return

    def move(self, path):
        if (path.children.count() == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('buffer file %s moved!', self.name)
        return

    def pushElement(self, element):
        if self.MAX_BUF_FILE_SIZE == self.queue.count:
            raise SystemError('Buffer file is full')
        self.queue.append(element)
        return

    def consumeElement(self):
        if self.queue.count == 0:
            raise SystemError('Buffer file is empty')
        lineToReturn = self.queue[0]
        self.queue.pop(0)
        return lineToReturn