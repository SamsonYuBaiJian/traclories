from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
import numpy as np
from annoy import AnnoyIndex
import os
import datetime

model = VGG16(weights='imagenet', include_top=False)

img_directory = './dataset/images/'

vector_dict = {}
name_list = []
index = 0
f = 1 * 7 * 7 * 512
t = AnnoyIndex(f)  # Length of item vector that will be indexed

for img_file in os.listdir(img_directory):
    img = image.load_img(img_directory + img_file, target_size=(224, 224))
    img_data = image.img_to_array(img)
    img_data = np.expand_dims(img_data, axis=0)
    img_data = preprocess_input(img_data)
    vgg16_feature = model.predict(img_data)
    flat = np.ndarray.flatten(vgg16_feature)
    t.add_item(index, flat)
    name_list.append(img_file)
    index += 1
    if (index + 1) % 10 == 0:
        print("Vectors done: " + str(index + 1))

t.build(10) # 10 trees
model_file_name = './cv_' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '.ann'
t.save(model_file_name)

u = AnnoyIndex(f)
u.load(model_file_name) # super fast, will just map the file
num_neighbour = 10
nn_indexes = u.get_nns_by_item(0, num_neighbour, include_distances=True)[0] # will find the 10 nearest neighbors

for index in nn_indexes:
    print(name_list[index])