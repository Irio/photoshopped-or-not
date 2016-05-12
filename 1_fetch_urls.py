import flickrapi
from helpers import flickr_api, load_dataset
import pandas as pd
import sys

ids_dataset_path = 'datasetFlickrID.txt'
urls_dataset_path = 'psed_images.csv'
file_headers = ['photo_id', 'url']
flickr = flickr_api('config.ini')
ids_dataset = load_dataset(ids_dataset_path, ['photo_id'])
urls_dataset = load_dataset(urls_dataset_path, file_headers)
remaining_images = ids_dataset[~ids_dataset['photo_id'].isin(urls_dataset['photo_id'])]

for index, photo in remaining_images.iterrows():
    url = None
    photo_id = str(photo['photo_id'])
    try:
        available_sizes = flickr.photos.getSizes(photo_id=photo_id)
        url = available_sizes['sizes']['size'][-1]['source']
        print('+ %s' % photo_id)
    except flickrapi.exceptions.FlickrError as e:
        print('%s - %s' % (photo_id, e), file=sys.stderr)

    row = pd.Series([photo_id, url], index=file_headers)
    urls_dataset = urls_dataset.append(row, ignore_index=True)
    urls_dataset.to_csv(urls_dataset_path, encoding='utf-8', index=False)
