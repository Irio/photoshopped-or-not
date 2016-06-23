import cv2
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from scipy import misc
import imread

IMAGE_SHAPE = (64, 64)
IMAGE_ARRAY_SIZE = IMAGE_SHAPE[0] * IMAGE_SHAPE[1]

def image_files_in_folder(folder):
    all_files = os.listdir(folder)
    return [file for file in all_files if file.endswith('.jpg')]

def read_image(path):
    file = imread(path, as_grey=True)
    file = scipy.misc.imresize(file, IMAGE_SHAPE). \
                      reshape(IMAGE_ARRAY_SIZE)
    return file


PATH = 'MICC-F220'
dataset = pd.read_table('%s/groundtruthDB_220.txt' % PATH,
                        delim_whitespace=True,
                        header=None,
                        index_col=False,
                        names=['filename', 'tempered'])
dataset['tempered'] = dataset['tempered'].astype(np.bool)
dataset['image'] = pd.Series(dtype=np.ndarray)
images = np.empty((len(dataset), 659840), dtype=np.ndarray) # 657920

for index, row in dataset.iterrows():
    if index > 1:
        break
    file_path = '%s/%s' % (PATH, row['filename'])
    read_image(path)
    img = cv2.imread(file_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.SIFT()
    # kp = sift.detect(gray, None)
    # img = cv2.drawKeypoints(gray,
    #                         kp,
    #                         flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    # cv2.imwrite('sift_keypoints2.jpg',img)
    kp, des = sift.detectAndCompute(gray, None)
    images[index] = des.reshape(-1)
