import matplotlib.pyplot as plt
import numpy as np

def plot_examples():
    """
    This function demonstrates various plotting examples using Matplotlib.
    """

    x = np.linspace(0, 5, 11)  # Generate 11 points from 0 to 5
    y = x ** 2  # Calculate the square of each value in x

    print(y)  # Print the values of y

    # Uncomment the following lines to see different plot examples

    # Line Plot
    # plt.plot(x, y, 'rs-')  # 'r' is the color red, 's' is the marker style, '-' is the line style
    # plt.show()

    # Line Plot with Dots
    # plt.plot(x, y, 'yD:')  # 'y' is the color yellow, 'D' is the marker style, ':' is the line style
    # plt.show()

    # Histogram
    # plt.hist(x)  # Plot a histogram of the values in x
    # plt.show()

    # Pie Chart
    # plt.pie(x)  # Plot a pie chart using the values in x
    # plt.show()

    # Scatter Plot
    # plt.scatter(x, y)  # Plot a scatter plot using the values in x and y
    # plt.show()

    # Box Plot
    plt.boxplot(x)  # Plot a box plot using the values in x
    plt.show()

plot_examples()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,11) # 11 points from 0 to 5
y = x**2

print(y)

# plt.plot(x,y, 'rs-') # 'r' is the color red
# plt.show()

# plt.plot(x,y, 'yD:') # 'r' is the color red
# plt.show()

# plt.hist(x)
# plt.show()

# plt.pie(x)
# plt.show()

# plt.scatter(x,y)
# plt.show()

plt.boxplot(x)
plt.show()