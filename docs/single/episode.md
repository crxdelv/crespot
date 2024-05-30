<h3 align="center"><code>Episode</code> <kbd>Object</kbd></h3>

A `Show` object contains 12 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`EpisodeSnippet`](/crespot/snippet/episode).

### `str: id`
This is the ID of the episode.

### `str: description` <kbd>Nullable</kbd>
This is the description of the episode.

### `str: html_description` <kbd>Nullable</kbd>
This is the HTML-formatted description of the episode..

### `str: external`
This is the episode's page url of Spotify's website.

### `list(Copyright): copyrights`
This is a list of copyright informations of the show.

### `list(str): markets` <kbd>Undefinable</kbd>
This is the list of available markets of the show.

### `str: name`
This is the name of the show.

### `int: duration`
This is the milliseconds duration of the episode.

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