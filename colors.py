import matplotlib.pyplot as plt
import numpy as np
import csv

color_set1 = [
    # [189,57,52],
    [237,137,0],
    [254,181,16]
]

color_set2 = [
    # [102,96,46],
    [167,152,0],
    [212,188,0]
]

color_set3 = [
    # [212,188,0],
    [187,169,1],
    [224,198,0]
]

white = [
    [255, 255, 255],
    [255, 255, 255],
    [255, 255, 255]
]

black = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

color_set_size = 2

def get_number_pixels(number):
    img_data = []
    with open("./mnist_train.csv", mode="r") as f:
        n = 1
        reader = csv.reader(f)
        for line in reader:
            if int(line[0]) == number:
                if np.random.random() <= 1/n:
                    img_data = np.array([int(x) for x in line[1:]])
                n += 1

    return np.around((img_data / 255) - 0.3)

if __name__ == "__main__":
    secret_number = np.random.randint(0, 10)
    colors = get_number_pixels(secret_number)

    dim = int(np.sqrt(colors.size))
    color_sets = [color_set3, color_set2]
    colors1 = np.array([color_sets[int(idx)][np.random.randint(0, color_set_size)] for idx in colors]) / 255
    color_sets = [black, white]
    colors2 = np.array([color_sets[int(idx)][np.random.randint(0, color_set_size)] for idx in colors]) / 255
    plt.imshow(colors1.reshape(dim, dim, 3))
    plt.show()
    plt.imshow(colors2.reshape(dim, dim, 3))
    plt.show()


