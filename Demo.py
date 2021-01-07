
import os
import random
import pandas as pd
import numpy as np
import cv2
import math
import re
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from itertools import chain
from skimage.io import imread, imshow, concatenate_images
from skimage.transform import resize
from tqdm import tqdm_notebook
from skimage.morphology import label
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tqdm.notebook import tqdm
from keras.models import Model, load_model
from keras.layers import Input, BatchNormalization, Activation, Dense, Dropout, DepthwiseConv2D, Flatten
from keras.layers.core import Lambda, RepeatVector, Reshape
from keras.layers.convolutional import Conv2D, Conv2DTranspose
from keras.layers.pooling import MaxPooling2D, GlobalMaxPool2D
from keras.layers.merge import concatenate, add
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from keras import backend as K


def conv2d_block(input_tensor, n_filters, kernel_size=3, batchnorm=True):
    # first layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(input_tensor)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("relu")(x)
    # second layer
    x = Conv2D(filters=n_filters, kernel_size=(kernel_size, kernel_size), kernel_initializer="he_normal",
               padding="same")(x)
    if batchnorm:
        x = BatchNormalization()(x)
    x = Activation("relu")(x)
    return x


def unet_en(input_img, n_filters=16, dropout=0.3, batchnorm=True):
    c1 = conv2d_block(input_img, n_filters=n_filters * 1, kernel_size=3, batchnorm=batchnorm)
    p1 = MaxPooling2D((2, 2))(c1)
    p1 = Dropout(dropout * 0.5)(p1)

    c2 = conv2d_block(p1, n_filters=n_filters * 2, kernel_size=3, batchnorm=batchnorm)
    p2 = MaxPooling2D((2, 2))(c2)
    p2 = Dropout(dropout)(p2)

    c3 = conv2d_block(p2, n_filters=n_filters * 4, kernel_size=3, batchnorm=batchnorm)
    p3 = MaxPooling2D((2, 2))(c3)
    p3 = Dropout(dropout)(p3)

    c4 = conv2d_block(p3, n_filters=n_filters * 8, kernel_size=3, batchnorm=batchnorm)
    p4 = MaxPooling2D((2, 2))(c4)
    p4 = Dropout(dropout)(p4)

    c5 = conv2d_block(p4, n_filters=n_filters * 16, kernel_size=3, batchnorm=batchnorm)
    return [c1, c2, c3, c4, c5]

    # expansive path


def unet_dec(input_img, layers, n_filters=16, dropout=0.4, batchnorm=True):
    c1, c2, c3, c4, _ = layers

    u6 = Conv2DTranspose(n_filters * 8, (3, 3), strides=(2, 2), padding='same')(input_img)
    u6 = concatenate([u6, c4])
    u6 = Dropout(dropout)(u6)
    c6 = conv2d_block(u6, n_filters=n_filters * 8, kernel_size=3, batchnorm=batchnorm)

    u7 = Conv2DTranspose(n_filters * 4, (3, 3), strides=(2, 2), padding='same')(c6)
    u7 = concatenate([u7, c3])
    u7 = Dropout(dropout)(u7)
    c7 = conv2d_block(u7, n_filters=n_filters * 4, kernel_size=3, batchnorm=batchnorm)

    u8 = Conv2DTranspose(n_filters * 2, (3, 3), strides=(2, 2), padding='same')(c7)
    u8 = concatenate([u8, c2])
    u8 = Dropout(dropout)(u8)
    c8 = conv2d_block(u8, n_filters=n_filters * 2, kernel_size=3, batchnorm=batchnorm)

    u9 = Conv2DTranspose(n_filters * 1, (3, 3), strides=(2, 2), padding='same')(c8)
    u9 = concatenate([u9, c1], axis=3)
    u9 = Dropout(dropout)(u9)
    c9 = conv2d_block(u9, n_filters=n_filters * 1, kernel_size=3, batchnorm=batchnorm)

    return c9


def unet_half_en(input_img, n_filters=16, dropout=0.3, batchnorm=True):
    # contracting pat
    c1 = conv2d_block(input_img, n_filters=n_filters * 1, kernel_size=3, batchnorm=batchnorm)
    p1 = MaxPooling2D((2, 2))(c1)
    p1 = Dropout(dropout * 0.5)(p1)

    c2 = conv2d_block(p1, n_filters=n_filters * 2, kernel_size=3, batchnorm=batchnorm)
    p2 = MaxPooling2D((2, 2))(c2)
    p2 = Dropout(dropout)(p2)

    c3 = conv2d_block(p2, n_filters=n_filters * 4, kernel_size=3, batchnorm=batchnorm)
    p3 = MaxPooling2D((2, 2))(c3)
    p3 = Dropout(dropout)(p3)

    c4 = conv2d_block(p3, n_filters=n_filters * 16, kernel_size=3, batchnorm=batchnorm)
    return [c1, c2, c3, c4]


