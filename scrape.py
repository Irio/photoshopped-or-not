import ConfigParser
import flickrapi
import numpy as np
import pandas as pd
import os.path

def flickr_api(settings_path):
    settings = ConfigParser.RawConfigParser()
    settings.read(settings_path)
    api_key = settings.get('Flickr', 'APIKey')
    secret = settings.get('Flickr', 'Secret')
    return flickrapi.FlickrAPI(api_key, secret)

def load_dataset(file_path, file_headers):
    if os.path.isfile(file_path):
        return pd.read_csv(file_path, dtype=np.str)
    else:
        return pd.DataFrame(columns=file_headers)

file_path = 'images.csv'
file_headers = ['photo_id', 'url']
keywords = 'manipulate,manipulation,manipulated,doctored,faked,photoshop,edited,modified,modification,doctored,retouched,enhanced'
flickr = flickr_api('config.ini')
dataset = load_dataset(file_path, file_headers)

for photo in flickr.walk(tag_mode='any', tags=keywords, per_page=10):
    photo_id = photo.get('id')
    if (dataset['photo_id'] == photo_id).any:
        next

    available_sizes = flickr.photos.getSizes(photo_id=photo_id)[0]
    url = available_sizes[len(available_sizes) - 1].get('source')
    row = pd.Series([photo_id, url], index=file_headers)
    dataset = dataset.append(row, ignore_index=True)
    dataset.to_csv(file_path, encoding='utf-8', index=False)
