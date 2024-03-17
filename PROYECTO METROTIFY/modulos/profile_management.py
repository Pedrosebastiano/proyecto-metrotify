#IMPORTACION LIBRERIAS
import uuid
#IMPORTACION DE CLASES
from objetos.user import Musician, Listener

#FUNCIONES MODULO GESTION DE PERFIL

def new_user(self):
    """Funcion que permite registrar nuevos usuarios en la app
        Crea objetos: Musician, Listener
        Genera db (musician, listener, user)
        Retorna la agregacion a la base de datos
        """
    #TOMA DE DATOS DEL USUARIO
    print('\n       👤REGISTRO DE NUEVO USUARIO\n')
    while True:
        try:
            name = input('             Ingrese su nombre o nombre artistico: ').title()
            if not(all(word.isalpha() or ' ' in word for word in name.split())):
                raise Exception
            email = input('             Ingrese su correo electronico: ')
            val_email = email.split('@')[0]
            if not(email.split('@')[1] == "unimet.edu.ve"):
                print('\n             Solo estan permitidos correos UNIMET (@unimet.edu.ve)✅')
            if not(val_email.isalnum() and email.split('@')[1] == "unimet.edu.ve"):
                raise Exception
            username = input('             Ingrese su username: ')
            if not(username.isalnum()):
                raise Exception
            user_type = int(input("""             Seleccione su tipo de usuario:
                        1. Musico
                        2. Escucha
                        >>>"""))
            if not(user_type == 1 or user_type == 2):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌\n')
        
    #GENERADOR DE ID NUEVA
    id_generado = str(uuid.uuid4())
    print('\n             Perfil creado exitosamente✅')
    if user_type == 1:
        return self.db_musicians.append(Musician(id_generado, name, email, username, 0, 0)), self.db_users.append(Musician(id_generado, name, email, username, 0, 0))
    elif user_type == 2:
        return self.db_listeners.append(Listener(id_generado, name, email, username, 0, 0)), self.db_users.append(Listener(id_generado, name, email, username, 0, 0))
    
def search_user():
    '''Funcion que permite buscar los usuarios por su nombre
        Retorna la busqueda realizada'''
    print('        Indique el nombre del usuario\n')
    while True:
        try:
            search = input("                🧑🔎: ").title()
            val_search = ""
            for caracter in search:
                if not(caracter == " "):
                    val_search += caracter
            if not(val_search.isalpha()):
                raise Exception
            break
        except:
            print('\n             Ingreso invalido!!!❌(No se permiten numeros o caracteres especiales)\n')
    return search    

def log_in(self, list):
    '''Funcion que permite comparar la busqueda con la lista de usuarios
        Agrega de ultimo a la base de datos el usuario'''
    search = search_user()
    not_founded = True
    for user in list:
        if user.name == search:
            print(f'\n        ✅ SESION INICIADA CORRECTAMENTE\n')
            user_found = user
            not_founded = False
            break
    if not_founded:
        print(f'\n        💡 USUARIO NO ENCONTRADO\n')
        log_in(self, list)
    else:
        if user.type == "musician":
            self.db_musicians.remove(user_found)
            self.db_musicians.append(user_found)
            self.db_users.remove(user_found)
            self.db_users.append(user_found)
        elif user.type == "listener":
            self.db_listeners.remove(user_found)
            self.db_listeners.append(user_found)
            self.db_users.remove(user_found)
            self.db_users.append(user_found)

