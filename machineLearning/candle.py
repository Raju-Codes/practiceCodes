import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

data = [
    # Open, High, Low, Close
    (100, 110, 95, 105),
    (105, 108, 100, 103),
    (103, 112, 98, 110),
    (110, 115, 105, 108),
    (108, 120, 107, 118),
]

fig, ax = plt.subplots()

for i, (open_price, high, low, close) in enumerate(data):

    # Green if price went up, red if price went down
    color = "green" if close >= open_price else "red"

    # Wick
    ax.plot(
        [i, i],
        [low, high],
        color=color
    )

    # Candle body
    bottom = min(open_price, close)
    height = abs(close - open_price)

    candle = Rectangle(
        (i - 0.3, bottom),
        0.6,
        height,
        facecolor=color,
        edgecolor=color
    )

    ax.add_patch(candle)

ax.set_title("Candlestick Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Price")

plt.show()