def unet_half_dec(input_img, n_filters=16, dropout=0.4, batchnorm=True):
    c1, c2, c3, x = input_img

    u4 = Conv2DTranspose(n_filters * 2, (3, 3), strides=(2, 2), padding='same')(x)
    u4 = concatenate([u4, c3])
    u4 = Dropout(dropout)(u4)
    c4 = conv2d_block(u4, n_filters=n_filters * 4, kernel_size=3, batchnorm=batchnorm)

    u5 = Conv2DTranspose(n_filters * 1, (3, 3), strides=(2, 2), padding='same')(c4)
    u5 = concatenate([u5, c2], axis=3)
    u5 = Dropout(dropout)(u5)
    c5 = conv2d_block(u5, n_filters=n_filters * 2, kernel_size=3, batchnorm=batchnorm)

    u6 = Conv2DTranspose(n_filters * 2, (3, 3), strides=(2, 2), padding='same')(c5)
    u6 = concatenate([u6, c1])
    u6 = Dropout(dropout)(u6)
    c6 = conv2d_block(u6, n_filters=n_filters * 1, kernel_size=3, batchnorm=batchnorm)

    u7 = Conv2DTranspose(n_filters * 2, (3, 3), strides=(2, 2), padding='same')(c6)

    return u7


def dilated_Conv(en1, en2):
    input_img = add([en1, en2])
    dilate3 = Conv2D(64, 3, activation='relu', padding='same', dilation_rate=4, kernel_initializer='he_normal')(
        input_img)
    b9 = BatchNormalization()(dilate3)
    b9 = Dropout(rate=0.2)(b9)

    dilate4 = Conv2D(64, 3, activation='relu', padding='same', dilation_rate=8, kernel_initializer='he_normal')(b9)
    b10 = BatchNormalization()(dilate4)
    b10 = Dropout(rate=0.2)(b10)

    dilate5 = Conv2D(64, 3, activation='relu', padding='same', dilation_rate=16, kernel_initializer='he_normal')(b10)
    b11 = BatchNormalization()(dilate5)
    b11 = Dropout(rate=0.2)(b11)

    dilate6 = Conv2D(64, 3, activation='relu', padding='same', dilation_rate=32, kernel_initializer='he_normal')(b11)
    return b11


def reconstruct(dec, dec_half):
    out = concatenate([dec, dec_half])
    out = Conv2D(3, (1, 1), activation='sigmoid')(out)
    return out


im_height = 1024
im_width = 1600
input_img_half = Input((im_height//2, im_width//2, 3), name='img_half')
input_img = Input((im_height, im_width, 3), name='img')

encoding = unet_en(input_img, n_filters=16, dropout=0.05, batchnorm=True)
half_encoding = unet_half_en(input_img_half, n_filters=16, dropout=0.05, batchnorm=True)

bottleneck = dilated_Conv(encoding[-1], half_encoding[-1])

decoding = unet_dec(bottleneck, encoding, n_filters=16, dropout=0.05, batchnorm=True)
half_decoding = unet_half_dec(half_encoding, n_filters=16, dropout=0.05, batchnorm=True)

output = reconstruct(decoding, half_decoding)

derain = Model(inputs=[input_img, input_img_half], outputs = [output])
dehaze = Model(inputs=[input_img, input_img_half], outputs = [output])
desnow = Model(inputs=[input_img, input_img_half], outputs = [output])

dehaze.summary()

derain.load_weights('DERAIN_400x400_25epochs.h5')


def sorting(x):
    return int(re.findall("\d+", x)[0])


def get_datafortest(path):
    ids = next(os.walk(path))[2]
    # ids = sorted(ids, key=sorting)
    print(ids)

    X = np.zeros((len(ids), im_height, im_width, 3), dtype=np.float32)
    X_half = np.zeros((len(ids), im_height // 2, im_width // 2, 3), dtype=np.float32)

    for n, id_ in tqdm_notebook(enumerate(ids), total=len(ids), disable=True):
        # Load images
        img = load_img(path + id_, grayscale=False)
        x_img = img_to_array(img)
        x_img = resize(x_img, (im_height, im_width, 3), mode='constant', preserve_range=True)
        x_img_half = resize(x_img, (im_height // 2, im_width // 2, 3), mode='constant', preserve_range=True)
        X[n] = x_img / 255
        X_half[n] = x_img_half / 255
        if n == 300:
            return X, X_half

    return X, X_half

import imageio

path_derain = '/home/user/JH/Demo/derain'
rainy, rainy_half = get_datafortest(path_derain)
Rainy_pred = derain.predict([rainy, rainy_half])
imageio.mimwrite('derain_demo2.mp4', Rainy_pred , fps = 30)