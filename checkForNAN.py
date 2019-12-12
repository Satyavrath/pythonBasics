import numpy as np

# create an array with nan and numeric elements
b = np.array([np.nan,1., 2.,np.nan,3.,4., 5])
print(b)
# checks and print whether the given index number is ' NOT(~) nan'
print(b[~np.isnan(b)])

