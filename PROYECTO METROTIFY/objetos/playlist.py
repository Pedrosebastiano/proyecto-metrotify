class Playlist:
    def __init__(self, id, name, description, creator, likes):
        self.id = id
        self.name = name
        self.description = description
        self.creator = creator
        self.tracklist =[]
        self.likes = likes
    
    def show_info_playlist(self):
        return f"""Playlist:
        Nombre: {self.name}"""
    
    def show_songs(self):
        for song in self.tracklist:
            print(f'💿 {song.show_attr()}')