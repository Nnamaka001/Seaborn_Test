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


