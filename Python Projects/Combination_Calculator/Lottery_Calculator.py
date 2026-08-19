class LotteryCalculator:
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
    def calculate_total_combinations(self):
        if self.k > self.n:
            return "Invalid input: k (group of items) cannot be greater than n (total items in the set)."
        else:
            total_set = self.factorial(self.n)
            group_of_items = self.factorial(self.k)
            remaining_items = self.factorial(self.n - self.k)
            possible_combinations = total_set // (group_of_items * remaining_items)
            return possible_combinations

    # calculates the probability of winning the lottery
    def winning_chance(self):
        return 1 / self.calculate_total_combinations()

    def k_matches(self, matches):
        if matches > self.k:
            return "Invalid input: matches cannot be greater than k (group of items)."
        else:
            total_set = self.calculate_total_combinations()
            matching = self.factorial(self.k) // (self.factorial(matches) * (self.factorial(self.k - matches)))
            not_matching = self.factorial(self.n - self.k) // (self.factorial(self.k - matches) * self.factorial((self.n - self.k) - (self.k - matches)))
            probability = (matching * not_matching) / total_set
            return probability

# lottery program output
lottery = LotteryCalculator(49, 6)

print("=== 6/49 Lottery Probability ===")

print(f"Total possible combinations: {lottery.calculate_total_combinations():,}")

print(f"Jackpot probability: {lottery.winning_chance():.10f}")

print("\nProbability of exactly k matches:")

for matches in range(0, 7):
    probability = lottery.k_matches(matches)
    print(f"{matches} matches: {probability:.10f} ({probability * 100:.6f}%)")