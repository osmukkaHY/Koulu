import re

class WordPos:
    def __init__(self, start, length):
        self.start = start
        self.end = start + length-1

    def __repr__(self):
        return f'({self.start}, {self.end})'

class WordFinder:
    def set_grid(self, grid):
        self.word = None
        self.grid = grid

    def count(self, word):
        self.word = word
        self.positions = set()

        return self.positions

    def find_on_line(self, line):


    def __init__(self):
        self.grid = []

if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    finder.set_grid(grid)

    print(finder.count("TIRA")) # 7 
    print(finder.count("TA")) # 13
    print(finder.count("RITARI")) # 3
    print(finder.count("A")) # 8
    print(finder.count("AA")) # 6
    print(finder.count("RAITA")) # 0
