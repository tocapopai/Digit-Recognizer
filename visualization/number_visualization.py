import csv
import numpy as np
import scipy.misc as sm
import scipy.ndimage as nd

def createImage(digit):

    digit_image = np.zeros((28, 28))
    size = 28

    for row in range(0, size-1):
        for column in range(0, size-1):
            index = row*size +column
            digit_image[row][column] = digit[index]

    return digit_image        


#Opening csv file and loading it into a numpy array
with open('../data/train.csv', 'rb') as data:
    reader = csv.reader(data, delimiter=',')
    next(reader)
    numbers = np.array(list(reader)).astype(int)

'''
    Extracting the first column of each line of the array. The first column has the
    value of the handwritten digit
'''
digits = numbers[:, [0]]
handwritten = numbers[:,1:]


print("Enter the row from the csv file that you which to see the digit")
num_image = input()
num_image-=1

#Displaying the digit image accordingly to the user input
digit_image = createImage(handwritten[num_image]) 
digit_image = nd.zoom(digit_image, 8, order=3)
img = sm.toimage(digit_image)
img.show()
