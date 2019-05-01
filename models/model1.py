# download trained model here:
# https://people.cs.uct.ac.za/~mshstu001/model1_epoch_49.h5


import os
import datetime
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras.callbacks import TensorBoard

# filthy fix for file reading errors
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

IMAGE_SIZE = 150
BATCH_SIZE = 16

# make new empty log directory for tensorboard
LOG_DIR = 'data/summaries/model1_' + datetime.datetime.now().strftime("%Y-%m-%d-%Hh%M")
if os.path.isdir(LOG_DIR):
    os.rmdir(LOG_DIR)
os.makedirs(LOG_DIR)


strawberry_gen = ImageDataGenerator(
    validation_split=0.2,
)
train_datagen = strawberry_gen.flow_from_directory(
    'data',
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    classes=['strawberry', 'not-strawberry'],
    class_mode='binary',
    subset='training'
)
val_datagen = strawberry_gen.flow_from_directory(
    'data',
    target_size=(IMAGE_SIZE, IMAGE_SIZE),
    batch_size=BATCH_SIZE,
    classes=['strawberry', 'not-strawberry'],
    class_mode='binary',
    subset='validation'
)

print(train_datagen.n)
print(val_datagen.n)

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=keras.optimizers.Adam(lr=0.00003),
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir=LOG_DIR, histogram_freq=0, write_graph=False, write_images=False)

model.fit_generator(
    train_datagen,
    steps_per_epoch=2000//BATCH_SIZE,
    epochs=50,
    validation_data=val_datagen,
    validation_steps=800//BATCH_SIZE,
    callbacks=[tensorboard]
)

model.save('data/model1_epoch_49.h5', include_optimizer=False)
