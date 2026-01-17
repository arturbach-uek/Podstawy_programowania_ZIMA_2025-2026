class Statistics():
    def __init__(self, ):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)
    
    def display_numbers(self):
        print(f"Numbers: {" ".join(str(num) for num in self.numbers)}")

    def get_max(self):
        if not self.numbers:
            return None
        return max(self.numbers)
    
    def get_min(self):
        if not self.numbers:
            return None
        return min(self.numbers)
    
    def get_mean(self):
        if not self.numbers:
            return None
        return sum(self.numbers) / len(self.numbers)

    def get_median(self):
        if not self.numbers:
            return None
        
        sorted_nums = sorted(self.numbers)
        length = len(sorted_nums)
        middle = length // 2
        
        if length % 2 == 0:
            return (sorted_nums[middle - 1] + sorted_nums[middle]) / 2
        else:
            return sorted_nums[middle]
    
    def print_statistics(self):
        print(f"Minimum: {self.get_min()}")
        print(f"Maximum: {self.get_max()}")
        print(f"Mean: {self.get_mean():.2f}")
        print(f"Median: {self.get_median()}")


stats = Statistics()
    
numbers = [12, 37, 6, 9, 17]
for num in numbers:
    stats.add_number(num)

stats.display_numbers()
stats.print_statistics()