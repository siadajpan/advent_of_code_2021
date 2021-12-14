import cv2
import numpy as np

import utils.file_io

DATA = utils.file_io.read_file('input.txt')
NP_DATA = np.array([np.array([int(n_) for n_ in n]) for n in DATA])


def part_1():
    # print(NP_DATA)
    h, w = NP_DATA.shape
    new_arr = np.ones((h + 2, w + 2)) * 99
    print(new_arr.shape)
    new_arr[1:-1, 1:-1] = NP_DATA
    # print(new_arr)
    found = []
    positions = np.zeros_like(NP_DATA)
    for i in range(1, new_arr.shape[0] - 1):
        for j in range(1, new_arr.shape[1] - 1):
            # print('el', new_arr[i][j])
            el = new_arr[i][j]
            if el < new_arr[i, j - 1] \
                    and el < new_arr[i - 1, j] \
                    and el < new_arr[i + 1, j] \
                    and el < new_arr[i, j + 1]:
                found.append(el)
                positions[i - 1, j - 1] = 1

    print(sum(np.array(found) + 1))
    return positions


def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue == 0] = 0

    cv2.imshow('labeled.png', labeled_img)
    cv2.waitKey()


def part_2():
    # positions = part_1()
    image = (NP_DATA < 9).astype(np.uint8) * 255
    image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)[1]
    cv2.imshow('b', image)
    h, w = image.shape[:2]
    new_arr = np.zeros((h + 2, w + 2), dtype=np.uint8)
    new_arr[1:-1, 1:-1] = image
    image = new_arr
    num_labels, labels_im = cv2.connectedComponents(image, 4, cv2.CV_32S)
    imshow_components(labels_im)
    areas = []
    for i in range(1, num_labels):
        areas.append(len(np.where(labels_im == i)[0]))

    print(np.prod(sorted(areas)[-3:]))


if __name__ == '__main__':
    part_2()
