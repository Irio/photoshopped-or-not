import numpy as np
import os
import pandas as pd
import urllib.request
import sys

def download_image(url, file_path):
    try:
        urllib.request.urlretrieve(url, file_path)
        print('+ %s' % url)
    except IOError as e:
        print('%s - %s' % (url, e), file=sys.stderr)

path = 'psed'
if not os.path.exists(path):
    os.mkdir(path)

dataset = pd.read_csv('psed_images.csv', dtype={'photo_id': np.str, 'url': np.str})
photo_ids = [name.split('_')[0] for name in os.listdir(path)]
already_downloaded = dataset['photo_id'].isin(photo_ids)
without_url = dataset['url'].isnull()
remaining_images = dataset[~(already_downloaded | without_url)]

for index, values in remaining_images.iterrows():
    url = values[1]
    file_path = '%s/%s' % (path, url.split('/')[-1].split('?')[0])
    download_image(url, file_path)
