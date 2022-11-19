class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.name = dirName
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        self.children = []
        print('directory %s created!', self.name)
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('directory %s deleted!', self.name)
        return

    def listContent(self):
        return self.children

    def move(self, node, path):
        if not self.children.__contains__(node):
            raise SystemError("Directory doesn't contain entered node") 
        if (path.children.count() == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory is full')
        self.children.remove(node)
        node.father = path
        path.children.append(node)
        print('element %s moved!', node.name)
        return

    def moveSelf(self, path):
        if (path.children.count() == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('directory %s moved!', self.name)
        return