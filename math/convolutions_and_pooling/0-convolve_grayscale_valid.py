#!/usr/bin/env python3
'''applies convolution to grayscale image data'''

import numpy as np


def convolve_grayscale_valid(images, kernel):
    '''executes a valid convolution on a set of grayscale images

    Args:
        images: array of shape (m, h, w) representing multiple grayscale images
            m: number of images
            h: height of each image in pixels
            w: width of each image in pixels

        kernel: array of shape (kh, kw) representing the convolution filter
            kh: kernel height
            kw: kernel width

    Returns:
        numpy.ndarray containing the convolution results for each image
    '''
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    n_h = h - kh + 1
    n_w = w - kw + 1

    # initialize the output array for convolved results
    convolved = np.zeros([m, n_h, n_w])

    # iterate over each possible position in the output
    for x in range(n_h):
        for y in range(n_w):
            # extract the corresponding region from each image
            image = images[:, x:x+kh, y:y+kw]

            # perform element-wise multiplication with the kernel
            # then sum across height and width dimensions
            convolved[:, x, y] = np.multiply(image, kernel).sum(axis=(1, 2))

    # optional check to confirm expected output dimensions
    # assert(convolved.shape == (m, n_h, n_w))

    return convolved
