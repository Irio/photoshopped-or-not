import os
import pandas as pd
import urllib.request
import sys

def download_image(url, file_path):
    try:
        urllib.request.urlretrieve(url, file_path)
    except IOError as e:
        print('%s %s' % (e, url), file=sys.stderr)

remaining_downloads = 3500
path = 'photoshopped'
if not os.path.exists(path):
    os.mkdir(path)

dataset = pd.read_csv('psed_images.csv')
photo_ids = [name.split('_')[0] for name in os.listdir(path)]
for index, values in dataset[~dataset['photo_id'].isin(photo_ids)].iterrows():
    url = values[1]
    file_path = '%s/%s' % (path, url.split('/')[-1])
    if remaining_downloads == 0:
        break
    elif os.path.exists(file_path):
        print('Skipping #%s' % values[0])
        continue

    download_image(url, file_path)
    remaining_downloads = remaining_downloads - 1
