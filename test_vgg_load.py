from keras.models import model_from_json
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

vgg16_json = 'cov_cnn_web/predictor/model_weights/VGG16/VGG16_Model.json'
with open(vgg16_json, 'r') as vggjson:
    vgg16model = model_from_json(vggjson.read())
print("VGG16 model loaded successfully")
