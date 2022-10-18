import matplotlib.pyplot as plt
import mnist as mnist
from tqdm import tqdm
from model import MnistSolver


def draw_point(point_value, label):
    color_value = hex(point_value)[2:]
    color = "#{0:0>6}".format(color_value)
    random_position = np.random.randint(0, 100)
    plt.scatter(point_value, random_position, c=color, s=100)
    plt.text(point_value, random_position, label)


if __name__ == '__main__':
    import numpy as np
    train_dataset, train_labels = mnist.test_images(), mnist.test_labels()

    model = MnistSolver(train_dataset.shape[1] * train_dataset.shape[2])
    for im, label in tqdm(zip(train_dataset, train_labels)):
        # flat_image = im.flatten()
        # active_pixels = np.where(flat_image > 0)[0]
        # point_value = int(np.mean([model.get_node_color(p) for p in active_pixels]))

        point_value = model.process_image(im)
        draw_point(point_value, label)
    plt.show()
