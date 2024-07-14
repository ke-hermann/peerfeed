from pathlib import Path
import peewee as pw


DB_PATH = Path.home() / ".peerfeed.db"

db = pw.SqliteDatabase(DB_PATH)


# Define the model for the table
class Entries(pw.Model):
    title = pw.CharField()
    description = pw.TextField()
    thumbnail = pw.CharField()
    url = pw.CharField()

    class Meta:
        database = db  # This model uses the "example.db" database


def create_database():
    db.connect()
    db.create_tables([Entries])
