import image
import model
import window
import PySimpleGUI as sg
import tensorflow as tf
import numpy as np

class_names = ['normal', 'bacteria', 'virus']
cnn = model.get_model()

def load_image(path):
    image = Image.open(path)
    return image

win = window.init_window()

result = win.FindElement('result')

while True:
    event, values = win.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "uploaded_path":
        img = image.load_image(values['uploaded_path'])
        matrix = image.image_to_matrix(img, 32)
        predictions = cnn.predict(tf.expand_dims(matrix, 0))
        score = tf.nn.softmax(predictions[0])
        result.update("This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score)))
win.close()
