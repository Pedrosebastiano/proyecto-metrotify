#IMPORTACION DE LIBRERIAS
from datetime import datetime
import uuid
import re
import time
import webbrowser
#IMPORTACION DE CLASES
from objetos.album import Album
from objetos.playlist import Playlist
from objetos.song import Song
from objetos.like import Like


#FUNCIONES MODULO GESTION DE PERFIL

def give_like(self, id_item, name_item):
    """Funcion que crea objetos like y los agrega a la lista de likes. Si el like ya existe, no realiza la
    creacion de objetos.
    No retorna. Crea y anade objetos a el db_likes"""
    like_given = True
    for like in self.db_users[-1].items_liked:
        if like.id_item_liked == id_item:
            print(f'\n             Ya lo habia likeado❤️✅\n')
            like_given= False
    if like_given:
        print(f'\n             ❤️ Le ha dado like a {name_item}❤️\n')
        new_like = Like(self.db_users[-1].id, id_item, name_item)
        self.db_likes.append(new_like)
        self.db_users[-1].items_liked.append(new_like)
        return True
        
            
def remove_like(self, id_item, name_item):
    """Funcion que elimina los objetos like de la lista de likes. Si el like no existe, no elimina nada
    No retorna. Elimina objetos like del db_likes"""
    like_given = True
    for like in self.db_users[-1].items_liked:
        if like.id_item_liked == id_item:
            self.db_users[-1].items_liked.remove(like)
            self.db_likes.remove(like)
            print(f'\n             💔 Le ha quitado su like a {name_item}💔\n')
            like_given = False
            return True
    if like_given:
        print(f'\n             Like inexistente❌💔\n')


def new_album(self):
    """Funcion que permite crear un nuevo album, y nuevas canciones solicitando todos los datos necesarios
    No retorna, pero añade el álbum y sus canciones a las bases de datos correspondientes de la clase."""
    print('\n       🎵 REGISTRO DE NUEVO ÁLBUM\n')
    while True:
        try:
            #TOMA DE DATOS DEL USUARIO
            name = input('             Ingrese el nombre del álbum: ').lower()
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in name)):
                raise ValueError('El nombre debe contener solo letras y espacios.')
            description = input('             Ingrese la descripción del álbum: ')
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in description)):
                raise ValueError('La descripción debe contener solo letras y espacios.')
            cover_link = input('             Ingrese el link de la portada del álbum: ')
            if not(cover_link.startswith('https://')):
                raise ValueError('El link de la portada debe comenzar con https://')
            genre = input('             Ingrese el género predominante del álbum: ').title()
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in genre)):
                raise ValueError('El género debe contener solo letras y espacios.')
            #GENERADOR DE FECHA
            published = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            #GENERADOR DE ID NUEVA
            id_generado = str(uuid.uuid4())
            break
        except ValueError as e:
            print(f'\n             {e}❌\n')
        except Exception:
            print(f'\n              Ingreso invalido!!!❌\n')

    while True:
        try:
            #CREAR CANCIONES
            print('\n       💿 CARGA DE CANCIONES\n')
            tracklist = []
            num_canciones = int(input('             Ingrese el número de canciones del álbum: '))
            if "-" in str(num_canciones):
                raise Exception
            break
        except:
            print(f'\n              Ingreso invalido!!!❌\n')
  
    patron = re.compile(r'^[0-5]?\d:[0-5]\d$')
    i = 1
    while num_canciones > 0:
        try:
            print(f'\n            🎼 CANCION {i}')
            song_name = input('             Ingrese el nombre de la cancion: ').lower()
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in song_name)):
                raise ValueError('El nombre de la cancion debe contener solo letras y espacios.')
            duration = input('             Ingrese el de duracion de la cancion en formato MM:SS: ')
            if not(patron.match(duration)):
                raise ValueError('La duracion debe de tener formato MM:SS.')
            song_link = input('             Ingrese el link de la cancion (https://soundcloud.com/): ')
            if not(song_link.startswith("https://soundcloud.com/")):
                raise ValueError('El link debe de comenzar por https://soundcloud.com/')
            id_cancion = str(uuid.uuid4())
            tracklist.append(Song(id_cancion, song_name, duration, song_link, 0, 0))
            num_canciones -= 1
            i += 1
            self.db_songs.append(tracklist[-1])
        except ValueError as e:
            print(f'\n             {e}❌\n')
        except Exception:
            print(f'\n              Ingreso invalido!!!❌\n')
            
        

    album_completed = Album(id_generado, name, description, cover_link, published, genre, self.db_musicians[-1].id, 0, 0)
    album_completed.tracklist = tracklist
    self.db_albums.append(album_completed)
    print('\n             Album creado exitosamente✅')
    self.db_musicians[-1].albums.append(album_completed)


