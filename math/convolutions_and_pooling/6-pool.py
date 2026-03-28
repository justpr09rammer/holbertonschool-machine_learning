#!/usr/bin/env python3
'''Pooling operations on multi-channel images'''

import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    '''applies pooling on multi-channel images

    Args:
        images: array of shape (m, h, w, c) containing multiple images
            m: number of images
            h: height of each image
            w: width of each image
            c: number of channels

        kernel_shape: tuple (kh, kw) specifying pooling window
            kh: height of the window
            kw: width of the window

        stride: tuple (sh, sw)
            sh: stride along height
            sw: stride along width

        mode: pooling type
            'max': max pooling
            'avg': average pooling

    Returns:
        numpy.ndarray containing the pooled images
    '''
    m = images.shape[0]
    h = images.shape[1]
    w = images.shape[2]
    c = images.shape[3]
    kh = kernel_shape[0]
    kw = kernel_shape[1]
    sh = stride[0]
    sw = stride[1]

    pooling = np.max if mode == 'max' else np.average

    nh = int(((h - kh) / sh)) + 1
    nw = int(((w - kw) / sw)) + 1
    conv = np.zeros((m, nh, nw, c))

    for i in range(nh):
        for j in range(nw):
            x = i * sh
            y = j * sw
            conv[:, i, j, :] = pooling(images[:, x:x+kh, y:y+kw, :], axis=(1, 2))

    return conv
