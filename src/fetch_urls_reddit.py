import flickrapi
from functools import reduce
import numpy as np
import pandas as pd
import re
import requests
import sys
from helpers import flickr_api, load_dataset

CSV_PATH = sys.argv[1]
OUTPUT_CSV_PATH = sys.argv[2]

def imgur_url(url):
    match = re.search(r'https?:\/\/(?:[\w-]+\.)?imgur.com\/(?:a\/)?(?P<id>\w+)', url)
    if match:
        return 'https://i.imgur.com/%s.jpg' % match.groups('id')[0]

def gfycat_url(url):
    match = re.search(r'https?:\/\/(?:[\w-]+\.)?gfycat\.com\/(?P<id>\w+)', url)
    if match:
        return 'https://thumbs.gfycat.com/%s-size_restricted.gif' % match.groups('id')[0]

def flickr_url(url):
    match = re.search(r'https?:\/\/(?:[\w-]+\.)?flickr\.com\/photos\/\w+@?\w+\/(?P<id>\d+)', url)
    if match:
        try:
            available_sizes = flickr.photos.getSizes(photo_id=match.groups('id')[0])
            return available_sizes['sizes']['size'][-1]['source']
        except flickrapi.exceptions.FlickrError as e:
            return None

def is_direct_link(url):
    extensions = ['.gif', '.jpg', '.png']
    regexp = '|'.join([r'(?:\%s\?[\w=&;]+)' % ext for ext in extensions])
    return url[-4:].lower() in extensions or \
        re.search(regexp, url, flags=re.IGNORECASE)

def extract_image_url(url):
    if is_direct_link(url):
        return url
    else:
        return imgur_url(url) or \
            gfycat_url(url) or \
            flickr_url(url)

flickr = flickr_api('config.ini')
reddit_dataset = load_dataset(CSV_PATH)
reddit_dataset = reddit_dataset[~reddit_dataset['is_self']]
reddit_dataset['image_url'] = reddit_dataset['url'].map(extract_image_url)

skipped_rows = reddit_dataset[reddit_dataset['image_url'].isnull()]['url']
print('--- Skipping %i rows' % len(skipped_rows))
if len(skipped_rows):
    print(skipped_rows)

urls_dataset_path = 'reddit_psed_images.csv'
file_headers = ['csv', 'url']
urls_dataset = load_dataset(urls_dataset_path, file_headers)
new_images = ~(reddit_dataset['image_url'].isin(urls_dataset['url']) | \
    reddit_dataset['image_url'].isnull())
urls_to_include = pd.DataFrame()
urls_to_include[['permalink', 'url']] = reddit_dataset[new_images][['permalink', 'image_url']]
urls_to_include['csv'] = np.repeat(CSV_PATH.split('/')[-1], len(urls_to_include))
urls_dataset = pd.concat([urls_dataset, urls_to_include]).drop_duplicates('url')
urls_dataset.to_csv(urls_dataset_path, encoding='utf-8', index=False)
