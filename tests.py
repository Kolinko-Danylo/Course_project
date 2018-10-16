from modules.musixmatch_request import get_track_id, get_track_lyrics
import unittest

class Track_id_Test(unittest.TestCase):
    def test_track(self):
        self.assertEqual(int(get_track_id("Maroon 5", "Sugar")), 74268378)
    def test_track_2(self):
        self.assertEqual(int(get_track_id("Океан Ельзи", "911")), 85057362)
    def test_track_3(self):
        self.assertEqual(int(get_track_id("Adele", "Hello")), 84213309)

class Track_lyrics_Test(unittest.TestCase):
    def test_track_4(self):
        self.assertEqual(get_track_id("Hans Zimmer", "Time"), "no_lyrics")
    def test_track_5(self):
        self.assertEqual(get_track_id("Adele", "911"), "nothing_found")
    def test_track_6(self):
        self.assertTrue(get_track_lyrics(get_track_id("Adele", "Hello").strip().startswith("Hello, it's me")))
    def test_track_7(self):
        self.assertEqual(get_track_lyrics(get_track_id("Hans Zimmer", "Time")), None)
