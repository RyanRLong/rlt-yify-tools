# -*- coding: utf-8 -*-
"""
.. module:: local_feeds
   :platform: Unix
   :synopsis: Fetches, saves and loads YIFY feeds

.. moduleauthor:: Ryan Long <rlong@redlineperf.com>

"""
import datetime
import os
import pickle

import feedparser

URL = "https://yts.ws/rss/0/all/all/0"  # todo add to config file


def save_feed(feed):
    """Saves feeds as a binary file"""
    with open(
        os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "..",
            "..",
            "data",
            f"{_create_file_name_from_date()}",
        ),
        "wb",
    ) as file:
        pickle.dump(feed, file)


def load_feed(file_path):
    """Loads feed as a binary file"""
    with open(file_path, "rb") as file:
        return pickle.load(file)


def fetch_feed() -> feedparser.FeedParserDict:
    """Fetches feed from YIFY RSS"""
    result = feedparser.parse(URL)
    save_feed(result)
    return result


def _create_file_name_from_date():
    """Convenience method for storing feed names with a date format"""
    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S_feed.txt")


if __name__ == "__main__":
    pass
