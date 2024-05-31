<h3 align="center"><code>Track</code> <kbd>Object</kbd></h3>

A `Track` object contains 13 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`TrackSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/track)

### `str: id`
This is the ID of the track.

### `bool: available`
This is set to true if the track is available to the given market.

### `str: external`
This is the track's page url of Spotify's website.

### `AlbumSnippet: album`
This is the snippet album of the track.

### `Identifications: identifications`
This is the identification information of the track.

### `int: popularity`
This is the popularity score of the track.

### `str: name`
This is the name of the track.

### `int: number`
This is the track number.

### `int: disc`
This is the disc number of the track.

### `bool: explicit`
This is true if the track is explicit.

### `int: duration`
This is the milliseconds duration of the track.

### `str: preview` <kbd>Nullable</kbd>
This is the audio preview url of the track.

### `list(ArtistSnippet): artists`
This is a list of snippet artists of the track.

### Related links

- [`ArtistSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/artist)
- [`AlbumSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/album)
- [`Identifications`](https://github.com/creuserr/crespot/tree/main/docs/detail/identification)
