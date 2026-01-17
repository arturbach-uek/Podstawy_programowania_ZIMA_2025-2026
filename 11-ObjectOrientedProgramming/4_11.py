class C:
    def __init__(self, sector_fans):
        self.sector_fans = sector_fans.copy()

    def m1(self, sector, fans_count):
        self.sector_fans[sector] = fans_count

    def m2(self, sectors_string):
        total_fans = 0
        for sector in sectors_string:
            if sector in self.sector_fans:
                total_fans += self.sector_fans[sector]
        return total_fans

stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})
stadium.m1("G", 130)
print(stadium.m2("GD"))
print(stadium.m2("KEJ"))