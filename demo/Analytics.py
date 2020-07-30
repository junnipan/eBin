from PIL import Image
import tensorflow as tf
import numpy as np
import cv2

# will use this to convert prediction num to string value
CATEGORIES = ["Cardboard", "Glass", "Metal", "Paper", "Plastic", "Trash"]
IMG_SIZE = 299


# def prepare(filepath):
#     img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
#     new_array = cv2.resize(img, (IMG_SIZE / 255, IMG_SIZE / 255))  # resize image to match model's expected sizing
#     return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)  # return the image with shaping that TF wants.
#
#
model = tf.keras.models.load_model("model/my_model.h5")
#
# prediction = model.predict([prepare("data/images.jpeg")])
# print(prediction)  # will be a list in a list.
# print(CATEGORIES[int(prediction[0][0])])


def load(file):
    test_image = Image.open(file)
    test_image = np.array(test_image).astype('float32') / 255
    test_image = cv2.resize(test_image, (IMG_SIZE, IMG_SIZE), 3)
    test_image = np.expand_dims(test_image, axis=0)
    return test_image


def analyze(file):
    image = load(file)
    prediction = model.predict(image)
    i = np.argmax(prediction)
    category = CATEGORIES[i]
    print(prediction)
    print(category)
    # print(CATEGORIES[int(prediction[0][0])])

