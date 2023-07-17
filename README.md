# AxeRadioAPIWrapper - An Asyncronous Python API Wrapper

( This is all possible using the RadioJar api endpoints, so technically this works for any RadioJar station. Feel free to use this with other projects )

> ### ✨ Example:
```py
import AxeRadioAPIWrapper
import asyncio

# Fetch the event loop
eloop = asyncio.get_event_loop()

# Init the client
client = AxeRadioAPIWrapper()

# Fetch the current playing song
r = eloop.run_until_complete(client.fetch_now_playing())

# Prints the song in an "Artist - Title" style
print(r)
```

📓 Method Reference
---
## `AxeRadioAPIWrapper.fetch_now_playing()`
> Returns a singular [Track](https://github.com/l0gnes/axe-radio/blob/f40e5b1d5062b74a3e260b314513981c93adcc41/axe-radio/objects/Track.py#L7C10-L7C10) object, denoting the song that is currently playing on the station. This requires no arguments but **this method is a coroutine**. Please make sure to run it as such.

## `AxeRadioAPIWrapper.fetch_upcoming_tracks()`
> Returns a list of [UpcomingTrack](https://github.com/l0gnes/axe-radio/blob/f40e5b1d5062b74a3e260b314513981c93adcc41/axe-radio/objects/UpcomingTrack.py#L4C28-L4C28) objects, which provide similar information to a Track object, while providing the alleged start and end times for each track. There are a few methods to help with handling this extra information.

## > 📜Note: The currently playing track does not consistently appear in the "upcoming tracks" response, so if you are trying to use it for that purpose, dont. 
> In the event that you need the end time for the current song, you can use the start time of the first song when pulling the upcoming tracks.