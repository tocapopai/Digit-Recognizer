import csv
import numpy as np

#Opening csv file and loading it into a numpy array
with open('../data/dummy.csv', 'rb') as data:
    reader = csv.reader(data, delimiter=',')
    numbers = np.array(list(reader)).astype(int)

'''
    Extracting the first column of each line of the array. The first column has the
    value of the handwritten digit
'''
digits = numbers[:, [0]]
handwritten = numbers[:,1:]

