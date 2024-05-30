<h3 align="center"><code>Show</code> <kbd>Object</kbd></h3>

A `Show` object contains 12 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`ShowSnippet`](/crespot/snippet/show)

### `str: id`
This is the ID of the show.

### `str: description` <kbd>Nullable</kbd>
This is the description of the show.

### `str: html_description` <kbd>Nullable</kbd>
This is the HTML-formatted description of the show.

### `str: external`
This is the albums's page url of Spotify's website.

### `list(Copyright): copyrights`
This is a list of copyright informations of the show.

### `list(str): markets` <kbd>Undefinable</kbd>
This is the list of available markets of the show.

### `str: name`
This is the name of the show.

### `int: total`
This is the total amount of episodes in the episodes.

### `str: type`
This is the media type of the show.

### `str: publisher`
This is the publisher of the show.

### `list(EpisodeSnippet): episodes`
This is a list of snippet episodes of the show.

### `list(Image): images`
This is the artwork images of the playlist.

### Related links

- [`Copyright`](/crespot/detail/copyright)
- [`EpisodeSnippet`](/crespot/snippet/episode)
- [`Image`](/crespot/detail/image)