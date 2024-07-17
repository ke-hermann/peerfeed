from pathlib import Path
import peewee as pw
from custom_types import FeedEntry
from typing import Iterator

DB_PATH = Path.home() / ".peerfeed.db"

database = pw.SqliteDatabase(DB_PATH)


# Define the model for the table
class Entries(pw.Model):
    title = pw.CharField()
    description = pw.TextField()
    thumbnail = pw.CharField()
    url = pw.CharField()

    class Meta:
        database = database  # This model uses the "example.db" database


def create_database():
    with database:
        database.create_tables([Entries])

# Function to insert a new entry into the database
def insert_new_entry(entry: FeedEntry):
    with database:
        new_entry = Entries.create(
            title= entry.title,
            description= entry.description,
            thumbnail= entry.thumbnail,
            url= entry.url
        )
    return new_entry

def fetch_all_entries() -> Iterator[FeedEntry]:
    for entry in Entries.select():
        yield entry

if __name__ == "__main__":
    create_database()