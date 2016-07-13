# Detecting Photoshopped images with Machine Learning

If every picture tells a story, a doctored image has the goal of making people misjudge the original story. People may remove, add or change elements in pictures, but unveiling the true behind each photo has been a challenge for decades. Leveraging Machine Learning techniques and domain knowledge acquired specifically for this project I was able to achieve about 93% of accuracy on detecting when a digital photo was doctored or not.

Running an algorithm of Error Level Analysis, or ELA, on different datasets of thousands of images, I get an image, with the same dimensions of the original, but with measurements of the compression level of pixel grid. When a picture is taken directly from a camera to a hard disk, the file has no or just a minimum compression, uniform throughout the pixels. Resaving it with the intension of reducing the file size (using algorithms like JPEG) will leave traces, allowing a forensics specialist detect what the compression level was. Resaving it with some kind of editing, like filters, brushing or use of the stamp tool will leave a specific type of trace in the region affected, something detectable by mathematical models as ELA.

Leveraging an open source implementation of the Error Level Analysis algorithm, my analysis was created in Python and is publicly available on GitHub (Irio/photoshopped-or-not). Having tried different methods from Linear Regression to Convolutional Neural Networks, combining or not multiple models, scikit-learn’s Random Forest gave me the best results with lower complexity. Is able to find patterns in datasets of images photoshopped or not, scraped from reddit or collected from research groups studying different aspects of digitally altered images.

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
