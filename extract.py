from linkpreview import link_preview

from PySide6.QtCore import QObject, Property
from custom_types import FeedEntry

class ListItem(QObject):
    def __init__(self, title, description, image_source, parent=None):
        super().__init__(parent)
        self._title = title
        self._description = description
        self._image_source = image_source

    @Property(str)
    def title(self):
        return self._title

    @Property(str)
    def imageSource(self):
        return self._image_source

    @Property(str)
    def description(self):
        return self._description


def generate_list_item(url: str) -> ListItem:
    preview = link_preview(url)
    return ListItem(preview.title, preview.description, preview.image)


def generate_feed_entry(url: str) -> FeedEntry:
    preview = link_preview(url)
    entry = FeedEntry(preview.title, preview.description, preview.image, url)
    return entry
