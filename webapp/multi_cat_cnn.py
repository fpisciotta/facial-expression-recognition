from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.optimizers import SGD, RMSprop
from keras.utils.np_utils import to_categorical
from log import save_model, save_config, save_result
# from fer2013data import load_data
import numpy as np
import sys

# import dataset:
X_fname = './data/X_train.npy'
y_fname = './data/y_train.npy'
X_train = np.load(X_fname)
y_train = np.load(y_fname)
X_test = np.load('data/X_test.npy')
y_test = np.load('data/y_test.npy')
X_train = X_train.astype('float32');
X_test = X_test.astype('float32');
print ('Lengths: ', len(X_train) ,len(y_train))

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
# params:
batch_size = 128
nb_epoch = 50

# setup info:
print ('X_train shape: ', X_train.shape) # (n_sample, 1, 48, 48)
print ('y_train shape: ', y_train.shape) # (n_sample, n_categories)
print ('  img size: ', X_train.shape[2], X_train.shape[3])
print ('batch size: ', batch_size)
print ('  nb_epoch: ', nb_epoch)
print ('Lengths: ', len(X_train) ,len(y_train))
print ('Target: ', y_train)
# model architecture:
model = Sequential()
model.add(Conv2D(48, 3, 3, border_mode='same',activation='relu',input_shape=(1, X_train.shape[2], X_train.shape[3])))
model.add(Conv2D(48, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(48, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))

model.add(Conv2D(96, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(96, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(96, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))

model.add(Conv2D(144, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(144, 3, 3, border_mode='same', activation='relu'))
model.add(Conv2D(144, 3, 3, border_mode='same', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), dim_ordering="th"))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(6, activation='softmax'))

# optimizer:
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print ('Training....')
hist = model.fit(X_train, y_train, nb_epoch=nb_epoch, batch_size=batch_size,
          validation_split=0.3, shuffle=True, verbose=1)

train_val_accuracy = hist.history;
# set callback: https://github.com/sallamander/headline-generation/blob/master/headline_generation/model/model.py

# model result:
loss_and_metrics = model.evaluate(X_test, y_test, batch_size=batch_size, verbose=1)
print ('Done!')
print ('Loss: ', loss_and_metrics[0])
print (' Acc: ', loss_and_metrics[1])

# model logging:
notes = 'medium set 100'
save_model(model, './data/results/')
#save_config(model.get_config(), './data/results/')
#save_result(train_val_accuracy,loss_and_metrics, notes, './data/results/')