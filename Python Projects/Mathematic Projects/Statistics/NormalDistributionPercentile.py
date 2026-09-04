import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statistics import NormalDist

def z_score(point, mean, std_dev):
    return (point - mean) / std_dev

def percentile_calculation(z, direction):
    if direction == "above":
        percentile = 1 - NormalDist().cdf(z)
    elif direction == "below":
        percentile = NormalDist().cdf(z) # The same as z score table
    else:
        raise ValueError("Direction must be 'above' or 'below'.")
    return f"The percentile of the distribution {direction} the point is: {percentile * 100:.2f}%"

print("Normal Distribution Percentile Calculator\nPlease enter if you want to find the percentile above or below a point in a normal distribution.")
point = float(input("Enter the point to find the percentile: "))
mean = float(input("Enter the mean of the distribution: "))
std_dev = float(input("Enter the standard deviation of the distribution: "))
direction = input("Enter the direction from the point (above/below): ").strip().lower()
print(percentile_calculation(z_score(point, mean, std_dev), direction))