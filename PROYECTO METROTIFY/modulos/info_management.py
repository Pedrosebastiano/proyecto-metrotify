# IMPORTACIONES DE LIBRERIAS
import requests

#IMPORTACION DE CLASES
from objetos.user import Musician, Listener
from objetos.album import Album
from objetos.playlist import Playlist
from objetos.song import Song
from objetos.like import Like

# FUNCIONES MODULO MANEJO DE INFORMACION
        
def get_apidata():
    """Extrae informacion de la API y escribe .TXT
    No retorna
    """
    print("\nIniciando descarga de datos...📩")
    
    url_users = requests.request("GET", 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/users.json')
    url_albums = requests.request("GET", 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/albums.json')
    url_playlists = requests.request("GET", 'https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/playlists.json')
    
    directory = './archivos/'

    file_name = 'db_users'
    with open(directory + file_name, 'w') as file:
        for user in url_users.json():
            file.write(f'{user["id"]},{user["name"]},{user["email"]},{user["username"]},{user["type"]},{0},{0}*\n')

    file_name = 'db_albums'
    with open(directory + file_name, 'w') as file:
        for album in url_albums.json():
            if "\n" in album["description"]:
                description = album["description"].split("\n")[0] + album["description"].split("\n")[1]
            else:
                description = album["description"]
            file.write(f'{album["id"]},{album["name"]},{description},')
            file. write(f'{album["cover"]},{album["published"]},{album["genre"]},{album["artist"]},{0},{0}*\n')

    file_name = 'db_albums_songs'
    with open(directory + file_name, 'w') as file:
        for album in url_albums.json():
            for song in album["tracklist"]:
                file.write(f'{album["id"]},{song["id"]},{song["name"]},{song["duration"]},{song["link"]},{0},{0}*\n')

    file_name = 'db_playlist'
    with open(directory + file_name, 'w') as file:
        for playlist in url_playlists.json():
            if "\n" in playlist["description"]:
                description = playlist["description"].split("\n")[0] + playlist["description"].split("\n")[1]
            else:
                description = playlist["description"]
            file.write(f'{playlist["id"]},{playlist["name"]},{description},{playlist["creator"]},{0}*\n')

    file_name = 'db_playlist_songs'
    with open(directory + file_name, 'w') as file:
        for playlist in url_playlists.json():
            for song in playlist["tracks"]:
                file.write(f'{playlist["id"]},{song}* \n')

    file_name = 'db_likes'
    with open(directory + file_name, 'w') as file:
        file.write(f'')

        print('Informacion actualizada exitosamente! ✅')


def read_files():
        """Lee informacion de los archivos .TXT y crea los db
        Retorna listas con objetos(DB)
        """
        directory = './archivos/'
        
        #CREA LISTAS DE USUARIOS, ESCUCHAS Y MUSICOS
        db_users = []
        db_musicians = []
        db_listeners = []
        file_name = 'db_users'
        with open(directory + file_name) as file:
            for user in file:
                if "musician" in user:
                    musician = Musician(id = user.split(",")[0], name = user.split(",")[1], email = user.split(",")[2], username = user.split(",")[3], streams= int(user.split(",")[5]), likes = int(user.split(",")[6].split("*")[0]))
                    db_musicians.append(musician)
                    db_users.append(musician)
                    continue
                listener = Listener(id = user.split(",")[0], name = user.split(",")[1], email = user.split(",")[2], username = user.split(",")[3], streams= int(user.split(",")[5]), likes = int(user.split(",")[6].split("*")[0]))
                db_users.append(listener)
                db_listeners.append(listener)                
        
        #CREA LISTA DE ALBUMS
        db_albums = []
        file_name = 'db_albums'
        with open(directory + file_name) as file:
            for album in file:
                album = Album(id = album.split(",")[0], name = album.split(",")[1], description=album.split(",")[2], cover = album.split(",")[3], published=album.split(",")[4], genre=album.split(",")[5], artist=album.split(",")[6], streams= int(album.split(",")[7]), likes= int(album.split(",")[8].split("*")[0]))
                db_albums.append(album)
                for user in db_musicians:
                    if user.id == album.artist:
                        user.albums.append(album)

        #AGREGA LAS CANCIONES A CADA ALBUM
        db_songs = []
        file_name = 'db_albums_songs'
        with open(directory + file_name) as file:
            for tracklist in file:
                song = Song(id = tracklist.split(",")[1], name= tracklist.split(",")[2], duration= tracklist.split(",")[3], link= tracklist.split(",")[4], streams= int(tracklist.split(",")[5]), likes= int(tracklist.split(",")[6].split("*")[0]))
                db_songs.append(song)         
                for album in db_albums:
                    if album.id == tracklist.split(",")[0]:
                        album.tracklist.append(song)
                        break


        #CREA LISTA DE PLAYLIST
        db_playlist = []
        file_name = 'db_playlist'
        with open(directory + file_name) as file:
            for playlist in file:
                playlist = Playlist(id = playlist.split(",")[0], name = playlist.split(",")[1], description=playlist.split(",")[2], creator=playlist.split(",")[3], likes=int(playlist.split(",")[4].split("*")[0]))
                db_playlist.append(playlist)
                for user in db_listeners:
                    if user.id == playlist.creator:
                        user.playlist.append(playlist)

        #AGREGA LAS CANCIONES A LA PLAYLIST
        file_name = 'db_playlist_songs'
        with open(directory + file_name) as file:
            for playlist_song in file:
                for song in db_songs:
                    if playlist_song.split(",")[1].split("*")[0] == song.id:
                        song_add = song
                        for playlist in db_playlist:
                            if playlist.id == playlist_song.split(",")[0]:
                                playlist.tracklist.append(song_add)
                                break
                        break

        #CREA LISTA DE LIKES
        db_likes = []
        file_name = 'db_likes'
        with open(directory + file_name) as file:
            content = file.read()
            if not content:
                pass
            else:
                file.seek(0)
                for like in file:
                    new_like = Like(like.split(",")[0], like.split(",")[1], like.split(",")[2].split("*")[0])
                    db_likes.append(new_like)
                    for user in db_users:
                        if like.split(",")[0] == user.id:
                            user.items_liked.append(new_like)
                            break



        return db_users, db_musicians, db_listeners, db_albums, db_playlist, db_songs, db_likes


def save_data(self):
    """Funcion que toma las listas de objetos y reescribe los atributos en el txt al cerrar el programa
    si hay objetos nuevos, los escribe en este mismo
    No retorna. Escribe .txt"""
    directory = './archivos/'

    file_name = 'db_users'
    with open(directory + file_name, 'w') as file:
        for user in self.db_users:
            file.write(f'{user.id},{user.name},{user.email},{user.username},{user.type},{user.streams},{user.likes}*\n')

    file_name = 'db_albums'
    with open(directory + file_name, 'w') as file:
        for album in self.db_albums:
            file.write(f'{album.id},{album.name},{album.description},{album.cover},{album.published},{album.genre},{album.artist},{album.streams},{album.likes}*\n')

    file_name = 'db_albums_songs'
    with open(directory + file_name, 'w') as file:
        for album in self.db_albums:
            for song in album.tracklist:
                file.write(f'{album.id},{song.id},{song.name},{song.duration},{song.link},{song.streams},{song.likes}*\n')

    file_name = 'db_playlist'
    with open(directory + file_name, 'w') as file:
        for playlist in self.db_playlists:
            file.write(f'{playlist.id},{playlist.name},{playlist.description},{playlist.creator},{playlist.likes}*\n')

    file_name = 'db_playlist_songs'
    with open(directory + file_name, 'w') as file:
        for playlist in self.db_playlists:
            for song in playlist.tracklist:
                file.write(f'{playlist.id},{song.id}*\n')

    file_name = 'db_likes'
    with open(directory + file_name, 'w') as file:
        for like in self.db_likes:
            file.write(f'{like.id_user},{like.id_item_liked},{like.name_item}*\n')