import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [10, 12, 11, 4, 5, 90, 52, 432, 57]

plt.plot(x, y, color='red', linewidth=3, linestyle='dashed', marker='*', markerfacecolor='brown')
plt.show()

plt.candle(x,y, color='red')
plt.show()
