import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
sns.boxplot(x='day', y='total_bill', data=tips, hue='smoker')
plt.title("Total bill distribution by day and smoking status")
plt.show()