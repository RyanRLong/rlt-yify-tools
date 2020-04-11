# -*- coding: utf-8 -*-
"""
.. module:: feed
   :platform: Unix
   :synopsis: Yify feed model

.. moduleauthor:: Ryan Long <rlong@redlineperf.com>

"""
from feedparser import FeedParserDict
from models.entry import Entry


class Feed:
    """Represents an RSS Yify Feed"""

    def __init__(self, data: FeedParserDict):
        """Initializes Feed instance from data

        Args:
            data (FeedParserDict): feed
        """
        self.data = data

    def __len__(self):
        """Gets the number of film entries from the feed

        Returns:
            number of entries as int

        """
        return len(self.get_entries())

    def get_info(self):
        """Dictionary of feed info

        Returns:
            dict of feed info

        """
        return self.data["feed"]

    def get_entries(self):
        """Gets film entries as list comprehension

        Returns:
            list comprehension of film entries

        """
        return [Entry(item) for item in self.data["entries"]]

    def is_ok(self):
        """True on feed retrieval succeess, False otherwise

        Returns:
            bool

        """
        return self.data["status"] == 200


if __name__ == "__main__":
    pass
