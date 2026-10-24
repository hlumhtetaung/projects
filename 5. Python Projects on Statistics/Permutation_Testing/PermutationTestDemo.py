import numpy as np
import matplotlib.pyplot as plt

maths = [85, 90, 78, 92, 88, 95, 80, 87, 91, 89]
physics = [82, 88, 79, 85, 90, 84, 81, 86, 83, 87]

# Original mean difference between maths and physics scores
original_mean_diff = np.mean(maths) - np.mean(physics)
print(original_mean_diff) # 3.0

# null hypothesis: mean difference between maths and physics scores is zero (H0: μ_maths - μ_physics = 0)
# alternative hypothesis: mean of maths scores is greater than mean of physics scores (H1: μ_maths - μ_physics > 0)

# Null Hypothesis process
# Combine the two datasets
# Randomly shuffle the combined dataset and split it into two new groups of the same size as the original groups
# Calculate the mean difference between the two new groups (Build a distribution of mean differences under the null hypothesis)
# Repeat the above process many times (e.g., 10,000 times) to build a distribution of mean differences under the null hypothesis
# Calculate the p-value by finding the proportion of mean differences in the null distribution that are greater than or equal to the original mean difference

# Set the number of permutations
number_of_permutations = 10000
null_distribution = [] # To store means of the permuted samples

for i in range(number_of_permutations):
    # Combining scores of maths and physics
    combined_scores = np.concatenate((maths, physics))

    # Shuffling the combined scores
    np.random.shuffle(combined_scores)

    # Initialize an array to store the mean differences under the null hypothesis
    new_maths = combined_scores[:len(maths)]
    new_physics = combined_scores[len(maths):]

    # Calculate the mean difference for the shuffled groups
    mean_diff = np.mean(new_maths) - np.mean(new_physics)

    null_distribution.append(mean_diff)

# Histogram of the null distribution
plt.hist(null_distribution, bins=50, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Mean Difference')
plt.ylabel('Frequency')
plt.title('Null Distribution')
plt.axvline(original_mean_diff, color='red', linewidth=2, label='Original Mean Difference')
plt.legend()
plt.show()

# Based on the plot we failed to reject the null hypothsis.
# The original mean difference is not significant enough to reject the null hypothesis.

# Calculate the p-value
p_value = np.sum(np.array(null_distribution) >= original_mean_diff) / number_of_permutations
print(f"P-value: {p_value}") # 0.0829
# p value > 0.05, we fail to reject the null hypothesis.