#!/usr/bin/env python3
'''Convolution on multi-channel grayscale images'''

import numpy as np


def convolve_channels(images, kernel, padding='same', stride=(1, 1)):
    '''performs convolution on multi-channel images with optional padding and stride

    Args:
        images: array of shape (m, h, w, c) containing multiple images
            m: number of images
            h: height of each image
            w: width of each image
            c: number of channels

        kernel: array of shape (kh, kw, c) representing the convolution filter
            kh: kernel height
            kw: kernel width
            c: number of channels (must match image channels)

        padding: 'same', 'valid', or tuple (ph, pw)
            'same': output has same spatial dimensions as input
            'valid': no padding applied
            tuple: (ph, pw) specifies padding for height and width
            padding is applied with zeros

        stride: tuple (sh, sw)
            sh: stride along height
            sw: stride along width

    Returns:
        numpy.ndarray containing the convolved images
    '''
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = kernel.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    sh = stride[0]
    sw = stride[1]

    if type(padding) is tuple:
        padh = padding[0]
        padw = padding[1]
    elif padding == 'same':
        padh = int((((h - 1) * sh - h + kh) / 2)) + 1
        padw = int((((w - 1) * sw - w + kw) / 2)) + 1
    elif padding == 'valid':
        padh = padw = 0

    nh = int(((h + (2 * padh) - kh) / sh)) + 1
    nw = int(((w + (2 * padw) - kw) / sw)) + 1
    conv = np.zeros((m, nh, nw))

    pad = ((0, 0), (padh, padh), (padw, padw), (0, 0))
    imagepaded = np.pad(images, pad_width=pad, mode='constant', constant_values=0)

    for i in range(nh):
        for j in range(nw):
            x = i * sh
            y = j * sw
            image = imagepaded[:, x:x+kh, y:y+kw, :]
            conv[:, i, j] = np.multiply(image, kernel).sum(axis=(1, 2, 3))

    return conv
