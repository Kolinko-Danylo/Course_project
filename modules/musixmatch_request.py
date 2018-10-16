from musixmatch import Musixmatch
musixmatch = Musixmatch('2d6016b0ba648c1e1b10321e982b0db9')


def get_track_id(artist_name, track_name):
     """Utility to get track_id by author name and song name."""
     dict_id = musixmatch.track_search(q_artist= artist_name, q_track= track_name,page_size=100, page=1, s_track_rating='desc')
     track_list = dict_id['message']['body']['track_list']
     if not track_list:
          return 'nothing_found'
     track = track_list[0]['track']
     if not track['has_lyrics']:
          return 'no_lyrics'
     return track['track_id']


def get_track_lyrics(track_id):
     """Utility to get track lyrics by track_id"""
     try:
          track_info = musixmatch.track_lyrics_get(track_id)['message']['body']
          if not track_info:
               raise ValueError
          return track_info['lyrics']['lyrics_body']
     except ValueError:
          return None