# !pip install flickrapi

import flickrapi
import pandas as pd
import os.path

import ConfigParser
settings = ConfigParser.RawConfigParser()
settings.read('config.ini')

file_name = 'images.csv'
file_headers = ['photo_id', 'url']
if os.path.isfile(file_name):
    dataset = pd.read_csv(file_name, header=file_headers)
else:
    dataset = pd.DataFrame(columns=file_headers)
api_key, secret = settings.get('Flickr', 'APIKey'), settings.get('Flickr', 'Secret')
keywords = 'manipulate,manipulation,manipulated,doctored,faked,photoshop,edited,modified,modification,doctored,retouched,enhanced'

flickr = flickrapi.FlickrAPI(api_key, secret)
for photo in flickr.walk(tag_mode='any', tags=keywords, per_page=10):
    photo_id = photo.get('id')
    if (dataset['photo_id'] == photo_id).any:
        next

    available_sizes = flickr.photos.getSizes(photo_id=photo_id)[0]
    url = available_sizes[len(available_sizes) - 1].get('source')
    row = pd.Series([photo_id, url], index=file_headers)
    dataset = dataset.append(row, ignore_index=True)
    dataset.to_csv(file_name, encoding='utf-8', index=False)
