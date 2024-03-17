class Song:
    def __init__(self, id, name, duration, link, streams, likes):
        self.id = id
        self.name = name
        self.duration = duration
        self.link = link
        self.streams = streams
        self.likes = likes
    
    def show_attr(self):
        return f'''Nombre: {self.name}
        Duración: {self.duration}
        '''