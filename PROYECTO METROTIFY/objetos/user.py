class User:
    def __init__(self, id, name, email, username, likes):
        self.id = id
        self.name = name   
        self.email = email
        self.username = username
        self.likes = likes
        self.items_liked = []
    
    def show_attr(self):
        return f'''
        Nombre: {self.name}
        Email: {self.email}
        Username: {self.username}
        '''
    
class Musician(User):
    def __init__(self, id, name, email, username, likes, streams):
        super().__init__(id, name, email, username, likes)
        self.type = "musician"
        self.albums = []
        self.streams = streams
    
    def show_personal_info(self):
        return f'''{super().show_attr()}'''
    def show_album(self):
        i = 0
        for album in self.albums:
            i +=1
            print(f'{i}. {album.show_info_album()}')
    def show_albums_songs(self):
        i = 0
        for album in self.albums:
            i +=1
            print(f'📔{i}. {album.show_info_album()}')
            for song in album.tracklist:
                print(f'💿{song.show_attr()}')
    def show_attr(self):
        return f'''
        Nombre: {self.name}
        Tipo : {self.type}
        Streams: {self.streams}'''
    
    
class Listener(User):
    def __init__(self, id, name, email, username, streams, likes):
        super().__init__(id, name, email, username, likes)
        self.type = "listener"   
        self.playlist = []
        self.streams = streams
    
    def show_personal_info(self):
        return f'''{super().show_attr()}'''
    def show_attr(self):
        return f'''Nombre: {self.name}
        Tipo : {self.type}'''
    def show_playlist(self):
        i = 0
        for playlist in self.playlist:
            i +=1
            print(f'🎶{i}. {playlist.show_info_playlist()}')