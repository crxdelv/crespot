<h3 align="center">crespot</h3>
<p align="center">A python wrapper for Spotify API with no required authentication. :musical_note:</p>

### :key: Must-read informations

1. `User` object is not included as it lacks of usage due to the unauthenticated access.
2. Some properties are not added, such as `href` and `uri`.
3. <kbd>Nullable</kbd> are properties that can be `None`, while <kbd>Undefinable</kbd> are properties that can not exist.
4. <kbd>:globe_with_meridians:</kbd> badge signifies that the method uses http request(s).

**Additional informations**

1. Simplified objects are named with the postfix `Snippet`. For example, `ArtistSnippet` is the simplified object of `Artist`.
2. Every class have the property `_token` and `_market`.
3. Every snippets have the method `get_real` <kbd>:globe_with_meridians:</kbd> that returns a non-snippet class instance.

### :book: What is crespot?
crespot is basically a python wrapper for spotify's web api. The greatest thing about crespot is it allows you to access spotify without any access token.

### :building_construction: Constructor

```python
CreSpot(str: token, str: market='ES')
```

### :nesting_dolls: Classes
crespot has 20 classes, including all the snippets:

#### Objects

1. [`Track`](https://github.com/creuserr/crespot/tree/main/docs/single/track)
2. [`Artist`](https://github.com/creuserr/crespot/tree/main/docs/single/artist)
3. [`Album`](https://github.com/creuserr/crespot/tree/main/docs/group/album)
4. [`Show`](https://github.com/creuserr/crespot/tree/main/docs/group/show)
5. [`Episode`](https://github.com/creuserr/crespot/tree/main/docs/single/episode)
6. [`Audiobook`](https://github.com/creuserr/crespot/tree/main/docs/group/audiobook)
7. [`Chapter`](https://github.com/creuserr/crespot/tree/main/docs/single/chapter)

These classes have their own corresponding snippet. For example, the class `Track` has its own snippet named `TrackSnippet` and its also a class.

Therefore, the total classes of that list is 14.

#### Special object

1. [`Playlist`](https://github.com/creuserr/crespot/tree/main/docs/group/playlist)

This object is special as it doesn't have its own snippet and it has track informations.

#### Detail objects

1. [`Identification`](https://github.com/creuserr/crespot/tree/main/docs/detail/identification) &ndash; This class contains the external identification of the track.
2. [`Image`](https://github.com/creuserr/crespot/tree/main/docs/detail/image) &ndash; This class contains the width <kbd>Nullable</kbd>, the height <kbd>Nullable</kbd>, and the source url of an image.
3. [`Owner`](https://github.com/creuserr/crespot/tree/main/docs/detail/owner) &ndash; This class contains the information of the playlist's owner.
4. [`TrackInfo`](https://github.com/creuserr/crespot/tree/main/docs/detail/trackinfo) &ndash; This class contains the information that the track has inside the playlist. For example, it includes who added the track to the partylist.
5. [`Copyright`](https://github.com/creuserr/crespot/tree/main/docs/detail/copyright) &ndash; This class contains the copyright information of the object.
6. [`Error`](https://github.com/creuserr/crespot/tree/main/docs/detail/copyright) &ndash; This class contains the error status and its JSON response. This class only can only appear when an HTTP request fails.

### Methods

crespot have 13 methods in its inner class:

#### `__init__(str: token, str: market='ES')`

Market are used to determine if the object is available. Markets are strings that includes two-letter country code. For example, `ES` is spain.

*Spotify chose ES as the default value. It's not my fault.*

#### `search(str: query, str or list: type=['artist', 'album', 'track'], int: page=0) -> dict` <kbd>:globe_with_meridians:</kbd>

This method is used to search for objects.

`type` argument specifies which objects you are looking for. The valid values are `artist`, `album`, `track`, `playlist`, `show`, `episode`, `audiobook`, and `chapter`. For example, `type='track'` only returns tracks.

`page` is how you control the parameter limit and offset. The limit is multiplied by 20 and defaults by 20. For example, if the page is 1, then the limit is 40 and the offset is 20.

This method will return this schema:
```py
{
  'total': int,
  'tracks': list(Track),
  'albums': list(AlbumSnippet),
  'artists': list(Artist),
  'shows': list(ShowSnippet),
  'episodes': list(EpisodeSnippet),
  'audiobooks': list(AudiobookSnippet),
  'chapters': list(ChapterSnippet),
  'playlists': list(Playlist)
}
```

Please note that everything (except `total`) are undefinable.

#### static `create_token() -> str`

This method creates a temporary access token that can be used at anything.

> [!IMPORTANT]
> Generated access tokens have expiration dates. It is recommended to regenerate your token for **every 5 minutes**.

#### `update_token(str: token)`

This method updates the current token. This is useful for regenerating the token.

Under the hood, it's basically: `self._token = your_token`. 

#### `get_genre_seeds() -> list(str)` <kbd>:globe_with_meridians:</kbd>

This method returns a list of recommended genre seeds.

#### `get_markets() -> list(str)` <kbd>:globe_with_meridians:</kbd>

This method returns a list of available markets.

#### `get_track(str: track_id) -> Track` <kbd>:globe_with_meridians:</kbd>

This method returns a `Track` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_artist(str: artist_id) -> Artist` <kbd>:globe_with_meridians:</kbd>

This method returns an `Artist` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_album(str: album_id) -> Album` <kbd>:globe_with_meridians:</kbd>

This method returns an `Album` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_playlist(str: playlist_id) -> Playlist` <kbd>:globe_with_meridians:</kbd>

This method returns a `Playlist` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_show(str: show_id) -> Show` <kbd>:globe_with_meridians:</kbd>

This method returns a `Show` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_episode(str: episode_id) -> Episode` <kbd>:globe_with_meridians:</kbd>

This method returns an `Episode` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_audiobook(str: audiobook_id) -> Audiobook` <kbd>:globe_with_meridians:</kbd>

This method returns an `Audiobook` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.

#### `get_chapter(str: chapter_id) -> Chapter` <kbd>:globe_with_meridians:</kbd>

This method returns a `Chapter` object if the search is successful. Please be aware of the IDs because every objects has the same ID format but different instance.