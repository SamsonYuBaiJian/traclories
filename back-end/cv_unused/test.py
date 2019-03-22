from keras.preprocessing import image
from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
import numpy as np
from annoy import AnnoyIndex
import os

class CVModel:
    def __init__(self, img_data, name_list, calorie_data):
        self.model      = VGG16(weights='imagenet', include_top=False)
        self.calorie_data = calorie_data
        self.img_data    = img_data
        self.vector_dim = 1 * 7 * 7 * 512
        self.name_list = name_list
        self.t = AnnoyIndex(self.vector_dim)    # Length of item vector that will be indexed
        self.model_file_name = "./cv.ann"
        self.num_neighbours = 5

    def train(self):
        for img_index in range(len(self.img_data)):
            try:
                img = image.load_img(self.img_data[img_index], target_size=(224, 224))
                img_data = image.img_to_array(img)
                img_data = np.expand_dims(img_data, axis=0)
                img_data = preprocess_input(img_data)
                vgg16_feature = self.model.predict(img_data)
                flat = np.ndarray.flatten(vgg16_feature)
                self.t.add_item(img_index, flat)
                if (img_index + 1) % 100 == 0:
                    print("Vectors done: " + str(img_index + 1) + "/" + len(self.img_data))
            except:
                continue

        self.t.build(10)    # 10 trees

    def save(self):
        self.t.save(self.model_file_name)
        print("\nCV model saved at " + self.model_file_name + ".\n")

    def load(self):
        self.t.load(self.model_file_name)    # super fast, will just map the file

    def predict_internal(self, input_index):
        nn_indexes = self.t.get_nns_by_item(input_index, self.num_neighbours, include_distances=True)[0] # will find the 10 nearest neighbors
        result = []

        print("\nCV prediction:\n")

        for nn_index in nn_indexes:
            print(self.name_list[nn_index])
            result.append(self.calorie_data[nn_index])

        return result

    def predict_external(self, img_dir):
        img = image.load_img(img_dir, target_size=(224, 224))
        img_data = image.img_to_array(img)
        img_data = np.expand_dims(img_data, axis=0)
        img_data = preprocess_input(img_data)
        vgg16_feature = self.model.predict(img_data)
        flat = np.ndarray.flatten(vgg16_feature)
        self.t.add_item(len(self.img_data), flat)
        self.t.build(10)

        nn_indexes = self.t.get_nns_by_item(len(self.img_data), self.num_neighbours+1, include_distances=True)[
            0]  # will find the 10 nearest neighbors
        result = []
        for nn_index in nn_indexes:
            if nn_index != len(self.img_data):
                print(self.name_list[nn_index])
                print(self.calorie_data[nn_index])
                result.append(self.calorie_data[nn_index])

        return result