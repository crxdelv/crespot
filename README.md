<h3 align="center">crespot</h3>
<p align="center">Limitlessly access spotify web api without authorization tokens.</p>

```py
token = CreSpot.create_token()
spot = CreSpot(token, 'EN')

result = spot.search('Prologue aespa', 'track')
print(result.tracks[0])
```

### Installation

Download the file [`crespot.py`](https://github.com/creuserr/crespot/blob/main/dist/crespot.py.md) and import it.

```py
from crespot import CreSpot
```

> [!NOTE]
> This library uses the dependency `requests`.

### Documentation

**Constructor**
- [`CreSpot`](https://github.com/creuserr/crespot/tree/main/docs/index.md.md) &ndash; If you're new, please read this document first.

**Singles**
- [`Track`](https://github.com/creuserr/crespot/tree/main/docs/single/track.md)
- [`Artist`](https://github.com/creuserr/crespot/tree/main/docs/single/artist.md)
- [`Episode`](https://github.com/creuserr/crespot/tree/main/docs/single/episode.md)
- [`Chapter`](https://github.com/creuserr/crespot/tree/main/docs/single/chapter.md)

**Groups**
- [`Audiobook`](https://github.com/creuserr/crespot/tree/main/docs/group/audiobook.md)
- [`Album`](https://github.com/creuserr/crespot/tree/main/docs/group/album.md)
- [`Show`](https://github.com/creuserr/crespot/tree/main/docs/group/show.md)
- [`Playlist`](https://github.com/creuserr/crespot/tree/main/docs/group/playlist.md)


**Details**
- [`Identification`](https://github.com/creuserr/crespot/tree/main/docs/detail/identification.md)
- [`Image`](https://github.com/creuserr/crespot/tree/main/docs/detail/image.md)
- [`Owner`](https://github.com/creuserr/crespot/tree/main/docs/detail/owner.md)
- [`TrackInfo`](https://github.com/creuserr/crespot/tree/main/docs/detail/trackinfo.md)
- [`Copyright`](https://github.com/creuserr/crespot/tree/main/docs/detail/copyright.md)
- [`Error`](https://github.com/creuserr/crespot/tree/main/docs/detail/copyright.md)

**Snippets**
- [`AudiobookSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/audiobook.md)
- [`AlbumSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/album.md)
- [`ShowSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/show.md)
- [`TrackSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/track.md)
- [`ArtistSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/artist.md)
- [`EpisodeSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/episode.md)
- [`ChapterSnippet`](https://github.com/creuserr/crespot/tree/main/docs/snippet/chapter.md)