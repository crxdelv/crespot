<h3 align="center"><code>Audiobook</code> <kbd>Object</kbd></h3>

An `Audiobook` object contains 14 properties (excluding `_market` and `_token`). For the snippet class, please refer to [`AudiobookSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/audiobook).

### `str: id`
This is the ID of the audiobook.

### `str: description` <kbd>Nullable</kbd>
This is the description of the audiobook.

### `str: html_description` <kbd>Nullable</kbd>
This is the HTML-formatted description of the audiobook.

### `str: external`
This is the audiobook's page url of Spotify's website.

### `list(Copyright): copyrights`
This is a list of copyright informations of the audiobook.

### `list(str): markets` <kbd>Undefinable</kbd>
This is the list of available markets of the audiobook.

### `str: name`
This is the name of the audiobook.

### `int: total`
This is the total amount of chapters in the audiobook.

### `str: type`
This is the media type of the audiobook.

### `str: publisher`
This is the publisher of the audiobook.

### `list(ChapterSnippet): chapters`
This is a list of snippet chapters of the audiobook.

### `list(Image): images`
This is the artwork images of the audiobook.

### `list(str): authors`
This is a list of authors' name of the audiobook.

### `list(str): narrators`
This is a list of narrators' name of the audiobook.

### `str: edition` <kbd>Nullable</kbd>
This is the edition label of the audiobook.

### Related links

- [`Copyright`](https://github.com/creuserr/crespot/tree/main/docs/detail/copyright)
- [`ChapterSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/chapter)
- [`Image`](https://github.com/creuserr/crespot/tree/main/docs/detail/image)