def new_playlist(self):
    """Funcion que permite crear una nueva playlist solicitando todos los datos necesarios
    No retorna, pero añade la playlist a las bases de datos correspondientes de la clase."""
    print('\n       😜 REGISTRO DE NUEVA PLAYLIST\n')
    while True:
        try:
            #TOMA DE DATOS DEL USUARIO
            title = input('             Ingrese el titulo de la playlist: ').lower()
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in title)):
                raise ValueError('El titulo debe contener solo letras y espacios.')
            description = input('             Ingrese la descripción de la playlist: ')
            if not(all(palabra.isalpha() or palabra.isspace() for palabra in description)):
                raise ValueError('La descripción debe contener solo letras y espacios.')
            #GENERADOR DE ID NUEVA
            id_generado = str(uuid.uuid4())
            id_creator = self.db_listeners[-1].id
            break
        except ValueError as e:
            print(f'\n             {e}❌\n')
        except Exception:
            print(f'\n              Ingreso invalido!!!❌\n')


    tracklist = []
    while True:
        try:
            option = input('''
                Ingrese el número correspondiente a la accion que desee realizar🎧:
                    1. Buscar por nombre del músico
                    2. Buscar por nombre de la canción
                    3. Terminar playlist
                    >>> ''')
            if option == '3' and len(tracklist)> 0:
                break
            elif option == '3' and len(tracklist)==0:
                raise ValueError('La playlist esta vacia, asegurese de ingresar canciones')
            elif option == '1':
                cancion = searh_byname(self, False)
                if cancion == None:
                    continue
                tracklist.append(cancion)
            elif option == '2':
                cancion = search_song(self, self.db_songs, False)
                if cancion == None:
                    continue
                tracklist.append(cancion)
            else:
                raise Exception
        except ValueError as e:
            print(f'\n             {e}❌\n')
        except Exception:
            print(f'\n              Ingreso invalido!!!❌\n')

    playlist_completed = Playlist(id_generado, title, description, id_creator, 0)
    playlist_completed.tracklist = tracklist
    self.db_playlists.append(playlist_completed)
    print('\n             Playlist creada exitosamente✅')
    self.db_listeners[-1].playlist.append(playlist_completed)
        
            
def searcher(self):
    """Funcion que permite seleccionar el tipo de busqueda que se desea realizar
    No retorna, llama a otras funciones segun la busqueda a realizar."""
    while True:
        option = input('''
                Ingrese el número correspondiente a la accion que desee realizar🎧:
                    1. Buscar por nombre del músico
                    2. Buscar por nombre del álbum
                    3. Buscar por nombre de la canción
                    4. Buscar por nombre del playlist
                    5. Volver
                    >>> ''')

        if option == '1':
            searh_byname(self, True)
        elif option == '2':
            search_byalbum(self)
        elif option == '3':
            search_song(self, self.db_songs, True)
        elif option == '4':
            search_byplaylist(self)
        elif option == '5':
            break
        else:
            print("\n           Ingreso invalido!!!❌")

    
