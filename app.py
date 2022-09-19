import pandas
data = pandas.read_csv('2016data.csv')
data  

import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}) 

#Manipulating data
data.shape    # 40 rows and 8 columns
data.columns  # It has columns   



import pandas.plotting as plotting
plotting.scatter_matrix(data[['Race', 'Age Group', 'Hospital County']])
