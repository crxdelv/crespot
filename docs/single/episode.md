<h3 align="center"><code>Episode</code> <kbd>Object</kbd></h3>

A `Episode` object contains 12 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`EpisodeSnippet`](/crespot/snippet/episode).

### `str: id`
This is the ID of the episode.

### `str: description` <kbd>Nullable</kbd>
This is the description of the episode.

### `str: html_description` <kbd>Nullable</kbd>
This is the HTML-formatted description of the episode.

### `str: external`
This is the episode's page url of Spotify's website.

### `list(str): markets` <kbd>Undefinable</kbd>
This is the list of available markets of the episode.

### `str: name`
This is the name of the episode.

### `int: duration`
This is the milliseconds duration of the episode.

### `str: date`
This is the first release date of the album. The format is `yyyy-mm-dd`.

### `str: preview` <kbd>Nullable</kbd>
This is the audio preview url of the track.

### `bool: explicit`
This is true if the track is explicit.

### `bool: available`
This is set to true if the track is available to the given market.

### `str: type`
This is the media type of the show.

### `str: publisher`
This is the publisher of the show.

### `ShowSnippet: show`
This is the snippet show of the episode.

### Related links

- [`ShowSnippet`](/crespot/snippet/show)