def search_song(self, list, listen):
    """Funcion que permite buscar el nombre de una cancion y darle/remover like a la misma. Dependiendo del valor del  
    atributo listen puede o reproducir las canciones y aumentar el numero de streams, o buscar la cancion para 
    ser agregada a una playlist. Recibe lista de objetos de canciones donde buscara la cancion deseada
    Retorna el objeto cancion en caso de que se quiera buscar el nombre de la cancion, en caso contrario, 
    reproducira la cancion."""
    while True:
        try:
            search = input("                🎵🔎Indique el nombre de la cancion: ").lower()
            val_search = ""
            for caracter in search:
                if not(caracter == " "):
                    val_search += caracter
            if not(val_search.isalpha() or "-" in val_search):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌(No se permiten numeros o caracteres especiales)\n')
    
    not_founded = True
    for song in list:
        if song.name == search:
            song_save = song
            not_founded = False
            break
    if listen:
        if not_founded:
            print(f'\n              💡 CANCION {search} NO ENCONTRADO\n')
        else:
            print(f'\n                 🎶Escuchando {song.name}...🎶')
            time.sleep(5)
            for musician in self.db_musicians:
                for album in musician.albums:
                    for cancion in album.tracklist:
                        if cancion.name == search:
                            if self.db_users[-1].type == "listener":
                                self.db_users[-1].streams += 1
                            cancion.streams += 1
                            album.streams += 1
                            musician.streams += 1
                            song_object = cancion
                            webbrowser.open(cancion.link)
                            break
            while True:
                action = input("""                  Seleccione la accion que desea realizar
                               1. Escuchar mas canciones
                               2. Dar like a la cancion
                               3. Remover like a la cancion
                               4. Volver
                               >>>""")
                if action == "1":
                    search_song(self, list, listen)
                elif action == "2":
                    new_like = give_like(self, song_object.id, song_object.name)
                    if new_like: 
                        song_object.likes += 1
                elif action == "3":
                    delete_like = remove_like(self, song_object.id, song_object.name)
                    if delete_like:
                        song_object.likes -=1
                elif action == "4":
                    break
                else:
                    print('\n               Ingreso invalido!!!❌\n')
                break
    else:
        if not_founded:
            print(f'\n        💡 CANCION {search} NO ENCONTRADO\n')
        else:
            print(f'\n        ✅ CANCION {search} AGREGADA EXITOSAMENTE\n')
            return song_save
            

def search_byalbum(self):
    """Funcion que permite realizar la busqueda de un album y darle/remover like, para luego llamar a la funcion 
    que permita buscar a la cancion
    No retorna, valida que el album exista y pasa lista de canciones del album a la funcion search_song."""
    while True:
        try:
            search = input("                🎵🔎Indique el nombre del album que desea escuchar: ").lower()
            val_search = ""
            for caracter in search:
                if not(caracter == " "):
                    val_search += caracter
            if not(val_search.isalpha()):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌(No se permiten numeros o caracteres especiales)\n')
    not_founded = True
    for album in self.db_albums:
        if album.name.lower() == search:
            print(f'\n       ✅ ALBUM ENCONTRADO✅\n')
            not_founded = False
            while True: 
                action = input("""                  Seleccione la accion que desea realizar
                               1. Ver canciones del album
                               2. Dar like al album
                               3. Remover like al album
                               4. Volver
                               >>>""")
                if action == "1":
                    album.show_songs()
                    search_song(self, album.tracklist, True)
                    break
                elif action == "2":
                    new_like = give_like(self, album.id, album.name)
                    if new_like:
                        album.likes +=1
                elif action == "3":
                    delete_like = remove_like(self, album.id, album.name)
                    if delete_like:
                        album.likes -=1
                elif action == "4":
                    break
                else:
                    print('\n             Ingreso invalido!!!❌\n')
            break        
    if not_founded:
        print(f'\n        💡 ALBUM {search} NO ENCONTRADO\n')


