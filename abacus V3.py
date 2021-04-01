#%%
numbers = list(range(1, 101))


# %%
import matplotlib.pyplot as plt

y_min, y_max = (1, 12)
x_1s, x_10s = (6, 3)
x_bar_min, x_bar_max, y_bar = (1, 8, 10)
radius=1

plt.figure(figsize=(20,10))
ax = plt.gca()

ax.plot([x_10s, x_10s], [y_min, y_max])
ax.plot([x_1s, x_1s], [y_min, y_max])
ax.plot([x_bar_min, x_bar_max], [y_bar, y_bar])

import random
num = random.choice(numbers)
numbers.remove(num)
ax.margins(0.05)
def plot_beeds(bar_value, rod, bar_place):
    if bar_value >= 5:
        circle1 = plt.Circle((rod, bar_place+radius+0.04), radius, color='r')
        ax.add_patch(circle1)
        bar_value = bar_value - 5

    for i in range(1, bar_value+1):
        circle2 = plt.Circle((rod, bar_place-((i-1)*2*radius + radius)-0.04), radius, color='r')
        ax.add_patch(circle2)

number_of_10s = int(num/10)
plot_beeds(number_of_10s, x_10s, y_bar)

number_of_1s = num%10
plot_beeds(number_of_1s, x_1s, y_bar)

ax.add_patch(plt.Circle((x_1s, y_bar), 0.2, color='k', linewidth=8, fill=False))
ax.add_patch(plt.Circle((x_1s, y_bar), 0.2, color='w'))

ax.axis('off')
print ('')





# %%
