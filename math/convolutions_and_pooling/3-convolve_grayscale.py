#!/usr/bin/env python3
'''Strided convolution on grayscale images'''

import numpy as np


def convolve_grayscale(images, kernel, padding='same', stride=(1, 1)):
    '''performs convolution on grayscale images with optional padding and stride

    Args:
        images: array of shape (m, h, w) containing multiple grayscale images
            m: number of images
            h: image height in pixels
            w: image width in pixels

        kernel: array of shape (kh, kw) used as the convolution filter
            kh: kernel height
            kw: kernel width

        padding: 'same', 'valid', or tuple (ph, pw)
            'same': output has same dimensions as input
            'valid': no padding applied
            tuple: ph and pw specify padding for height and width
            padding is applied with zeros

        stride: tuple (sh, sw)
            sh: stride along the height
            sw: stride along the width

    Returns:
        numpy.ndarray containing the convolved images
    '''
    m, h, w = images.shape
    kh, kw = kernel.shape
    sh, sw = stride

    if isinstance(padding, tuple):
        padh, padw = padding
    elif padding == 'same':
        padh = int((((h - 1) * sh - h + kh) / 2)) + 1
        padw = int((((w - 1) * sw - w + kw) / 2)) + 1
    elif padding == 'valid':
        padh = padw = 0

    nh = int(((h + (2 * padh) - kh) / sh)) + 1
    nw = int(((w + (2 * padw) - kw) / sw)) + 1

    convolved = np.zeros((m, nh, nw))
    pad = ((0, 0), (padh, padh), (padw, padw))
    imagepaded = np.pad(
        images,
        pad_width=pad,
        mode='constant',
        constant_values=0
    )

    for i in range(nh):
        for j in range(nw):
            x = i * sh
            y = j * sw
            convolved[:, i, j] = np.multiply(
                imagepaded[:, x:x+kh, y:y+kw], kernel
            ).sum(axis=(1, 2))

    return convolved
