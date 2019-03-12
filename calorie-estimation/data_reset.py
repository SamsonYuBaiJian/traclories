import os
import shutil

data_directory = "./dataset"

shutil.rmtree(data_directory, ignore_errors=True)
os.mkdir(data_directory)
os.mkdir(data_directory + "/images")