def user_byname(self, list):
    """Funcion que permite comparar la busqueda con la lista de usuarios
        No retorna. Imprime los resultados de la busqueda
        """
    print('\n       🧍BUSQUEDA DE USUARIOS POR SU NOMBRE')
    search = search_user()
    not_founded = True
    for user in list:
        if user.name.title() == search:
            print(f'\n        💡 RESULTADOS DE LA BUSQUEDA:\n')
            print('---------------------------------------------------------------')
            print(user.show_attr())
            if user.type == "musician":
                print(f'\n        💿CANCIONES DE LOS ALBUMS:\n')
                user.show_albums_songs()
                print(f'\n        😜TOP 10 DE CANCIONES MAS ESCUCHADAS:\n')
                all_songs = []
                for album in user.albums:
                    all_songs.extend(album.tracklist)
                ordered_songs = sorted(all_songs, key=lambda song: song.streams, reverse=True)
                top_10 = ordered_songs[:10]
                for i, song in enumerate(top_10, start=1):
                    print(f"    🎼{i}. {song.name} - {song.streams} streams")
            if user.type == "listener":
                print(f'\n        📔LISTA DE PLAYLIST:\n')
                user.show_playlist()
                print(f'\n        ❤️ITEMS LIKEADOS:\n')
                like_things = False
                for like in self.db_likes:
                    if user.id == like.id_user:
                        print(f'💖{like.name_item}')
                        like_things = True
                if not(like_things):
                    print(f'        Este usuario no tiene items likeados💔\n')
            not_founded = False
    if not_founded:
        print(f'\n        💡 USUARIO NO ENCONTRADO\n')

def change_info(self, list):
    """Funcion que permite cambiar la informacion de un usuario
        No retorna. Cambia los datos del ultimo objeto en lista(Usuario que se registro o inicio sesion)
        """
    print(list[-1].show_personal_info())
    while True:
        try:    
            option = int(input('''                  Seleccione la opcion de la informacion a cambiar😜:
                            1. Nombre
                            2. Email
                            3. Username
                            >>>'''))
            if option == 1:
                name = input('             Ingrese su nombre o nombre artistico: ')
                if not(all(word.isalpha() or ' ' in word for word in name.split())):
                    raise Exception
                list[-1].name = name
                if list[-1].type == "musician":
                    self.db_musicians[-1].name = name
                else:
                    self.db_listeners[-1].name = name
            elif option == 2:
                email = input('             Ingrese su correo electronico: ')
                val_email = email.split('@')[0]
                if not(email.split('@')[1] == "unimet.edu.ve"):
                    print('\n             Solo estan permitidos correos UNIMET (@unimet.edu.ve)✅')
                if not(val_email.isalnum() and email.split('@')[1] == "unimet.edu.ve"):
                    raise Exception
                list[-1].email = email
                if list[-1].type == "musician":
                    self.db_musicians[-1].email = email
                else:
                    self.db_listeners[-1].email = email
            elif option == 3:
                username = input('             Ingrese su username: ')
                list[-1].username = username
                if list[-1].type == "musician":
                    self.db_musicians[-1].username = username
                else:
                    self.db_listeners[-1].username = username
            print('\n             Operacion exitosa!!!✅\n')
            break
        except:
            print('\n             Ingreso invalido!!!❌\n')

def delete_account(self):
    """Funcion que elimina la cuenta de el usuario con el que se inicio sesion o se registo, borrando tanto
    albums/playlist, canciones, likes y el perfil del user.
    No retorna. Remueve objetos de las listas"""
    while True:
        ask = input("""             ¿Esta seguro que desea continuar? (Se eliminaran todos los datos cargados en la cuenta)
                    1. Continuar
                    2. Salir
                    >>>""")
        if ask == "1":
            id_to_delete = self.db_users[-1].id 
            if self.db_users[-1].type == "musician":
                self.db_musicians.pop(-1)
                for album in self.db_albums:
                    if album.artist == id_to_delete:
                        id_album = album.id
                        self.db_albums.remove(album)
                        for song in self.db_songs:
                            if song.id == id_album:
                                self.db_albums.remove(song)
            elif self.db_users[-1].type == "listener":
                self.db_listeners.pop(-1)
                for playlist in self.db_playlist:
                    if playlist.creator == id_to_delete:
                        self.db_playlist.remove(playlist)
            self.db_users.pop(-1)
            for like in self.db_likes:
                if id_to_delete == like.id_user:
                    self.db_likes.remove(like)
            print('\n             Cuenta borrada exitosamente!⛔\n')
            return True
        elif ask == "2":
            return False
        else:
            print('\n             Ingreso invalido!!!❌\n')
        
            