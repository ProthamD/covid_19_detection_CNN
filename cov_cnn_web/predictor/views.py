import os
import cv2
import time
import numpy as np
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from keras.models import load_model

# Create your views here.

covid_pred = ['Covid-19', 'Non Covid-19']
IMAGE_SIZE = 64

MODEL_PATHS = {
    'vgg16':    'predictor/model_weights/VGG16/VGG16_Model.hdf5',
    'resnet':   'predictor/model_weights/ResNet50/ResNet50_Model.hdf5',
    'xception': 'predictor/model_weights/Xception/Xception_Model.hdf5',
}

# Load all models once at startup to avoid reloading on every request
print("Loading models into memory (this happens only once)...")
_t = time.time()
MODELS = {
    'vgg16':    load_model(MODEL_PATHS['vgg16'],    compile=False),
    'resnet':   load_model(MODEL_PATHS['resnet'],   compile=False),
    'xception': load_model(MODEL_PATHS['xception'], compile=False),
}
print(f"All models loaded in {time.time() - _t:.1f}s")


def predict_with_cached_model(model_key, pred_arr):
    """Predict using an already-loaded cached model."""
    model = MODELS[model_key]
    label = model.predict(pred_arr, verbose=0)
    idx = int(np.argmax(label[0]))
    score = float(np.amax(label[0]))
    return idx, score


def read_image(filepath):
    return cv2.imread(filepath)


def resize_image(img, image_size):
    return cv2.resize(img.copy(), image_size, interpolation=cv2.INTER_AREA)


def clear_mediadir():
    media_dir = "./media"
    for f in os.listdir(media_dir):
        os.remove(os.path.join(media_dir, f))


def index(request):
    if request.method == "POST":
        clear_mediadir()

        img = request.FILES['ImgFile']
        fs = FileSystemStorage()
        filename = fs.save(img.name, img)
        img_path = fs.path(filename)

        pred_arr = np.zeros((1, IMAGE_SIZE, IMAGE_SIZE, 3))
        im = read_image(img_path)
        if im is not None:
            pred_arr[0] = resize_image(im, (IMAGE_SIZE, IMAGE_SIZE))
        pred_arr = pred_arr / 255

        print("Running VGG16...")
        t0 = time.time()
        idx_vgg, cf_score_vgg = predict_with_cached_model('vgg16', pred_arr)
        vgg_exec = time.time() - t0
        print(f"VGG16 done: {covid_pred[idx_vgg]} ({cf_score_vgg:.2f}) in {vgg_exec:.1f}s")

        print("Running ResNet50...")
        t0 = time.time()
        idx_resnet, cf_score_resnet = predict_with_cached_model('resnet', pred_arr)
        resnet_exec = time.time() - t0
        print(f"ResNet50 done: {covid_pred[idx_resnet]} ({cf_score_resnet:.2f}) in {resnet_exec:.1f}s")

        print("Running Xception...")
        t0 = time.time()
        idx_xception, cf_score_xception = predict_with_cached_model('xception', pred_arr)
        xception_exec = time.time() - t0
        print(f"Xception done: {covid_pred[idx_xception]} ({cf_score_xception:.2f}) in {xception_exec:.1f}s")

        response = {
            'table': 'table',
            'col0': ' ', 'col1': 'VGG16', 'col2': 'ResNet50', 'col3': 'Xception',
            'row1': 'Results', 'row2': 'Confidence Score', 'row3': 'Prediction Time (s)',
            'v_pred': covid_pred[idx_vgg],
            'r_pred': covid_pred[idx_resnet],
            'x_pred': covid_pred[idx_xception],
            'v_cf': cf_score_vgg,
            'r_cf': cf_score_resnet,
            'x_cf': cf_score_xception,
            'v_time': vgg_exec,
            'r_time': resnet_exec,
            'x_time': xception_exec,
            'image': '../media/' + img.name,
        }
        return render(request, 'index.html', response)
    else:
        return render(request, 'index.html')
