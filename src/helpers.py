import configparser
import flickrapi
import numpy as np
import os.path
import pandas as pd

def flickr_api(settings_path):
    settings = configparser.RawConfigParser()
    settings.read(settings_path)
    api_key = settings.get('Flickr', 'APIKey')
    secret = settings.get('Flickr', 'Secret')
    return flickrapi.FlickrAPI(api_key, secret, format='parsed-json')

def load_dataset(file_path, headers = []):
    if os.path.exists(file_path):
        dtype = dict(list(map(lambda x: (x, np.str), headers)))
        return pd.read_csv(file_path, dtype=dtype)
    else:
        return pd.DataFrame(columns=headers)
