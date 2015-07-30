import csv
import random

def load_csv(image_path):
    numbers = []

    with open(image_path, 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        for row in reader:
            numbers_map = {'label': row[0]}
            numbers_map['pixels'] = row[1:]
            numbers.append(numbers_map)

    return numbers

def split_vector(vector):
    v1 = []
    v2 = []

    for element in vector:
        if random.randrange(0, 2) == 0:
            v1.append(element)
        else:
            v2.append(element)

    return v1, v2