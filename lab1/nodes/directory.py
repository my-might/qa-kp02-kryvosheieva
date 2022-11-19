class Directory:
    def __init__(self, dirName, maxElements = 0, father = None):
        self.name = dirName
        self.DIR_MAX_ELEMS = maxElements
        self.father = father
        if father != None:
            if (self.father.DIR_MAX_ELEMS == len(self.father.children)):
                raise SystemError('Father directory ', father.name, ' is full')
            self.father.children.append(self)
        self.children = []
        print('directory ', self.name,' created!')
    
    def delete(self):
        if self.father != None:
            self.father.children.remove(self)
        print('directory ', self.name,' deleted!')
        return

    def listContent(self):
        return self.children

    def move(self, node, path):
        if not self.children.__contains__(node):
            raise SystemError("Directory doesn't contain entered node") 
        if (len(path.children) == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory ', path.name, ' is full')
        self.children.remove(node)
        node.father = path
        path.children.append(node)
        print('element ', self.name,' moved to ', path.name, '!')
        return

    def moveSelf(self, path):
        if (len(path.children) == path.DIR_MAX_ELEMS):
            raise SystemError('Target directory ', path.name, ' is full')
        if self.father != None:
            self.father.children.remove(self)
        self.father = path
        path.children.append(self)
        print('directory ', self.name,' moved to ', path.name, '!')
        return