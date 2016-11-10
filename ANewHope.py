class ANewHope:

    def __init__(self):
        self._washdays = None
        self._weeksize = None
        self._currentweek = None
        self._lastweek = None
        self._washing = None
        self._weekcount = None

    def count(self, firstWeek, lastWeek, D):
        if firstWeek == lastWeek:
            return 1
        if set(firstWeek) == set(lastWeek) and len(lastWeek) > D:
            self._initvalues(firstWeek, lastWeek, D)
            return self._countweeks()
        return 0

    def _initvalues(self, firstweek, lastweek, washdays):
        self._washdays = washdays - 1
        self._weeksize = len(firstweek)
        self._currentweek = [None] * self._weeksize
        self._lastweek = lastweek
        self._washing = {}
        self._initfirstweek(firstweek)

    def _initfirstweek(self, shirtlist):
        washdays = self._washdays
        self._currentweek = shirtlist
        for shirt in reversed(shirtlist):
            self._washing[shirt] = washdays
            if washdays != 0:
                washdays -= 1

    def _countweeks(self):
        weekcount = 1
        complete = False
        while not complete:
            complete = True
            self._runweek()
            weekcount += 1
            for i in range(self._weeksize):
                if self._lastweek[i] != self._currentweek[i]:
                    complete = False
                    break
        return weekcount

    def _runweek(self):
        self._currentweek = list()
        for _ in self._lastweek:
            self._runday()

    def _runday(self):
        chosenshirt = None
        for shirt in self._lastweek:
            if self._washing[shirt] == 0 and shirt not in self._currentweek:
                self._currentweek.append(shirt)
                chosenshirt = shirt
                break
        for shirt, daysleft in self._washing.items():
            if self._washing[shirt] != 0:
                self._washing[shirt] -= 1
        self._washing[chosenshirt] += self._washdays

test = ANewHope()
print("Example 1")
print(test.count((1, 2, 3, 4), (4, 3, 2, 1), 3))
print("Example 2")
print(test.count((8, 5, 4, 1, 7, 6, 3, 2), (2, 4, 6, 8, 1, 3, 5, 7), 3))
print("Example 3")
print(test.count((1, 2, 3, 4), (1, 2, 3, 4), 2))
