<h3 align="center"><code>Album</code> <kbd>Object</kbd></h3>

An `Album` object contains 6 properties. (excluding `_market` and `_token`)

### `str: id`
This is the ID of the album.

### `str: label`
This is the label name of the album.

### `str: type`
This is the album type. It can be an `single`, `album`, or `compilation`.

### `str: external`
This is the albums's page url of Spotify's website.

### `int: popularity`
This is the popularity score of the album.

### `int: total`
This is the total amount of tracks in the albums.

### `str: name`
This is the name of the album.

### `str: date`
This is the first release date of the album. The format is `yyyy-mm-dd`.

### `list(str): market` <kbd>Undefinable</kbd>
This is the list of available markets of the album.

### `list(ArtistSnippet): artists`
This is a list of snippet artists of the album.

### `list(TrackSnippet): tracks`
This is a list of snippet tracks of the album.

### `list(Image): images`
This is the artwork images of the album.