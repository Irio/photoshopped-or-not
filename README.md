# Photoshopped or not?

Project made during http://datascienceretreat.com/.

## Setup

You will need:

* Flickr API credentials (today freely available at https://www.flickr.com/services/apps/create/apply/)

```
$ ./src/setup
```

Install OpenCV also.

## Running

```
$ python src/1_fetch_urls.py
$ python src/fetch_urls_reddit.py data/battleshops_reddit_posts.2015_12.csv data/reddit_psed.csv
$ python src/fetch_urls_reddit.py data/battleshops_reddit_posts.2016_01.csv data/reddit_psed.csv
$ python src/fetch_urls_reddit.py data/battleshops_reddit_posts.2016_02.csv data/reddit_psed.csv
$ python src/fetch_urls_reddit.py data/battleshops_reddit_posts.full_corpus_201512.csv data/reddit_psed.csv
$ python 2_save_images.py data/psed_images.csv url data/psed
$ python 2_save_images.py data/RAISE_1k.csv TIFF data/non-psed
$ python 2_save_images.py data/reddit_psed_images.csv url data/psed-reddit
```

Source of reddit dataset: https://www.reddit.com/r/photoshopbattles
