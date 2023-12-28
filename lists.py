class NumberList:
    def __init__(self, lst1: [int | float], lst2: [int | float]):
        self.lst1 = lst1
        self.lst2 = lst2

    def getList(self) -> [float | float]:
        average1 = 0
        if self.lst1:
            average1 = sum(self.lst1) / len(self.lst1)

        average2 = 0
        if self.lst2:
            average2 = sum(self.lst2) / len(self.lst2)

        return average1, average2


    def listComparison(self):
        average1, average2 = self.getList()
        if average1 > average2:
            print('Первый список имеет среднее значение больше')
        if average1 < average2:
            print('Второй  список имеет среднее значение больше')
        else:
            print("Списки имеют равное среднее значение")