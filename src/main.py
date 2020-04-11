from gateways.local_feeds import fetch_feed
from gateways.sqlite3_db import Sqlite3
from models.feed import Feed


def main():
    result = Feed(fetch_feed())

    db = Sqlite3()
    db.create_table()
    db.insert_records([item.get_as_record() for item in result.get_entries()])


if __name__ == "__main__":
    main()
