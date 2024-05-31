from urllib.parse import quote
import requests, json

class CreSpot:
  _market = 'ES'
  _version = 1
  
  # Detail objects
  
  class Error(Exception):
    def __init__(self, req, token, market):
      self._token = token
      self._market = market
      self.error = req.status_code
      try:
        self.content = json.loads(req.text)['error']['message']
      except:
        pass
    
    def __str__(self):
      return f'{self.error} {self.content}'
      
    def __repr__(self):
      return self.__str__()
  
  class Identifications:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.isrc = data['isrc'] if 'isrc' in data else None
      self.ean = data['ean'] if 'ean' in data else None
      self.upc = data['upc'] if 'upc' in data else None
    
    def __str__(self):
      avail = []
      if 'isrc' in self: avail.append('isrc')
      if 'ean' in self: avail.append('ean')
      if 'upc' in self: avail.append('upc')
      avail = ', '.join(avail)
      if len(avail) == 0: avail = 'None'
      return f'Identification: {avail}'
    
    def __repr__(self):
      return self.__str__()
  
  class TrackInfo:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.local = data['local']
      if 'added_by' in data: self.owner = CreSpot.Owner(data['added_by'], token, market)
      if 'added_at' in data: self.date = data['added_at']
      if data['type'] == 'episode':
        self.track = CreSpot.Episode(data['track'], token, market)
      else:
        self.track = CreSpot.Track(data['track'], token, market)
  
  class Owner:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.external = data['external_urls']['spotify']
      self.followers = data['followers']['total']
      self.id = data['id']
      if 'display_name' in data: self.name = data['display_name']
  
  class Image:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.width = data['width']
      self.height = data['height']
      self.url = data['url']
    
    def __str__(self):
      return f'Image: {self.width}x{self.height}'
    
    def __repr__(self):
      return self.__str__()
  
  class Copyright:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.text = data['text']
      self.type = data['type']
    
    def __str__(self):
      return f'Copyright: ({self.type}) {self.text}'
    
    def __repr__(self):
      return self.__str__()
  
  # Snippet objects
  
  class AlbumSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      self.type = data['album_type']
      self.total = data['total_tracks']
      self.name = data['name']
      self.date = data['release_date']
      self.artists = CreSpot._iter(data['artists'], CreSpot.ArtistSnippet, token, market)
      if 'available_markets' in data: self.markets = data['available_markets']
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
    
    def __str__(self):
      artists = ', '.join([x.name for x in self.artists])
      return f'AlbumSnippet: {self.name} - {artists}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/albums/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Album(res, self._token, self._market)
  
  class ChapterSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.description = data['description']
      self.html_description = data['html_description']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.duration = data['duration_ms']
      self.number = data['chapter_number']
      self.explicit = data['explicit']
      self.available = data['is_playable']
      self.languages = data['languages']
      self.name = data['name']
      self.preview = data['audio_preview_url']
      self.date = data['release_date']
      self.id = data['id']
      
    def __str__(self):
      return f'ChapterSnippet: {self.name}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/chapters/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Chapter(res, self._token, self._market)
  
  class ShowSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.description = data['description']
      self.html_description = data['html_description']
      self.copyrights = CreSpot._iter(data['copyrights'], CreSpot.Copyright, token, market)
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.publisher = data['publisher']
      self.total = data['total_episodes']
      self.type = data['media_type']
    
    def __str__(self):
      return f'ShowSnippet: {self.name} - {self.publisher}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/shows/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Show(res, self._token, self._market)
  
  class EpisodeSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.description = data['description']
      self.html_description = data['html_description']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.duration = data['duration_ms']
      self.explicit = data['explicit']
      self.available = data['is_playable']
      self.languages = data['languages']
      self.name = data['name']
      self.preview = data['audio_preview_url']
      self.date = data['release_date']
      self.id = data['id']
      
    def __str__(self):
      return f'EpisodeSnippet: {self.name}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/episodes/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Episode(res, self._token, self._market)
  
  class ArtistSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.name = data['name']
      self.id = data['id']
      self.external = data['external_urls']['spotify']
    
    def __str__(self):
      return f'ArtistSnippet: {self.name}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/artists/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Artist(res, self._token, self._market)
  
  class TrackSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      self.external = data['external_urls']['spotify']
      self.name = data['name']
      self.number = data['track_number']
      self.disc = data['disc_number']
      self.explicit = data['explicit']
      self.duration = data['duration_ms']
      self.preview = data['preview_url']
      self.artists = CreSpot._iter(data['artists'], CreSpot.ArtistSnippet, token, market)
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/tracks/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Track(res, self._token, self._market)
    
    def __str__(self):
      return f'TrackSnippet: {self.name} - {self.artists[0].name}'
    
    def __repr__(self):
      return self.__str__()
  
  class AudiobookSnippet:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.description = data['description']
      self.html_description = data['html_description']
      self.copyrights = CreSpot._iter(data['copyrights'], CreSpot.Copyright, token, market)
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.publisher = data['publisher']
      self.authors = [x['name'] for x in data['authors']]
      self.narrators = [x['name'] for x in data['narrators']]
      self.edition = data['edition']
      self.total = data['total_chapters']
      self.type = data['media_type']
      
    def __str__(self):
      return f'AudiobookSnippet: {self.name} - {self.publisher}'
    
    def __repr__(self):
      return self.__str__()
    
    def get_real(self):
      _h = { 'Authorization': 'Bearer ' + self._token }
      req = requests.get(f'https://api.spotify.com/v1/audiobooks/{self.id}?market={self._market}', headers=_h)
      if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
      res = json.loads(req.text)
      return CreSpot.Audiobook(res, self._token, self._market)
  
  # Group objects
  
  class Show:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      self.description = data['description']
      self.html_description = data['html_description']
      self.copyrights = CreSpot._iter(data['copyrights'], CreSpot.Copyright, token, market)
      if 'available_markets' in data: self.markets = data['available_markets']
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.publisher = data['publisher']
      self.total = data['total_episodes']
      self.type = data['media_type']
      self.episodes = CreSpot._iter(data['episodes']['items'], CreSpot.EpisodeSnippet, token, market)
     
    def __str__(self):
      return f'Show: {self.name} - {self.publisher}'
    
    def __repr__(self):
      return self.__str__()
  
  class Audiobook:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.description = data['description']
      self.html_description = data['html_description']
      self.copyrights = CreSpot._iter(data['copyrights'], CreSpot.Copyright, token, market)
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.publisher = data['publisher']
      self.authors = [x['name'] for x in data['authors']]
      self.narrators = [x['name'] for x in data['narrators']]
      self.edition = data['edition']
      self.total = data['total_chapters']
      self.type = data['media_type']
      self.chapters = CreSpot._iter(data['chapters']['items'], CreSpot.ChapterSnippet, token, market)
     
    def __str__(self):
      return f'Audiobook: {self.name} - {self.publisher}'
    
    def __repr__(self):
      return self.__str__()
  
  class Playlist:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['playlist_id']
      self.collaborative = data['collaborative']
      self.description = data['description']
      self.external = data['external_urls']['spotify']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.owner = CreSpot.Owner(data['owner'], token, market)
      self.followers = data['followers']['total']
      self.snapshot = data['snapshot_id']
      self.total = data['tracks']['total']
      self.tracks = CreSpot._iter(data['tracks']['items'], CreSpot.TrackInfo, token, market)
  
  class Album:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      self.popularity = data['popularity']
      self.label = data['label']
      self.type = data['album_type']
      self.total = data['total_tracks']
      self.name = data['name']
      self.date = data['release_date']
      self.artists = CreSpot._iter(data['artists'], CreSpot.ArtistSnippet, token, market)
      if 'available_markets' in data: self.markets = data['available_markets']
      self.external = data['external_urls']['spotify']
      self.tracks = CreSpot._iter(data['tracks']['items'], CreSpot.TrackSnippet, token, market)
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
    
    def __str__(self):
      artists = ', '.join([x.name for x in self.artists])
      return f'Album: {self.name} - {artists}'
    
    def __repr__(self):
      return self.__str__()
  
  # Single objects
  
  class Episode:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.description = data['description']
      self.html_description = data['html_description']
      self.external = data['external_urls']['spotify']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.duration = data['duration_ms']
      self.explicit = data['explicit']
      self.available = data['is_playable']
      self.languages = data['languages']
      self.name = data['name']
      self.date = data['release_date']
      self.id = data['id']
      self.preview = data['audio_preview_url']
      self.show = CreSpot.ShowSnippet(data['show'], token, market)
    
    def __str__(self):
      return f'Episode: {self.name} - {self.show.name}'
    
    def __repr__(self):
      return self.__str__()
  
  class Chapter:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.description = data['description']
      self.html_description = data['html_description']
      if 'available_markets' in data: self.markets = data['available_markets']
      self.duration = data['duration_ms']
      self.number = data['chapter_number']
      self.explicit = data['explicit']
      self.available = data['is_playable']
      self.languages = data['languages']
      self.name = data['name']
      self.preview = data['audio_preview_url']
      self.date = data['release_date']
      self.id = data['id']
      self.audiobook = CreSpot.AudiobookSnippet(data['audiobook'], token, market)
      
    def __str__(self):
      return f'Chapter: {self.name}'
    
    def __repr__(self):
      return self.__str__()
  
  class Artist:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.external = data['external_urls']['spotify']
      self.id = data['id']
      self.followers = data['followers']['total']
      self.genres = data['genres']
      self.images = CreSpot._iter(data['images'], CreSpot.Image, token, market)
      self.name = data['name']
      self.popularity = data['popularity']
    
    def __str__(self):
      return f'Artist: {self.name}'
    
    def __repr__(self):
      return self.__str__()
  
  class Track:
    def __init__(self, data, token, market):
      self._token = token
      self._market = market
      self.id = data['id']
      self.available = data['is_playable']
      self.external = data['external_urls']['spotify']
      self.album = CreSpot.AlbumSnippet(data['album'], token, market)
      self.identifications = CreSpot.Identifications(data['external_ids'], token, market)
      self.popularity = data['popularity']
      self.name = data['name']
      self.number = data['track_number']
      self.disc = data['disc_number']
      self.explicit = data['explicit']
      self.duration = data['duration_ms']
      self.preview = data['preview_url']
      self.artists = CreSpot._iter(data['artists'], CreSpot.ArtistSnippet, token, market)
    
    def __str__(self):
      return f'Track: {self.name} - {self.artists[0].name}'
    
    def __repr__(self):
      return self.__str__()
  
  # Methods
  
  def create_token():
    req = requests.get('https://open.spotify.com/get_access_token?reason=transport&productType=web_player')
    return json.loads(req.text)['accessToken']
  
  def __init__(self, token, market = 'ES'):
    self._token = token
    self._market = market
  
  def _iter(data, ins, token, market):
    res = []
    for d in data:
      res.append(ins(d, token, market))
    return res
  
  def update_token(self, token):
    self._token = token
  
  # HTTP Based Objects
  def search(self, query, types=['artist', 'album', 'track'], page=0):
    _m = self._market
    q = quote(query)
    t = type(types)
    limit = 20 * (page + 1)
    offset = limit - 20
    t = ','.join(types) if t is list or t is tuple else types
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/search?q={q}&type={t}&market={_m}&limit={limit}&offset={offset}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    ins = {
      'total': 0
    }
    if 'tracks' in res:
      ins['tracks'] = CreSpot._iter(res['tracks']['items'], CreSpot.Track, self._token, self._market)
      ins['total'] += len(ins['tracks'])
    if 'albums' in res:
      ins['albums'] = CreSpot._iter(res['albums']['items'], CreSpot.AlbumSnippet, self._token, self._market)
      ins['total'] += len(ins['albums'])
    if 'artists' in res:
      ins['artists'] = CreSpot._iter(res['artists']['items'], CreSpot.Artist, self._token, self._market)
      ins['total'] += len(ins['artists'])
    if 'shows' in res:
      ins['shows'] = CreSpot._iter(res['shows']['items'], CreSpot.ShowSnippet, self._token, self._market)
      ins['total'] += len(ins['shows'])
    if 'episodes' in res:
      ins['episodes'] = CreSpot._iter(res['episodes']['items'], CreSpot.EpisodeSnippet, self._token, self._market)
      ins['total'] += len(ins['episodes'])
    if 'audiobooks' in res:
      ins['audiobooks'] = CreSpot._iter(res['audiobooks']['items'], CreSpot.AudiobookSnippet, self._token, self._market)
      ins['total'] += len(ins['audiobooks'])
    if 'chapters' in res:
      ins['chapters'] = CreSpot._iter(res['chapters']['items'], CreSpot.ChapterSnippet, self._token, self._market)
      ins['total'] += len(ins['chapters'])
    return ins
  
  def get_grenre_seeds(self):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/recommendations/available-genre-seeds', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return res
    
  def get_markets(self):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/markets', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return res
  
  def get_artist(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/artists/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Artist(res)
  
  def get_album(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/albums/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Album(res)
  
  def get_track(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/tracks/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Track(res)
  
  def get_playlist(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/playlists/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Playlist(res)
  
  def get_show(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/shows/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Show(res)
  
  def get_episode(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/episodes/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Episode(res)
  
  def get_audiobook(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/audiobooks/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Audiobook(res)
  
  def get_chapter(self, key):
    _m = self._market
    _h = { 'Authorization': 'Bearer ' + self._token }
    req = requests.get(f'https://api.spotify.com/v1/chapters/{key}', headers=_h)
    if req.status_code > 399: raise CreSpot.Error(req, self._token, self._market)
    res = json.loads(req.text)
    return CreSpot.Chapter(res)