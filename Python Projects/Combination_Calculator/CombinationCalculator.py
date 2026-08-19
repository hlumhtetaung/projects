class CombinationCalculator:
    def __init__(self, n, k):
        self.n = n
        self.k = k

    def factorial(self, num):
        if num == 0 or num == 1:
            return 1
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

    # calculates the possible combinations using the formula
    def calculate_combination(self):
        if self.k > self.n:
            return "Invalid input: k (group of items) cannot be greater than n (total items in the set)."
        else:
            total_set = self.factorial(self.n)
            group_of_items = self.factorial(self.k)
            remaining_items = self.factorial(self.n - self.k)
            possible_combinations = total_set // (group_of_items * remaining_items)
            return possible_combinations

total_set = int(input("Please enter the total number of items in the set: "))
group_of_items = int(input("Please enter the total number of items for the grouping: "))
print("Possible combinations: " + str(CombinationCalculator(total_set, group_of_items).calculate_combination()))