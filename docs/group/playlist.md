<h3 align="center"><code>Playlist</code> <kbd>Object</kbd></h3>

A `Playlist` object contains 12 properties (excluding `_market` and `_token`).

### `str: id`
This is the ID of the playlist.

### `bool: collaborative`
This is set to true if the playlist allow public collaboration.

### `str: description` <kbd>Nullable</kbd>
This is the description of the playlist.

### `str: external`
This is the albums's page url of Spotify's website.

### `Owner: owner`
This is the owner of the playlist.

### `int: followers`
This is the total amount of followers of the playlist.

### `str: name`
This is the name of the playlist.

### `int: total`
This is the total amount of tracks/episodes in the playlist.

### `str: snapshot`
This is the version identifier of the current playlist's version.

### `list(TrackInfo): tracks`
This is a list of track informations of the playlist.

### `list(Image): images`
This is the artwork images of the playlist.

### Related links

- [`Owner`](https://github.com/creuserr/crespot/tree/main/docs/detail/owner.md)
- [`TrackInfo`](https://github.com/creuserr/crespot/tree/main/docs/detail/trackinfo.md)
- [`Image`](https://github.com/creuserr/crespot/tree/main/docs/detail/image.md)

<img src="https://komarev.com/ghpvc/?username=creuserr" alt="" width="0"></img>
