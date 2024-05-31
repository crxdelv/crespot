<h3 align="center"><code>Chapter</code> <kbd>Object</kbd></h3>

A `Chapter` object contains 14 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`ChapterSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/chapter.md).

### `str: id`
This is the ID of the chapter.

### `str: description` <kbd>Nullable</kbd>
This is the description of the chapter.

### `str: html_description` <kbd>Nullable</kbd>
This is the HTML-formatted description of the chapter.

### `str: external`
This is the chapter's page url of Spotify's website.

### `list(str): markets` <kbd>Undefinable</kbd>
This is the list of available markets of the chapter.

### `str: name`
This is the name of the chapter.

### `int: duration`
This is the milliseconds duration of the chapter.

### `str: date`
This is the first release date of the album. The format is `yyyy-mm-dd`.

### `str: preview` <kbd>Nullable</kbd>
This is the audio preview url of the chapter.

### `bool: explicit`
This is true if the chapter is explicit.

### `bool: available`
This is set to true if the chapter is available to the given market.

### `str: type`
This is the media type of the show.

### `str: publisher`
This is the publisher of the show.

### `AudiobookSnippet: audiobook`
This is the snippet audiobook of the chapter.

### Related links

- [`AudiobookSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/audiobook.md)