# -*- coding: utf-8 -*-
"""
.. module:: entry
   :platform: Unix
   :synopsis: Yify film entry model

.. moduleauthor:: Ryan Long <ryanlong1004@gmail.com>

"""
import re


class Entry:
    """Represents a film entry"""

    def __init__(self, data):
        """

        Args:
            data (dict): entry data
        """
        self._data = data

    @property
    def title(self):
        """Film title"""
        return (
            re.search(r"(^.+?)(\(.*\)\s)(\[.*\]\s)", self._data["title"])
            .group(1)
            .strip()
        )

    @property
    def year(self):
        """Film year"""
        return (
            re.search(r"(^.+?)(\(.*\)\s)(\[.*\]\s)", self._data["title"])
            .group(2)
            .strip()[1:-1]
        )

    @property
    def format(self):
        """Film format (typically 720p or 1080p"""
        return (
            re.search(r"(^.+?)(\(.*\)\s)(\[.*\]\s)", self._data["title"])
            .group(3)
            .strip()[1:-1]
        )

    @property
    def summary(self):
        """Synopsis of the film"""
        return re.search(r"(^.+)(/>)(.*)", self._data["summary"]).group(3).strip()

    @property
    def runtime(self):
        """Runtime in minutes"""
        return (
            re.search(r"(Runtime: )(\d.*?)\s", self._data["summary"]).group(2).strip()
        )

    @property
    def rating(self):
        """IMDB rating as x/x"""
        return (
            re.search(r"(Rating:\s)(.+)(<br\s/>Runtime)", self._data["summary"])
            .group(2)
            .strip()
        )

    @property
    def id(self):
        """Id of the film on Yify, also servers as link"""
        return self._data["id"]

    @property
    def link(self):
        """Links to the film, without specifying the format"""
        return self._data["link"]

    @property
    def published(self):
        """Time the film was added to Yify"""
        return self._data["published"]

    def get_as_record(self):
        """Returns record as tuple to be inserted into sqlite3 database"""
        return tuple(
            [
                self.id,
                self.title,
                self.year,
                self.format,
                self.summary,
                self.runtime,
                self.rating,
                self.link,
                self.published,
            ]
        )


if __name__ == "__main__":
    pass
