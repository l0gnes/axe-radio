from datetime import datetime
from . import Track

class UpcomingTrack(Track):

    start_time : datetime
    end_time : datetime

    def __init__(
        self, 
        title: str, 
        artist: str, 
        album: str, 
        duration: int, 
        guid: str, 
        cover_art_url: str,
        start_time : datetime,
        end_time : datetime) -> None:
        
        super().__init__(title, artist, album, duration, guid, cover_art_url)

        self.start_time = start_time
        self.end_time = end_time

    def is_playing_at(self, t : datetime) -> bool:
        """Determines whether or not the current track will be playing at time `t`

        :param t: The time to evaluate at
        :type t: datetime
        :return: `True` if the song is supposed to play at time `t`
        :rtype: bool
        """
        return self.start_time <= t and self.end_time < t

    @property
    def is_playing_now(self) -> bool:
        """Determines whether or not this track should be the one currently playing or not
        this attribute should hopefully mitigate querying the API multiple times for the
        same information

        :return: `True` if the song should be the one currently playing
        :rtype: bool
        """
        return self.is_playing_at(datetime.utcnow())