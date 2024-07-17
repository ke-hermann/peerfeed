from linkpreview import link_preview

from custom_types import FeedEntry, ListItem



def generate_list_item(url: str) -> ListItem:
    preview = link_preview(url)
    return ListItem(preview.title, preview.description, preview.image)


def generate_feed_entry(url: str) -> FeedEntry:
    preview = link_preview(url)
    entry = FeedEntry(preview.title, preview.description, preview.image, url)
    return entry
