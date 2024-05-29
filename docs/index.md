<h3 align="center">crespot</h3>
<p align="center">A python wrapper for Spotify API with no required authentication. :musical_note:</p>


### :key: Key concepts
1. Simplified objects are named with the postfix `Snippet`. For example, `ArtistSnippet` is the simplified object of `Artist`.
2. Every objects (excluding detail objects) have the property `_token` and `_market`.
3. `User` object is not included as it lacks of usage due to the unauthenticated access.
4. Every snippets has the method `get_real` that returns a non-snippet class instance.

### :book: What is crespot?
crespot is basically a python wrapper for spotify's web api. The greatest thing about crespot is it allows you to access spotify without any access token.

### :nesting_dolls: Classes
crespot has 20 classes, including all the snippets:

#### Objects

1. `Track`
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

# Methods

