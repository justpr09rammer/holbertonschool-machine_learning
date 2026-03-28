#!/usr/bin/env python3
'''applies convolution with same padding on grayscale images'''

import numpy as np


def convolve_grayscale_same(images, kernel):
    '''performs a same convolution on a collection of grayscale images

    Args:
        images: array of shape (m, h, w) containing grayscale images
            m: total number of images
            h: image height in pixels
            w: image width in pixels

        kernel: array of shape (kh, kw) used as the convolution filter
            kh: kernel height
            kw: kernel width

    Returns:
        numpy.ndarray containing the filtered images with same dimensions
    '''
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]

    padh = int(kh / 2)
    padw = int(kw / 2)
    pad = ((0, 0), (padh, padh), (padw, padw))

    convolved = np.zeros([m, h, w])
    imagepaded = np.pad(images, pad_width=pad, mode='constant',
                        constant_values=0)

    for x in range(h):
        for y in range(w):
            image = imagepaded[:, x:x+kh, y:y+kw]
            convolved[:, x, y] = np.multiply(image, kernel).sum(axis=(1, 2))

    return convolved
