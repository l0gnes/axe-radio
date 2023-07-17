import aiohttp
import os
import os.path
from json import load
from typing import List

from objects import Track, UpcomingTrack
import utils

__all__ = [
    "AxeRadioAPIWrapper"
]

class AxeRadioAPIWrapper(object):

    SETTINGS_CACHE : dict

    def load_settings(self, fp : os.PathLike) -> None:
        
        # Open the settings file and push it into the cache
        with open(fp, 'r') as sf:
            self.SETTINGS_CACHE = load(sf)
        

    def locate_settings(self) -> None:

        # Get the dir name for this file (which should be in the same directory as the settings file)
        dir_ = os.path.dirname(__file__)

        # Construct the expected path
        expected_path = os.path.join(dir_, 'settings.json')

        # Ensure the path exists
        if not os.path.exists(expected_path):
            raise FileNotFoundError("Failed to locate the settings.json file")
        
        # Return the file to load if it exists
        return expected_path

    def __init__(self) -> None:

        settings_path = self.locate_settings()
        self.load_settings(settings_path)

        print(self.SETTINGS_CACHE)

    async def fetch_now_playing(self) -> Track:

        # fetch the json response from the api endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.SETTINGS_CACHE.get("now_playing_url")
            ) as resp:
                r = await resp.json()

        # Return one of those cool track objects
        return Track(
            title           = r['title'],
            artist          = r['artist'],
            album           = r['album'],
            duration        = int(r['duration']),
            guid            = r['guid'],
            cover_art_url   = "http://radiojar-lib.appspot.com/get_media_image?size=orig&guid=%s" % (r['guid'],)
        )
    
    async def fetch_upcoming_tracks(self) -> List[UpcomingTrack]:
        
        # fetch the json response from the api endpoint
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.SETTINGS_CACHE.get("upcoming_tracks")
            ) as resp:
                r = await resp.json()

        return [
            UpcomingTrack(
                title           = r['track'],
                artist          = r['artist'],
                album           = r['album'],
                duration        = int(r['duration']),
                guid            = r['guid'],
                cover_art_url   = "http://radiojar-lib.appspot.com/get_media_image?size=orig&guid=%s" % (r['guid'],),
                start_time      = utils.i_hate_radiojar(r['tm']),
                end_time        = utils.i_hate_radiojar(r['tm_end'])
            )
        ]