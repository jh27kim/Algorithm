
import os
import random
import pandas as pd
from PIL import Image
import numpy as np
import cv2
import math
import re
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from itertools import chain
from skimage.io import imread, imshow, concatenate_images
from skimage.transform import resize
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
from tqdm.notebook import tqdm

import cv2
import numpy as np
import os

'''
# Playing video from file:
cap = cv2.VideoCapture('heavy_rain.mp4')

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    name = str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''


def canny_test(X):
    edges = []
    temp = []
    for img in X:
        edge = cv2.Canny((img * 255).astype(np.uint8), threshold_x, threshold_y)
        temp.append(np.sum(edge) / 255)
    temp = np.asarray(temp)
    edges.append(temp)
    edges = np.asarray(edges)
    return edges


def hsvmap(X):
    hsv_blue = []
    for img in X:
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
        hsv_blue.append(np.sum(mask) / (CF_width * CF_height))
    hsv_blue = np.asarray(hsv_blue)
    return hsv_blue


def test_generator_multiple(G):
    while True:
        Y = G.next()
        Y2 = canny_test(Y[0])
        Y3 = hsvmap(Y[0])
        yield [Y[0], Y2[0], Y3], Y[1]  # Yield both images and their mutual label


test_datagen = ImageDataGenerator(rescale=1. / 255, )
CF_height = 160
CF_width = 160

threshold_x = 150
threshold_y = 50

lower_blue = np.array([90, 50, 50])
upper_blue = np.array([110, 255, 255])
batch_size = 16

weather_in = Input(shape=(CF_height, CF_width, 3))

weather = Conv2D(8, (2, 2), padding='same', activation='relu')(weather_in)
weather = BatchNormalization()(weather)
weather = DepthwiseConv2D(8, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(16, (1, 1))(weather)
weather = BatchNormalization()(weather)
weather = DepthwiseConv2D(16, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(32, (1, 1))(weather)
weather = BatchNormalization()(weather)
weather = DepthwiseConv2D(32, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(32, (1, 1))(weather)
weather = DepthwiseConv2D(32, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(64, (1, 1))(weather)
weather = BatchNormalization()(weather)
weather = DepthwiseConv2D(64, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(64, (1, 1))(weather)
weather = DepthwiseConv2D(64, (2, 2), padding='same', activation='relu')(weather)
weather = Conv2D(128, (1, 1))(weather)
weather = BatchNormalization()(weather)
weather = MaxPooling2D((2, 2))(weather)

weather = Flatten()(weather)

edge_in = Input(shape=(1,))
edge = Dense(1, activation='relu')(edge_in)

hsv_in = Input(shape=(1,))
hsv = Dense(1, activation='relu')(hsv_in)

merged = concatenate([weather, edge, hsv])

fc = Dense(128, activation='relu')(merged)
drop = Dropout(0.5)(fc)
fc = Dense(32, activation='relu')(drop)
output = Dense(4, activation='softmax')(fc)

combinedModel = Model(inputs=[weather_in, edge_in, hsv_in], outputs=[output])

combinedModel.summary()


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

im_height = 160
im_width = 160
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


# Dark Channel property

def DarkChannel(im, sz):
    b, g, r = cv2.split(im)
    dc = cv2.min(cv2.min(r, g), b)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (sz, sz))
    dark = cv2.erode(dc, kernel)
    return dark


def AtmLight(im, dark):
    [h, w] = im.shape[:2]
    imsz = h * w
    numpx = int(max(math.floor(imsz / 1000), 1))
    darkvec = dark.reshape(imsz, 1)
    imvec = im.reshape(imsz, 3)

    indices = darkvec.argsort()
    indices = indices[imsz - numpx::]

    atmsum = np.zeros([1, 3])
    for ind in range(1, numpx):
        atmsum = atmsum + imvec[indices[ind]]

    A = atmsum / numpx
    return A


def TransmissionEstimate(im, A, sz):
    omega = 0.95
    im3 = np.empty(im.shape, im.dtype)

    for ind in range(0, 3):
        im3[:, :, ind] = im[:, :, ind] / A[0, ind]

    transmission = 1 - omega * DarkChannel(im3, sz)
    return transmission


def Guidedfilter(im, p, r, eps):
    mean_I = cv2.boxFilter(im, cv2.CV_64F, (r, r))
    mean_p = cv2.boxFilter(p, cv2.CV_64F, (r, r))
    mean_Ip = cv2.boxFilter(im * p, cv2.CV_64F, (r, r))
    cov_Ip = mean_Ip - mean_I * mean_p

    mean_II = cv2.boxFilter(im * im, cv2.CV_64F, (r, r))
    var_I = mean_II - mean_I * mean_I

    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I

    mean_a = cv2.boxFilter(a, cv2.CV_64F, (r, r))
    mean_b = cv2.boxFilter(b, cv2.CV_64F, (r, r))

    q = mean_a * im + mean_b
    return q


def TransmissionRefine(im, et):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray) / 255
    r = 60
    eps = 0.0001
    t = Guidedfilter(gray, et, r, eps)

    return t


def Imgrefinedbydark(X):
    I_t, tr_t = np.zeros(X.shape), np.zeros((len(X), im_width, im_height))
    for i in range(len(X)):
        I_t[i] = X[i]
        dark_t = DarkChannel(I_t[i], 15)
        A_t = AtmLight(I_t[i], dark_t)
        te_t = TransmissionEstimate(I_t[i], A_t, 15)
        tr_t[i] = TransmissionRefine(X[i] * 255, te_t)

    tr_t = np.repeat(tr_t, 3).reshape(len(X), im_width, im_height, 3)

    return X - 0.75 * tr_t


def Imgrefinedbydarkforhalf(X):
    I_t, tr_t = np.zeros(X.shape), np.zeros((len(X), im_width // 2, im_height // 2))
    for i in range(len(X)):
        I_t[i] = X[i]
        dark_t = DarkChannel(I_t[i], 15)
        A_t = AtmLight(I_t[i], dark_t)
        te_t = TransmissionEstimate(I_t[i], A_t, 15)
        tr_t[i] = TransmissionRefine(X[i] * 255, te_t)

    tr_t = np.repeat(tr_t, 3).reshape(len(X), im_width // 2, im_height // 2, 3)

    return X - 0.75 * tr_t


'''
# X_train changed by dark ch.
I_t,tr_t= np.zeros(X.shape),np.zeros((len(X),im_width,im_height))
I_t_h,tr_t_h = np.zeros(X_half.shape),np.zeros((len(X_half),im_width//2,im_height//2))

for i in range(len(X)):
    I_t[i] = X[i]
    dark_t = DarkChannel(I_t[i], 15)
    A_t = AtmLight(I_t[i], dark_t)
    te_t = TransmissionEstimate(I_t[i], A_t, 15)
    tr_t[i] = TransmissionRefine(X[i], te_t)

for i in range(len(X_half)):
    I_t_h[i] = X_half[i]
    dark_t_h = DarkChannel(I_t_h[i], 15)
    A_t_h = AtmLight(I_t_h[i], dark_t_h)
    te_t_h = TransmissionEstimate(I_t_h[i], A_t_h, 15)
    tr_t_h[i] = TransmissionRefine(X_half[i], te_t_h)

#Train , Val Split
tr_t = np.repeat(tr_t,3).reshape(len(X),im_width,im_height,3)
tr_t_h = np.repeat(tr_t_h,3).reshape(len(X_half),im_width//2,im_height//2,3)

X_refined = Imgrefinedbydark(X)
X_half_refined = Imgrefinedbydrakforhalf(X_half)
X_train, X_valid, y_train, y_valid = train_test_split(X_refined, y, test_size=0.2, random_state=2020)
X_train_half, X_valid_half, y_train_half, y_valid_half = train_test_split(X_half_refined, y_half, test_size=0.2, random_state=2020)
print(X_train.shape, X_valid.shape)
print(X_train_half.shape, X_valid_half.shape)

#Check if the features and the target match 
sel = random.randint(0, len(X_train)-1)
plt.subplot(2,2,1)
plt.imshow(X_train[sel])
plt.subplot(2,2,2)
plt.imshow(y_train[sel])

plt.subplot(2,2,3)
plt.imshow(X_train_half[sel])
plt.subplot(2,2,4)
plt.imshow(y_train_half[sel
plt.show()
'''

#derain.load_weights('DERAIN_400x400_25epochs.h5')
derain.load_weights('DERAIN_400x400_25epochs.h5')
dehaze.load_weights('Dehaze_Multi_scale_320x320_mse_ssim_mae_35epochs.h5')
desnow.load_weights('Desnow_multiscale_400x400_mse_ssim_mae_30epochs.h5')

data_path = 'C:/Users/hp/Desktop/Jai/졸작/imgs'

test_generator = test_datagen.flow_from_directory(
    data_path,
    target_size=(CF_height, CF_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle = False)

# Saved Model 부르기
new_model = combinedModel
new_model.load_weights('Mobilenet_edge_hsv_combined_160x160_25epochs.h5')

testgenerator = test_generator_multiple(test_generator)
STEP_SIZE_TEST=test_generator.n//batch_size + 1
total_test = test_generator.n

#model predict
class_names = ['HAZE', 'RAINY', 'SNOWY', 'SUNNY']
predictions = new_model.predict(testgenerator,steps = STEP_SIZE_TEST, verbose=1)

print('Number of test gen',test_generator.n)
print('prediction shape',predictions.shape)

count = 0
test_images = np.zeros((total_test,CF_height,CF_width,3))
test_labels = np.zeros((total_test,4))
for batch, CLS in test_generator:
    for j in range(len(batch)):
        img = batch[j]
        test_images[count]=img
        cls_temp = CLS[j]
        test_labels[count]=cls_temp
        count += 1
        if count == (total_test):
            break
    if count == (total_test):
        break

test_label_cls=np.argmax(test_labels,axis=1)
prediction_label=np.argmax(predictions,axis=1)
print('prediction: ', prediction_label,prediction_label.shape)
#print(test_label_cls,test_label_cls.shape)

'''
#model evaluate
test_loss, test_acc = new_model.evaluate(testgenerator,steps=STEP_SIZE_TEST, verbose=2)
print(test_acc)

acc_each=np.zeros(4)
for i in range(test_generator.n):
  if prediction_label[i] == test_label_cls[i]:
    if prediction_label[i] == 0:
      acc_each[0] +=1
    elif prediction_label[i] == 1:
      acc_each[1] +=1
    elif prediction_label[i] == 2:
      acc_each[2] +=1
    elif prediction_label[i] == 3:
      acc_each[3] +=1

print(acc_each/100)

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label_onehot, img = predictions_array[i], true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  true_label = np.argmax(true_label_onehot)

  plt.imshow(img)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),  
                                class_names[true_label]),
                                color=color,fontsize=5)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label_onehot = predictions_array[i], true_label[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])
  true_label = np.argmax(true_label_onehot)
  thisplot = plt.bar(range(4), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

num_rows = 8
num_cols = 5
num_images = num_rows*num_cols
plt.tight_layout
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions, test_labels, test_images)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions, test_labels)
plt.show()'''


def sorting(x):
    return int(re.findall("\d+", x)[0])


def get_datafortest(path):
    ids = next(os.walk(path))[2]
    ids = sorted(ids, key=sorting)
    print(ids)

    X = np.zeros((len(ids), im_height, im_width, 3), dtype=np.float32)
    X_half = np.zeros((len(ids), im_height // 2, im_width // 2, 3), dtype=np.float32)

    for n, id_ in tqdm(enumerate(ids), total=len(ids), disable=True):
        # Load images
        img = load_img(path + id_, grayscale=False)
        x_img = img_to_array(img)
        x_img = resize(x_img, (im_height, im_width, 3), mode='constant', preserve_range=True)
        x_img_half = resize(x_img, (im_height // 2, im_width // 2, 3), mode='constant', preserve_range=True)
        X[n] = x_img / 255
        X_half[n] = x_img_half / 255

    return X, X_half


path_dehaze = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/haze/'
path_derain = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/rain/'
path_desnow = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/snow/'
path_sunny = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/sunny/'
paths = [path_dehaze, path_derain, path_desnow, path_sunny]
ind = 0
print(prediction_label)
for batch, cl in test_generator:
    for img1 in batch:
        img = img1*255
        plt.imshow(img/255)
        plt.show()
        im = Image.fromarray(img.astype(np.uint8))
        print(paths[prediction_label[ind]]+str(ind))
        im.save(paths[prediction_label[ind]]+str(ind)+'.jpg')
        ind += 1
    if ind == len(prediction_label):
            break


hazy, hazy_half = get_datafortest(path_dehaze)
rainy, rainy_half = get_datafortest(path_derain)
snowy, snowy_half = get_datafortest(path_desnow)

for cf in prediction_label:
    if cf == 0:
        Hazy = Imgrefinedbydark(hazy)
        Hazy_half = Imgrefinedbydarkforhalf(hazy_half)
        Hazy_pred = dehaze.predict([Hazy, Hazy_half])
    elif cf == 1:
        Rainy_pred = derain.predict([rainy, rainy_half])
    elif cf == 2:
        Snowy_pred = desnow.predict([snowy, snowy_half])

import imageio
from PIL import Image
'''
pred = 255 * Hazy_pred
pred = pred.astype(np.uint8)

