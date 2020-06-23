import tensorflow as tf
import numpy as np

class Guesser:
    def __init__(self):
        self._base_model = tf.keras.models.load_model('number_guesser.hp5')

    def predict_num(self, mnist):
        predicts = self._base_model.predict([mnist])

        val = np.argmax(predicts[0])
        print("The number is: ", val)

        return val