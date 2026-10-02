import numpy as np
import matplotlib.pyplot as plt

def outlier_detection(data):
    if len(data) == 0:
        print("The data list is empty. Please provide a valid list of numbers.")
    else:

        # Finding first, second, and third quartiles
        data.sort()
        data = np.array(data)
        q2 = np.median(data) # split data in half
        q1 = np.median(data[data < q2]) # q1 is the median of the lower half
        q3 = np.median(data[data > q2]) # q3 is the median of the upper half

        # Finding interquartile range (IQR)
        iqr = q3 - q1

        # Finding lower fence and upper fence
        lower_fence = q1 - 1.5 * iqr
        upper_fence = q3 + 1.5 * iqr

        # Finding outliers
        outliers = data[(data < lower_fence) | (data > upper_fence)]
        return outliers

# Outlier detection
data_amount = int(input("Enter the number of data points: "))
data = []
for i in range(data_amount):
    data_point = float(input(f"Enter data point {i + 1}: "))
    data.append(data_point)

print("The outliers in the data are: " + str(outlier_detection(data)))

# Box plot for visualizations
plt.boxplot(data)
plt.title("Box plot of the data")
plt.xlabel("Data")
plt.ylabel("Values")
plt.show()