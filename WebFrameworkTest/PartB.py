import unittest
from unittest.mock import patch

from PartA import Artist, Song, Album, Playlist


class TestMusicPlaylistSystem(unittest.TestCase):

    def setUp(self):
        self.artist = Artist("Taylor Swift", "13-12-1989", "USA")
        self.song1 = Song("Blank Space", "Taylor Swift", 2014)
        self.song2 = Song("Style", "Taylor Swift", 2014)
        self.song3 = Song("Shake It Off", "Taylor Swift", 2014)
        self.album = Album("1989", "Taylor Swift", 2014)
        self.playlist = Playlist("Taylor Hits")

    # 4 tests: object IS instance of class
    def test_artist_is_instance_of_artist(self):
        self.assertIsInstance(self.artist, Artist)

    def test_song_is_instance_of_song(self):
        self.assertIsInstance(self.song1, Song)

    def test_album_is_instance_of_album(self):
        self.assertIsInstance(self.album, Album)

    def test_playlist_is_instance_of_playlist(self):
        self.assertIsInstance(self.playlist, Playlist)

    # 4 tests: object is NOT instance of class
    def test_artist_is_not_instance_of_song(self):
        self.assertNotIsInstance(self.artist, Song)

    def test_song_is_not_instance_of_album(self):
        self.assertNotIsInstance(self.song1, Album)

    def test_album_is_not_instance_of_playlist(self):
        self.assertNotIsInstance(self.album, Playlist)

    def test_playlist_is_not_instance_of_artist(self):
        self.assertNotIsInstance(self.playlist, Artist)

    # 2 tests: identical and unidentical but similar objects
    def test_identical_objects(self):
        same_song = self.song1
        self.assertIs(self.song1, same_song)

    def test_unidentical_but_similar_objects(self):
        similar_song = Song("Blank Space", "Taylor Swift", 2014)
        self.assertIsNot(self.song1, similar_song)
        self.assertEqual(self.song1.song_title, similar_song.song_title)
        self.assertEqual(self.song1.artist_name, similar_song.artist_name)
        self.assertEqual(self.song1.year_of_release, similar_song.year_of_release)

    # 4 tests: add_song() and add_album()
    def test_artist_add_album(self):
        self.artist.add_album(self.album)
        self.assertIn(self.album, self.artist.list_of_albums)
        self.assertEqual(len(self.artist.list_of_albums), 1)

    def test_artist_add_song(self):
        self.artist.add_song(self.song1)
        self.assertIn(self.song1, self.artist.list_of_songs)
        self.assertEqual(len(self.artist.list_of_songs), 1)

    def test_album_add_song(self):
        new_song = self.album.add_song("Bad Blood", 2014)
        self.assertIn(new_song, self.album.list_of_songs)
        self.assertEqual(new_song.song_title, "Bad Blood")
        self.assertEqual(new_song.artist_name, "Taylor Swift")
        self.assertEqual(new_song.year_of_release, 2014)

    def test_playlist_add_song(self):
        self.playlist.add_song(self.song1)
        self.assertIn(self.song1, self.playlist.list_of_songs)
        self.assertEqual(len(self.playlist.list_of_songs), 1)

    # 3 tests: sort_playlist() and shuffle_playlist()
    def test_sort_playlist_ascending(self):
        self.playlist.add_song(self.song2)   # Style
        self.playlist.add_song(self.song1)   # Blank Space
        self.playlist.add_song(self.song3)   # Shake It Off

        self.playlist.sort_playlist('ASC')
        titles = [song.song_title for song in self.playlist.list_of_songs]
        self.assertEqual(titles, ["Blank Space", "Shake It Off", "Style"])

    def test_sort_playlist_descending(self):
        self.playlist.add_song(self.song2)   # Style
        self.playlist.add_song(self.song1)   # Blank Space
        self.playlist.add_song(self.song3)   # Shake It Off

        self.playlist.sort_playlist('DES')
        titles = [song.song_title for song in self.playlist.list_of_songs]
        self.assertEqual(titles, ["Style", "Shake It Off", "Blank Space"])

    @patch('random.shuffle')
    def test_shuffle_playlist(self, mock_shuffle):
        self.playlist.add_song(self.song1)
        self.playlist.add_song(self.song2)
        self.playlist.add_song(self.song3)

        self.playlist.shuffle_playlist()
        mock_shuffle.assert_called_once_with(self.playlist.list_of_songs)


if __name__ == "__main__":
    unittest.main()