pred1 = 255 * hazy
pred1 = pred1.astype(np.uint8)
'''
haze_demo = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/haze/demo/'
rain_demo = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/rain/demo/'
snow_demo = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/snow/demo/'
sunny_demo = 'C:/Users/hp/Desktop/Jai/졸작/TEMP/sunny/demo/'

count = 0
for i1 in Hazy_pred:
    plt.rcParams["axes.grid"] = False
    plt.title('Hazy')
    plt.imshow(i1)
    plt.show()
    i1 = i1 * 255
    im = Image.fromarray(i1.astype(np.uint8))
    im.save(haze_demo+str(count)+'.jpg')
    count += 1

for i2 in Rainy_pred:
    plt.rcParams["axes.grid"] = False
    plt.title('Rain')
    plt.imshow(i2)
    plt.show()
    i2 = i2 * 255
    im = Image.fromarray(i2.astype(np.uint8))
    im.save(rain_demo+str(count)+'.jpg')
    count += 1

for i3 in Snowy_pred:
    plt.rcParams["axes.grid"] = False
    plt.title('Snowy')
    plt.imshow(i3)
    plt.show()
    i3 = i3 * 255
    im = Image.fromarray(i3.astype(np.uint8))
    im.save(snow_demo+str(count)+'.jpg')
    count += 1

#imageio.mimwrite('dehaze_demo2.mp4', H , fps = 30)
#imageio.mimwrite('dehaze_demo5.mp4', pred1, fps = 30)

#imageio.mimwrite('desnow_demo.mp4', Snowy_pred , fps = 30)
#imageio.mimwrite('desnow_original.mp4', snowy , fps = 30)

#print(Hazy.dtype)
#imageio.mimwrite('derain_demo5.mp4', Rainy_pred , fps = 30)
#imageio.mimwrite('dehaze_original4.mp4', rainy , fps = 30)


from PIL import ImageTk
import os
from tkinter import *
import PIL.Image

demos = [haze_demo, rain_demo, snow_demo, sunny_demo]
restore = [path_dehaze, path_derain, path_desnow, path_sunny]

root = Tk()
prompt = StringVar()
root.title("Demo")
label = Label(root, fg="dark green")
label.pack()

frame = Frame(root, background='red')
frame.pack()

# Function definition

# first create the canvas
canvas = Canvas(height=200, width=200)
canvas_demo = Canvas(height=200, width=200)
canvas.pack()
canvas_demo.pack()

default_img = ImageTk.PhotoImage(PIL.Image.open('ex.jpg'))
canvas.create_image(0, 0, anchor='nw', image=default_img)


def PrevImg():
    # Demo prev
    canvas.delete("all")
    image1_d = ImageTk.PhotoImage(PIL.Image.open(fp[Cur]))
    canvas.create_image(0, 0, anchor='nw', image=image1_d)
    canvas.image = image1_d

    # Restore prev
    canvas_demo.delete("all")
    image1_r = ImageTk.PhotoImage(PIL.Image.open(fp[Cur + 1]))
    canvas_demo.create_image(0, 0, anchor='nw', image=image1_r)
    canvas_demo.image = image1_r


def NextImg():
    # Demo next
    canvas.delete("all")
    image2_d = ImageTk.PhotoImage(PIL.Image.open(fp[Cur]))
    canvas.create_image(0, 0, anchor='nw', image=image2_d)
    canvas.image = image2_d
    canvas.itemconfig(image_id, image=image2_d)

    # Restored next
    canvas_demo.delete("all")
    image2_r = ImageTk.PhotoImage(PIL.Image.open(fp[Cur + 1]))
    canvas_demo.create_image(0, 0, anchor='nw', image=image2_r)
    canvas_demo.image = image2_r


def BtnNext():
    global Cur
    if Cur < len(fp) - 2:
        Cur = Cur + 2
        NextImg()


def BtnPrev():
    global Cur
    if Cur > 1:
        Cur = Cur - 2
        PrevImg()

    # Invoking through button


TextWindow = Label(frame, anchor=NW, justify=LEFT, bg='white', fg='blue', textvariable=prompt, width=75, height=20)
TextWindow.pack(side=TOP)

Prev = Button(frame, text='Prev', width=25, fg="green", command=BtnPrev)
Prev.pack(side=LEFT)
Next = Button(frame, text='For', width=25, fg="red", command=BtnNext)
Next.pack(side=RIGHT)

Cur = 0

# Create Text File
fp = []
for l in range(len(demos)):
    demoID = next(os.walk(demos[l]))[2]
    restoreID = next(os.walk(restore[l]))[2]
    for i in range(0, len(demoID)):
        fp.append(demos[l] + demoID[i])
        fp.append(restore[l] + restoreID[i])

root.mainloop()




