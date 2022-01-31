# Matplotlib Histogram - 2

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
  
# giving two age groups data
age_g1 = [1, 3, 5, 10, 15, 17, 18, 16, 19, 21,
          23, 28, 30, 31, 33, 38, 32, 40, 45, 
          43, 49, 55, 53, 63, 66, 85, 80, 57, 
          75, 93, 95]
  
age_g2 = [6, 4, 15, 17, 19, 21, 28, 23, 31, 36,
          39, 32, 50, 56, 59, 74, 79, 34, 98, 97,
          95, 67, 69, 92, 45, 55, 77, 76, 85]
  
# plotting first histogram
plt.hist(age_g1, label='Age group1', alpha=.7, color='red')
  
# plotting second histogram
plt.hist(age_g2, label="Age group2", alpha=.5,
         edgecolor='black', color='yellow')
plt.legend()
  
# Showing the plot using plt.show()
plt.show()


data = sns.load_dataset('iris')

# plotting more than 2 overlapping histograms
plt.hist(data['sepal_width'], 
         alpha=0.5, 
         label='sepal_width',
         color='red') # customized color parameter
  
plt.hist(data['petal_width'], 
         alpha=0.5,
         label='petal_width',
         color='green')
  
plt.hist(data['petal_length'], 
         alpha=0.5,
         label='petal_length',
         color='yellow')
  
plt.hist(data['sepal_length'], 
         alpha=0.5,
         label='sepal_length',
         color='purple')
  
plt.legend(loc='upper right')
plt.show()