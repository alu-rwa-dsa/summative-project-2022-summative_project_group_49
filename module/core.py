class Track:
    def __init__(self, artist: str, song: str, release: int):
        self.artist = artist
        self.song = song
        self.release = release

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Track):
            return self.artist == other.artist and self.song == other.song and self.release == other.release
        return False

    def __str__(self):
        return "Artist: {0}, Song: {1}, Release: {2}".format(self.artist, self.song, self.release)


class Node:
    #  initialising a new node with its attributes
    def __init__(self, data: Track):
        self.data: Track = data
        self.next: Node = None
        self.prev: Node = None
