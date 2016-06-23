from hashlib import sha256
from helpers import load_dataset
import numpy as np
import os
import pandas as pd
import requests
import sys
import time
import urllib.request

CSV_PATH = sys.argv[1]
URL_COLUMN = sys.argv[2]
PATH = sys.argv[3]

def download_image(url, file_path):
    try:
        if 'imgur.com' in url:
            final_url = requests.get(url).url
            if ('//'.join(final_url.split('//')[1:])) == 'i.imgur.com/removed.png':
                raise IOError('HTTP Error 404: Not Found')
        urllib.request.urlretrieve(url, file_path)
        print('+ %s' % url)
    except IOError as e:
        print('%s - %s' % (url, e), file=sys.stderr)

def url_to_file_name(url):
    if url:
        file_name = sha256(url.encode('utf-8')).hexdigest()
        extension = url.split('.')[-1]
        if len(extension) > 4:
            return file_name
        else:
            return '%s.%s' % (file_name, extension)

if not os.path.exists(PATH):
    os.mkdir(PATH)

dataset = load_dataset(CSV_PATH)
dataset[URL_COLUMN] = dataset[URL_COLUMN].astype(np.str).replace({'nan': None})
dataset['file_names'] = dataset[URL_COLUMN].map(url_to_file_name)
already_downloaded = dataset['file_names'].isin(os.listdir(PATH))
without_url = dataset[URL_COLUMN].isnull()
remaining_images = dataset[~(already_downloaded | without_url)]

print('Remaining: %i' % len(remaining_images))
for index, values in remaining_images.iterrows():
    url = dict(values)[URL_COLUMN]
    file_path = '%s/%s' % (PATH, url_to_file_name(url))
    time.sleep(1)
    download_image(url, file_path)
