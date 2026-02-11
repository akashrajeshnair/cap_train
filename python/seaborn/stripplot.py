import matplotlib.pyplot as plt
import seaborn as sns

x = ['sum', 'mon',' tue', 'wed', 'thu', 'fri', 'sat']
y = [5,6,7,4,6,2,4]
ax = sns.stripplot(x=x, y=y)
ax.set(xlabel='days', ylabel='amount spent')
plt.title('daily spending')
plt.show()