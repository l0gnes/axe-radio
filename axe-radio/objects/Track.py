from humanize import naturaldelta

__all__ = [
    "Track"
]

class Track(object):

    title : str
    artist : str
    album : str     
    duration : int          # Length of song in seconds
    guid : str              # A special identifier for the song

    cover_art_url : str     # Cover art for the album

    def __init__(
        self,
        title : str,
        artist : str,
        album : str,
        duration : int,
        guid : str,
        cover_art_url : str) -> None:

        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.guid = guid
        self.cover_art_url = cover_art_url

    def __str__(self) -> str:
        return f"{self.artist} - {self.title}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.title=} {self.artist=} {self.duration=}>"
    