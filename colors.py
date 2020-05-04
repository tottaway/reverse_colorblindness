import matplotlib.pyplot as plt
import numpy as np
import csv

# red and orange
color_set1 = [
    [237,137,0],
    [254,181,16]
]

# red and orange to a colorblind person
color_set2 = [
    [167,152,0],
    [212,188,0]
]

# greens
color_set3 = [
    [187,169,1],
    [224,198,0]
]

white = [
    [255, 255, 255],
    [255, 255, 255]
]

black = [
    [0, 0, 0],
    [0, 0, 0]
]

color_set_size = 2

def get_number_pixels(number):
    """
    returns an unrolled list of pixel brightnesses corresponding to a
    handwritten image of the input number from the mnist training set
    """
    img_data = []
    # loop over the dataset and select a image uniformly at random by replacing
    # one's current choice at each step, n, with probability 1/n
    with open("./mnist_train.csv", mode="r") as f:
        n = 1
        reader = csv.reader(f)
        for line in reader:
            if int(line[0]) == number:
                if np.random.random() <= 1/n:
                    img_data = np.array([int(x) for x in line[1:]])
                n += 1

    # scale data and force to be all ones and zeros
    return np.around((img_data / 255) - 0.3)

if __name__ == "__main__":
    # pick a number
    secret_number = np.random.randint(0, 10)
    colors = get_number_pixels(secret_number)

    dim = int(np.sqrt(colors.size))

    # display image 
    color_sets = [color_set3, color_set2]
    colors1 = np.array([color_sets[int(idx)][np.random.randint(0, color_set_size)] for idx in colors]) / 255
    plt.imshow(colors1.reshape(dim, dim, 3))
    plt.show()

    # display base truth image with black and white
    color_sets = [black, white]
    colors2 = np.array([color_sets[int(idx)][np.random.randint(0, color_set_size)] for idx in colors]) / 255
    plt.imshow(colors2.reshape(dim, dim, 3))
    plt.show()


