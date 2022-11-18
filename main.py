'''import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([10, 5, 8, 9, 4, 6, 7])
plt.show()'''

'''import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([10, 5, 7, 6, 8, 9], hist = False)
plt.show()'''

'''from numpy import random
num = random.normal(size = (4,7))
print(num)'''

'''from numpy import random
num = random.normal(size = (3,5))
print(num)'''

'''from numpy import random
num = random.normal(loc = 2, scale = 3, size = (3,5))
print(num)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size = 500), hist = False)
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size = 750))
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(size = 750), kde = False)
plt.show()'''

'''from numpy import random
num = random.binomial(n = 5, p = 0.5, size = 10)
print(num)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n = 5, p = 0.5, size = 10), kde = False)
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n = 5, p = 0.5, size = 10))
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n = 5, p = 0.5, size = 10), hist = False)
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')
plt.show()'''

'''from numpy import random
num = random.poisson(lam = 3, size = 10)
print(num)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam = 3, size = 750))
plt.show()'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.poisson(lam = 3, size = 750))
sns.distplot(random.binomial(n = 100, p = 0.5, size = 750), label = "binomial")
sns.distplot(random.normal(loc=100, scale=0.75, size = 750), label = "normal")
plt.show()'''

'''import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme()
df = sns.load_dataset("penguins")
sns.distplot(df["flipper_length_mm"])
plt.show()'''

#Create a 2x3 uniform distribution sample
'''from numpy import random
x = random.uniform(size=(2, 3))
print(x)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()'''

# Draw out a sample for dice roll (multinominal distribution is used)
'''from numpy import random
x = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(x)'''

'''from numpy import random  #For multinomial VISUALIZATION
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size = 1000), hist = False)
plt.show()'''

#Draw out a sample for exponential distribution with 2.0 scale with 2x3 size:

'''from numpy import random
x = random.exponential(scale=2, size=(2,3))
print(x)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.exponential(size=1000), hist =  False)
plt.show()'''

#Draw out a sample for a chi squared distribution with degree of freedom 2, size 2x3:

'''from numpy import random
x = random.chisquare(df=2, size=(2,3))
print(x)'''

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.chisquare(df=2, size=1000), hist = False)
plt.show()'''

#VISUALIZATION FOR PARETO DISTRIBUTION

'''from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot(random.pareto(a=2, size=1000), kde = False)
plt.show()'''

'''x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
    z.append(i + j)
    print(z)'''

'''import numpy as np
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)'''

'''import numpy as np
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)'''

'''import numpy as np
def myadd(x, y):
    return x + y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))'''

#LCM for individual numbers
'''import numpy as np
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)'''

#LCM for arrays
'''import numpy as np
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)'''

#Find LCM of all values of an array where the array contains integers from 1 to 10
'''import numpy as np
arr = np.arange(1, 11) #arange() will take integers from 1 to 10. 11 won't be included
x = np.lcm.reduce(arr)
print(x)'''

'''import numpy as np
x = np.sin(np.pi/2)
print(x)'''

'''import numpy as np
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)'''

'''import numpy as np
arr = np.array([1,1,1,2,3,4,5,5,6,7])
x = np.unique(arr)
print(x)'''

'''import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.union1d(arr1, arr2)
print(newarr)'''

'''import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.intersect1d(arr1, arr2)
print(newarr)'''

'''import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
newarr = np.setdiff1d(arr1, arr2)
newarr1 = np.setxor1d(arr1, arr2)
print(newarr)
print(newarr1)'''