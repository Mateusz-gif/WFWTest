import random


class Artist:
    def __init__(self, name, dob, country, list_of_albums=None, list_of_songs=None):
        self.name = name
        self.dob = dob
        self.country = country
        self.list_of_albums = list_of_albums if list_of_albums is not None else []
        self.list_of_songs = list_of_songs if list_of_songs is not None else []

    def display_info(self):
        print(f"Artist Name: {self.name}")
        print(f"Date of Birth: {self.dob}")
        print(f"Country: {self.country}")

        print("\nAlbums:")
        if self.list_of_albums:
            for album in self.list_of_albums:
                print(f" - {album.album_title} ({album.year_of_release})")
        else:
            print(" - None")

        print("\nSongs:")
        if self.list_of_songs:
            for song in self.list_of_songs:
                print(f" - {song.song_title} ({song.year_of_release})")
        else:
            print(" - None")

    def add_album(self, album):
        self.list_of_albums.append(album)

    def add_song(self, song):
        self.list_of_songs.append(song)


class Song:
    def __init__(self, song_title, artist_name, year_of_release):
        self.song_title = song_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release

    def display_info(self):
        print(f"Song Title: {self.song_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")


class Album:
    def __init__(self, album_title, artist_name, year_of_release, list_of_songs=None):
        self.album_title = album_title
        self.artist_name = artist_name
        self.year_of_release = year_of_release
        self.list_of_songs = list_of_songs if list_of_songs is not None else []

    def display_info(self):
        print(f"Album Title: {self.album_title}")
        print(f"Artist Name: {self.artist_name}")
        print(f"Year of Release: {self.year_of_release}")

        print("\nSongs:")
        if self.list_of_songs:
            for song in self.list_of_songs:
                print(f" - {song.song_title} ({song.year_of_release})")
        else:
            print(" - None")

    def add_song(self, title, release_year):
        new_song = Song(title, self.artist_name, release_year)
        self.list_of_songs.append(new_song)
        return new_song


class Playlist:
    def __init__(self, playlist_title, list_of_songs=None):
        self.playlist_title = playlist_title
        self.list_of_songs = list_of_songs if list_of_songs is not None else []

    def add_song(self, song):
        self.list_of_songs.append(song)

    def print_all_song(self):
        print(f"Playlist: {self.playlist_title}")
        if self.list_of_songs:
            for song in self.list_of_songs:
                print(f"{song.song_title} - {song.artist_name} ({song.year_of_release})")
        else:
            print("No songs in playlist.")

    def sort_playlist(self, order='ASC'):
        if order.upper() == 'DES':
            self.list_of_songs.sort(key=lambda song: song.song_title.lower(), reverse=True)
        else:
            self.list_of_songs.sort(key=lambda song: song.song_title.lower())

    def shuffle_playlist(self):
        random.shuffle(self.list_of_songs)


if __name__ == "__main__":
    # Create artist
    artist = Artist("Taylor Swift", "13-12-1989", "USA")

    # Create albums
    album_1989 = Album("1989", artist.name, 2014)
    album_red = Album("Red", artist.name, 2012)
    album_midnights = Album("Midnights", artist.name, 2022)

    # Create a few songs manually
    song1 = Song("Blank Space", artist.name, 2014)
    song2 = Song("Style", artist.name, 2014)
    song3 = Song("Shake It Off", artist.name, 2014)
    song4 = Song("All Too Well", artist.name, 2012)
    song5 = Song("Red", artist.name, 2012)
    song6 = Song("Anti-Hero", artist.name, 2022)

    # Use add_song() from Album class to add two songs
    album_song1 = album_1989.add_song("Bad Blood", 2014)
    album_song2 = album_1989.add_song("Wildest Dreams", 2014)

    # Add more songs to albums
    album_red.add_song("State Of Grace", 2012)
    album_red.add_song("Begin Again", 2012)

    album_midnights.add_song("Bejeweled", 2022)
    album_midnights.add_song("Karma", 2022)

    # Update artist info
    artist.add_album(album_1989)
    artist.add_album(album_red)
    artist.add_album(album_midnights)

    artist.add_song(song1)
    artist.add_song(song2)
    artist.add_song(song3)
    artist.add_song(song4)
    artist.add_song(song5)
    artist.add_song(song6)
    artist.add_song(album_song1)
    artist.add_song(album_song2)

    # Add album songs to artist song list
    for s in album_red.list_of_songs:
        artist.add_song(s)

    for s in album_midnights.list_of_songs:
        artist.add_song(s)

    # Create playlist
    playlist = Playlist("Taylor Swift Mix")

    # Add all songs from albums to playlist
    for s in album_1989.list_of_songs:
        playlist.add_song(s)

    for s in album_red.list_of_songs:
        playlist.add_song(s)

    for s in album_midnights.list_of_songs:
        playlist.add_song(s)

    # Also add some manually created songs
    playlist.add_song(song1)
    playlist.add_song(song2)
    playlist.add_song(song3)
    playlist.add_song(song4)
    playlist.add_song(song5)
    playlist.add_song(song6)

    # Demonstration
    print("========== ARTIST INFO ==========")
    artist.display_info()

    print("\n========== SONG INFO ==========")
    song1.display_info()

    print("\n========== ALBUM INFO ==========")
    album_1989.display_info()

    print("\n========== PLAYLIST BEFORE SORT ==========")
    playlist.print_all_song()

    playlist.sort_playlist('ASC')
    print("\n========== PLAYLIST SORTED ASC ==========")
    playlist.print_all_song()

    playlist.sort_playlist('DES')
    print("\n========== PLAYLIST SORTED DES ==========")
    playlist.print_all_song()

    playlist.shuffle_playlist()
    print("\n========== PLAYLIST SHUFFLED ==========")
    playlist.print_all_song()