from tensorflow.keras import models

def get_model():
    model = models.load_model("model/cnn/all")
    return model
