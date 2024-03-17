class Album:
    def __init__(self, id, name, description, cover, published, genre, artist, streams, likes):
        self.id = id
        self.name = name
        self.description = description
        self.cover = cover
        self.published = published
        self.genre = genre
        self.artist = artist
        self.tracklist = []
        self.streams = streams
        self.likes = likes
    
    def show_info_album(self):
        return f"""Album:
        Nombre: {self.name}
        Género: {self.genre}"""
    
    def show_songs(self):
        for song in self.tracklist:
            print(f'💿 {song.show_attr()}')