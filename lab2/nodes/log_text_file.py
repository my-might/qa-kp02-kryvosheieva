class LogTextFile:
    def __init__(self, fileName, father = None):
        self.name = fileName
        self.father = father
        self.info = ''
        if father != None:
            if (self.father.DIR_MAX_ELEMS == len(self.father.children)):
                raise SystemError('Father directory ', father.name, ' is full')
            self.father.children.append(self)
        print('log text file ', self.name,' created!')
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('log text file ', self.name,' deleted!')
        return

    def readFile(self):
        return self.info

    def move(self, path):
        if (len(path.children) == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory ', path.name, ' is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('log text file ', self.name,' moved to ', path.name, '!')
        return

    def appendLine(self, lineToAdd):
        self.info = self.info + lineToAdd
        return