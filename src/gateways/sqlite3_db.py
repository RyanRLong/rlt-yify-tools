# -*- coding: utf-8 -*-
"""
.. module:: sqlite3_db
   :platform: Unix
   :synopsis: I/O for sqlite3 database

.. moduleauthor:: Ryan Long <ryanlong1004@gmail.com>
"""
import os
import sqlite3


class Sqlite3:
    """Gateway for I/O to sqlite 3 database

    ..todo:: Add context manager so we can close the db
    """

    def __init__(self):
        """Creates connection to sqlite3 database"""
        self.conn = sqlite3.connect(
            os.path.join(
                os.path.dirname(os.path.abspath(__file__)), "../../data/yify.db3"
            )
        )

    def create_table(self):
        """Creates the library table if it does not exist"""
        c = self.conn.cursor()

        c.execute(
            """
            CREATE TABLE IF NOT EXISTS library
            (
                id TEXT NOT NULL,
                title TEXT NOT NULL,
                year INT NOT NULL,
                format TEXT NOT NULL,
                summary TEXT NOT NULL,
                runtime INT NOT NULL,
                rating TEXT NOT NULL,
                link TEXT NOT NULL,
                published TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
                PRIMARY KEY(id)
            )
            """
        )
        self.conn.commit()

    def insert_records(self, records: list):
        """Inserts list of records into the library table"""
        c = self.conn.cursor()
        c.executemany(
            """
        INSERT OR IGNORE INTO library
        (id, title, year, format, summary, runtime, rating, link, published)
        VALUES 
        (?,?,?,?,?,?,?,?,?)""",
            records,
        )
        self.conn.commit()


if __name__ == "__main__":
    pass
