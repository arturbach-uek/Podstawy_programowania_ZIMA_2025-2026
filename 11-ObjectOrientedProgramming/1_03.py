class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_receipt(self):
        print(f"Paragon Taxi:")
        print(f"Przebyty dystans: {self.distance} km")
        print(f"Stawka za km: {self.rate_per_km} PLN")
        print(f"Całkowita opłata: {self.fare} PLN")
        print("-" * 30)

def main():
    ride1 = TaxiRide(5)
    ride2 = TaxiRide(6.5)

    ride1.calculate_fare(10)
    ride2.calculate_fare(8)

    ride1.print_receipt()
    ride2.print_receipt()

if __name__ == "__main__":
    main()
