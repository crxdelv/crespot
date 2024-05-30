<h3 align="center">crespot</h3>
<p align="center">A python wrapper for Spotify API with no required authentication. :musical_note:</p>


### :key: Key concepts
1. Simplified objects are named with the postfix `Snippet`. For example, `ArtistSnippet` is the simplified object of `Artist`.
2. Every objects (excluding detail objects) have the property `_token` and `_market`.
3. `User` object is not included as it lacks of usage due to the unauthenticated access.
4. Every snippets have the method `get_real` that returns a non-snippet class instance.
5. <kbd>:globe_with_meridians:</kbd> badge signifies that the method uses http request(s).

### :book: What is crespot?
crespot is basically a python wrapper for spotify's web api. The greatest thing about crespot is it allows you to access spotify without any access token.

### :nesting_dolls: Classes
crespot has 20 classes, including all the snippets:

#### Objects

1. [`Track`](/crespot/track)
2. `Artist`
3. `Album`
4. `Show`
5. `Episode`
6. `Audiobook`
7. `Chapter`

These classes have their own corresponding snippet. For example, the class `Track` has its own snippet named `TrackSnippet` and its also a class.

Therefore, the total classes of that list is 14.

#### Special object

1. `Playlist`

This object is special as it doesn't have its own snippet and it has track informations.

#### Detail objects

1. `Identification` &ndash; This class contains the external identification of the track.
2. `Image` &ndash; This class contains the size and the source url of an image.
3. `Owner` &ndash; This class contains the information of the playlist's owner.
4. `TrackInfo` &ndash; This class contains the information that the track has inside the playlist. For example, it includes who added the track to the partylist.
5. `Copyright` &ndash; This class contains the copyright information of the object.

### Methods

crespot have 13 methods in its inner class:

#### `__init__(str: token, str: market='ES')`

Market are used to determine if the object is available. Markets are strings that includes two-letter country code. For example, `ES` is spain.

*Spotify chose ES as the default value. It's not my fault.*

#### `search(str: query, str or list: type=['artist', 'album', 'track'], int: page=0) -> dict` <kbd>:globe_with_meridians:</kbd>

This method is used to search for objects.

`type` argument specifies which objects you are looking for. The valid values are `artist`, `album`, `track`, `playlist`, `show`, `episode`, `audiobook`, and `chapter`. For example, `type='track'` only returns tracks.

`page` is how you control the parameter limit and offset. The limit is `20` and cannot be 

#### static `create_token() -> str`

This method creates a temporary access token that can be used at anything.

> [!IMPORTANT]
> Generated access tokens have expiration dates. It is recommended to regenerate your token for **every 5 minutes**.

#### `update_token(str: token)`

This method updates the current token. This is useful for regenerating the token.

If you're too lazy, just use `self._token = your_token`. 

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
