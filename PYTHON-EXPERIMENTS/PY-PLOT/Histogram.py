import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(500)

plt.hist(data, bins=20)
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Histogram')
plt.show()