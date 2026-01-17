class C:
    def __init__(self, points):
        self.points = points

    def m(self, n):
        count = sum(1 for x, y in self.points if x > 0 and y > 0)
        return count >= n
