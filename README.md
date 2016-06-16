# Photoshopped or not?

Project made during http://datascienceretreat.com/.

## Setup

You will need:

* Flickr API credentials (today freely available at https://www.flickr.com/services/apps/create/apply/)

```
$ ./setup
```

## Running

```
$ python 1_fetch_urls.py
$ python fetch_urls_reddit.py battleshops_reddit_posts.2015_12.csv reddit_psed.csv
$ python fetch_urls_reddit.py battleshops_reddit_posts.2016_01.csv reddit_psed.csv
$ python fetch_urls_reddit.py battleshops_reddit_posts.2016_02.csv reddit_psed.csv
$ python fetch_urls_reddit.py battleshops_reddit_posts.full_corpus_201512.csv reddit_psed.csv
$ python 2_save_images.py psed_images.csv url psed
$ python 2_save_images.py RAISE_1k.csv TIFF non-psed
$ python 2_save_images.py reddit_psed_images.csv url psed-reddit
```

Source of reddit dataset: https://www.reddit.com/r/photoshopbattles
