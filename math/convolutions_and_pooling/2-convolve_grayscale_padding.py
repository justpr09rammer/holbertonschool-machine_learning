#!/usr/bin/env python3
'''applies convolution with custom padding on grayscale images'''

import numpy as np


def convolve_grayscale_padding(images, kernel, padding):
    '''performs convolution on grayscale images with specified padding

    Args:
        images: array of shape (m, h, w) containing multiple grayscale images
            m: number of images
            h: height of each image in pixels
            w: width of each image in pixels

        kernel: array of shape (kh, kw) used as the convolution filter
            kh: kernel height
            kw: kernel width

        padding: tuple (ph, pw)
            ph: padding along image height
            pw: padding along image width
            the padding is applied with zeros

    Returns:
        numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]

    padh = padding[0]
    padw = padding[1]
    pad = ((0, 0), (padh, padh), (padw, padw))

    nh = h + (2 * padh) - kh + 1
    nw = w + (2 * padw) - kw + 1
    convolved = np.zeros([m, nh, nw])

    imagepaded = np.pad(images, pad_width=pad, mode='constant',
                        constant_values=0)

    for x in range(nh):
        for y in range(nw):
            image = imagepaded[:, x:x+kh, y:y+kw]
            convolved[:, x, y] = np.multiply(image, kernel).sum(axis=(1, 2))

    return convolved
