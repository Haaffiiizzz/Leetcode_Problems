import string
class Spreadsheet:

    def __init__(self, rows: int):
        self.Sheet = {i: [0]* (10**5) for i in string.ascii_uppercase}
        

    def setCell(self, cell: str, value: int) -> None:
        loc, index = cell[0], int(cell[1:])
        self.Sheet[loc][index] = value
        

    def resetCell(self, cell: str) -> None:
        loc, index = cell[0], int(cell[1:])
        self.Sheet[loc][index] = 0

    def getValue(self, formula: str) -> int:
        formula = formula.split("+")
        first = formula[0][1:]
        second = formula[1]

        if first[0].isdigit():
            first = int(first)
        else:
            first = self.Sheet[first[0]][int(first[1:])]

        if second[0].isdigit():
            second = int(second)
        else:
            second = self.Sheet[second[0]][int(second[1:])]

        return first + second
            
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)