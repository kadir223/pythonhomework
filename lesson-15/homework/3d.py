import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x = np.linspace(-10, 10, 100)
y = x**2 - 4*x + 4
plt.figure()
plt.plot(x, y, label='$f(x) = x^2 - 4x + 4$', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Basic Plot')
plt.legend()
plt.grid()
plt.show()

# 2. Sine and Cosine Plot
x = np.linspace(0, 2*np.pi, 100)
plt.figure()
plt.plot(x, np.sin(x), label='sin(x)', linestyle='-', color='red', marker='o')
plt.plot(x, np.cos(x), label='cos(x)', linestyle='--', color='blue', marker='x')
plt.xlabel('x')
plt.ylabel('Value')
plt.title('Sine and Cosine Functions')
plt.legend()
plt.grid()
plt.show()

# 3. Subplots
x = np.linspace(0, 5, 100)
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, x**3, color='purple')
axes[0, 0].set_title("$f(x) = x^3$")
axes[0, 1].plot(x, np.sin(x), color='green')
axes[0, 1].set_title("$f(x) = \sin(x)$")
axes[1, 0].plot(x, np.exp(x), color='orange')
axes[1, 0].set_title("$f(x) = e^x$")
axes[1, 1].plot(x, np.log(x+1), color='brown')
axes[1, 1].set_title("$f(x) = \log(x+1)$")
plt.tight_layout()
plt.show()

# 4. Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, color='blue', marker='o', alpha=0.6)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')
plt.grid()
plt.show()

# 5. Histogram
values = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(values, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution')
plt.show()

# 6. 3D Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.cos(X**2 + Y**2)
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Plot')
plt.show()

# 7. Bar Chart
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=['red', 'green', 'blue', 'orange', 'purple'])
plt.xlabel('Products')
plt.ylabel('Sales')
plt.title('Sales Data')
plt.show()

# 8. Stacked Bar Chart
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [5, 7, 8, 6]
category_B = [4, 6, 7, 5]
category_C = [3, 4, 5, 6]
plt.figure()
plt.bar(time_periods, category_A, label='Category A', color='red')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='blue')
plt.bar(time_periods, category_C, bottom=np.array(category_A)+np.array(category_B), label='Category C', color='green')
plt.xlabel('Time Periods')
plt.ylabel('Values')
plt.title('Stacked Bar Chart')
plt.legend()
plt.show()