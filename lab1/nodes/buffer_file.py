class BufferFile:
    def __init__(self, fileName, maxSize = 0, father = None):
        self.name = fileName
        self.MAX_BUF_FILE_SIZE = maxSize
        self.father = father
        self.queue = []
        if father != None:
            if (self.father.DIR_MAX_ELEMS == len(self.father.children)):
                raise SystemError('Father directory ', father.name, ' is full')
            self.father.children.append(self)
        print('buffer file ', self.name,' created!')
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('buffer file ', self.name,' deleted!')
        return

    def move(self, path):
        if (len(path.children) == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory ', path.name, ' is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('buffer file ', self.name,' moved to ', path.name, '!')
        return

    def pushElement(self, element):
        if self.MAX_BUF_FILE_SIZE == len(self.queue):
            raise SystemError('Buffer file ', self.name, ' is full')
        self.queue.append(element)
        return

    def consumeElement(self):
        if len(self.queue) == 0:
            raise SystemError('Buffer file ', self.name, ' is empty')
        lineToReturn = self.queue[0]
        self.queue.pop(0)
        return lineToReturn