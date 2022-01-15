import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import nibabel as nib
from scipy import ndimage
from preprocess import ProcessScan
import argparse


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument('-i', '--input', required=True, help='nifti file path')
    ap.add_argument('-m', '--model', required=True, help='Model path')
    args = vars(ap.parse_args())

model = tf.keras.models.load_model(args['model'])
process_mod = ProcessScan()
scan = process_mod.process_scan(args['input'])

# Making the Prediction
prediction = model.predict(np.expand_dims(scan, axis=0))[0]
scores = [1 - prediction[0], prediction[0]]
class_names = ['normal', 'abnormal']
for score, name in zip(scores, class_names):
    print("The model is %.2f percent confident that CT scan is %s"% ((100 * score), name))

