class Song:
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return (
            f"{'Performer:':<10} {self.artist}\n"
            f"{'Title:':<10} {self.track_title}\n"
            f"{'Album:':<10} {self.album}\n"
            f"{'Year:':<10} {self.year}\n"
        )

song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(song1)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)
print(song2)