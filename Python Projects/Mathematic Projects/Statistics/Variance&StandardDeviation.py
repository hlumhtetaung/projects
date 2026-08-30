import numpy as np

def calculate_variance(data):
    if len(data) == 0:
        print("Data list is empty. Variance cannot be calculated.")

    else:
        mean = np.mean(data)
        sum = 0
        for i in range(len(data)):
            sum += (data[i] - mean) ** 2
        variance = sum / len(data)
        return variance

def calculate_standard_deviation(data):
    if len(data) == 0:
        print("Data list is empty. Standard deviation cannot be calculated.")
    else:
        variance = calculate_variance(data)
        standard_deviation = np.sqrt(variance)
        return standard_deviation

data = []
data_count = int(input("Enter the amount of data you want to enter: "))
for i in range(data_count):
    value = float(input(f"Enter data point {i + 1}: "))
    data.append(value)

variance = calculate_variance(data)
standard_deviation = calculate_standard_deviation(data)
print(f"Variance: {variance}")
print(f"Standard Deviation: {standard_deviation}")


              