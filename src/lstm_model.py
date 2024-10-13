import tensorflow as tf
from tensorflow.keras.models import load_model
import keras

@keras.saving.register_keras_serializable()
def mse_with_positive_pressure(y_true: tf.Tensor, y_pred: tf.Tensor):
    """Función de pérdida MSE con presión positiva."""
    mse = (y_true - y_pred) ** 2
    positive_pressure = 10 * tf.maximum(-y_pred, 0.0)
    return tf.reduce_mean(mse + positive_pressure)

def load_lstm() -> tf.keras.Model:
    """Carga un modelo LSTM entrenado."""
    return load_model('model/model-best.keras', custom_objects={'mse_with_positive_pressure': mse_with_positive_pressure})
