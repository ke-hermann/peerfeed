from dataclasses import dataclass


@dataclass
class FeedEntry:
    title: str 
    description: str 
    thumbnail: str
    url: str