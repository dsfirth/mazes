class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column

        self.north = None
        self.east = None
        self.south = None
        self.west = None

        self.__links = {}

    def link(self, cell, bidi=True):
        self.__links[cell] = True
        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self.__links.pop(cell)
        if bidi:
            cell.unlick(self, False)

    def links(self):
        return self.__links.keys()

    def linked(self, cell):
        return cell in self.__links

    def neighbors(self):
        return list(filter(None, [self.north, self.east, self.south, self.west]))
