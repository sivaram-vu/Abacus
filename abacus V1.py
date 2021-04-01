#%%

# %%
import matplotlib.pyplot as plt

point1 = [2, 1]
point2 = [2, 6]

x_values = [point1[0], point2[0]]

y_values = [point1[1], point2[1]]

ax = plt.gca()

ax.plot(x_values, y_values)
ax.plot([3,3], [1,6])
ax.plot([1,4], [5,5])

# circle1 = plt.Circle((2, 5+0.2+0.04), 0.2, color='r')
# circle2 = plt.Circle((2, 5-0.2-0.04), 0.2, color='r')

# ax.add_patch(circle1)
# ax.add_patch(circle2)

import random
num = random.randint(1,101)

#print (num, num/10, num%10)
radius=0.4
number_of_10s = int(num/10)
if number_of_10s >= 5:
    circle1 = plt.Circle((2, 5+radius+0.04), radius, color='r')
    ax.add_patch(circle1)
    number_of_10s = number_of_10s - 5


for i in range(1, number_of_10s+1):
    circle2 = plt.Circle((2, 5-((i-1)*2*radius + radius)-0.04), radius, color='r')
    ax.add_patch(circle2)

number_of_1s = num%10

if number_of_1s >= 5:
    circle1 = plt.Circle((3, 5+radius+0.04), radius, color='r')
    ax.add_patch(circle1)
    number_of_1s = number_of_1s - 5


for i in range(1, number_of_1s+1):
    circle2 = plt.Circle((3, 5-((i-1)*2*radius + radius)-0.04), radius, color='r')
    ax.add_patch(circle2)

ax.axis('off')
print ('')

# %%
