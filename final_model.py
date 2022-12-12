# Train final model
# Imports 
import numpy as np
import pandas as pd
import os

import tensorflow as tf
from tensorflow import keras

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# EfficientNetB4
from tensorflow.keras.applications.efficientnet import EfficientNetB4
from tensorflow.keras.applications.efficientnet import preprocess_input as preprocess_input_efficient

train = pd.read_csv('train.csv')
train['image'] = train['Id'].map(lambda x: f'{x:0>4}.jpg')

train_df=train.groupby('label', group_keys=False).apply(lambda x: x.sample(frac=0.85, random_state=1996))
print(train_df.shape)
val_df = pd.concat([train_df,train]).drop_duplicates(keep=False)
print(val_df.shape)

path = os.getcwd()

train_gen = ImageDataGenerator(preprocessing_function=preprocess_input_efficient)
train_ds=train_gen.flow_from_dataframe(dataframe=train_df, directory=f'{path}/{"images"}', 
                                            x_col="image", y_col="label", class_mode="categorical", 
                                            target_size=(380,380), batch_size=32,seed=42)

val_gen = ImageDataGenerator(preprocessing_function=preprocess_input_efficient)
val_ds=val_gen.flow_from_dataframe(dataframe=val_df, directory=f'{path}/{"images"}', 
                                            x_col="image", y_col="label", class_mode="categorical", 
                                            target_size=(380,380), batch_size=32,seed=42)

def make_final_model(learning_rate=0.01, size_inner=300, size_inner_2=300, droprate=0.3, droprate_2=0.3):
    base_model = EfficientNetB4(
        weights='imagenet',
        include_top=False,
        input_shape=(380, 380, 3)
    )

    base_model.trainable = False

    #########################################

    inputs = keras.Input(shape=(380, 380, 3))
    base = base_model(inputs, training=False)
    vectors = keras.layers.GlobalAveragePooling2D()(base)
    
    inner = keras.layers.Dense(size_inner, activation='relu')(vectors)
    drop = keras.layers.Dropout(droprate)(inner)
    
    inner_2 = keras.layers.Dense(size_inner_2, activation='relu')(drop)
    drop_2 = keras.layers.Dropout(droprate_2)(inner_2)
    
    outputs = keras.layers.Dense(6)(drop_2)
    
    model = keras.Model(inputs, outputs)
    
    #########################################

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    loss = keras.losses.CategoricalCrossentropy(from_logits=True)

    model.compile(
        optimizer=optimizer,
        loss=loss,
        metrics=['accuracy']
    )
    
    
    return model

checkpoint = keras.callbacks.ModelCheckpoint(
    'EfficientNetB4{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only=False,
    monitor='val_accuracy',
    mode='max'
)

model = make_final_model()

history = model.fit(train_ds, epochs=50, validation_data=val_ds,
                   callbacks=[checkpoint])