def search_byplaylist(self):
    """Funcion que permite realizar la busqueda de una playlist y darle/remver like, para luego llamar a la funcion
    que permita buscar a la cancion
    No retorna, valida que la playlist exista y pasa lista de canciones de la playlist a la funcion search_song."""
    while True:
        try:
            search = input("                🎵🔎Indique el nombre de la playlist que desea escuchar: ").lower()
            val_search = ""
            for caracter in search:
                if not(caracter == " "):
                    val_search += caracter
            if not(val_search.isalpha()):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌(No se permiten numeros o caracteres especiales)\n')
    not_founded = True
    for playlist in self.db_playlists:
        if playlist.name.lower() == search:
            print(f'\n       ✅ PLAYLIST ENCONTRADO✅\n')
            not_founded = False
            while True:
                action = input("""                  Seleccione la accion que desea realizar
                               1. Ver canciones de la playlist
                               2. Dar like a la playlist
                               3. Remover like a la playlist
                               4. Volver
                               >>>""")
                if action == "1":
                    playlist.show_songs()
                    search_song(self, playlist.tracklist, True)
                elif action == "2":
                    new_like = give_like(self, playlist.id, playlist.name)
                    if new_like: 
                        playlist.likes += 1
                elif action == "3":
                    delete_like = remove_like(self, playlist.id, playlist.name)
                    if delete_like:
                        playlist.likes -=1
                elif action == "4":
                    break
                else:
                    print('\n             Ingreso invalido!!!❌\n')
            break
            
            break
    if not_founded:
        print(f'\n        💡 ALBUM {search} NO ENCONTRADO\n')


def searh_byname(self, listen):
    """Funcion que permite realizar la busqueda de un musico y poder darle/remover like, para luego mostrar las 
    carcateristicas de los albums del musico y finalmente llamar a la funcion search_song para buscar el nombre de 
    la cancion. Ademas, recibe un parametro booleano "listen" que permite identificar si el usuario esta escuchando 
    o se desea anadir una cancion a una playlist
    Retorna el llamado de la funcion search_song en caso de que se quiera anadir una cancion a la playlist, 
    en caso contrario, no retorna."""
    while True:
        try:
            search = input("                Ingrese el nombre de la persona la cual desea buscar🧑🔎: ").title()
            val_search = ""
            for caracter in search:
                if not(caracter == " "):
                    val_search += caracter
            if not(val_search.isalpha()):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌(No se permiten numeros o caracteres especiales)\n')
    not_founded = True
    for user in self.db_musicians:
        if user.name.title() == search:
            print(f'\n       ✅ USUARIO ENCONTRADO✅\n')
            not_founded = False
            while True:
                if listen:
                    action = input("""                  Seleccione la accion que desea realizar
                                   1. Ver albums del musico
                                   2. Dar like al perfil
                                   3. Remover like al perfil
                                   4. Volver
                                   >>>""")
                else:
                    action = "1"
                if action == "1":
                    user.show_album()
                    while True:
                        try:
                            album = int(input("                Ingrese el numero album que desee buscar🔎: "))
                            if album > len(user.albums):
                                raise Exception
                            break
                        except:
                            print('\n             Ingreso invalido!!!❌\n')
                    print('\n       🎺CANCIONES:\n')
                    user.albums[album-1].show_songs()
                    if listen:
                        search_song(self, user.albums[album-1].tracklist, listen)
                    else:
                        return search_song(self, user.albums[album-1].tracklist, listen)
                    break
                elif action == "2":
                    new_like = give_like(self, user.id, user.name)
                    if new_like: 
                        user.likes += 1
                elif action == "3":
                    delete_like = remove_like(self, user.id, user.name)
                    if delete_like:
                        user.likes -=1
                elif action == "4":
                    break
                else:
                    print('\n             Ingreso invalido!!!❌\n')
            break

    if not_founded:
        print(f'\n        💡 USUARIO {search} NO ENCONTRADO\n')


