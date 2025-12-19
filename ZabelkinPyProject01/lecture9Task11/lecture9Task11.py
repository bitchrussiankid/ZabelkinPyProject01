class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def displayInfo(self):
        return f"{self.artist} - {self.title} ({self.duration})"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def removeSong(self, songTitle):
        for song in self.songs:
            if songTitle == song.title:
                self.songs.remove(song)
                break

    def totalDuration(self):
        self.totalSeconds = 0
        for song in self.songs:
            self.totalSeconds += int(song.duration.split(":")[0]) * 60 + int(song.duration.split(":")[1])
        
        def formatDuration(totalSeconds):
            minutes = totalSeconds // 60
            seconds = totalSeconds % 60
            return f"{minutes:02d}:{seconds:02d}"

        print(f"Total duration: {formatDuration(self.totalSeconds)}")

    def displayPlaylist(self):
        formattedPlaylist = ""
        for song in self.songs:
            formattedPlaylist += f"{song.artist} - {song.title} ({song.duration})\n"
        
        print(f"Playlist: {self.name}\n")
        print(formattedPlaylist)


song1 = Song("Bohemian Rhapsody", "Queen", "05:01")
song2 = Song("Hey Jude", "The Beatles", "04:12")
song3 = Song("Light My Fire", "The Doors", "15:12")

playlist1 = Playlist("My Favorites")

playlist1.addSong(song1)
playlist1.addSong(song2)
playlist1.addSong(song3)

playlist1.removeSong("Hey Jude")


playlist1.displayPlaylist()
playlist1.totalDuration()