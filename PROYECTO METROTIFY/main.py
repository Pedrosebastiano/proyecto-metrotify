#IMPORTACION DE MODULOS
from modulos.info_management import get_apidata, read_files, save_data
from modulos.profile_management import log_in, new_user, user_byname, change_info, delete_account
from modulos.music_interc_managment import searcher, new_album, new_playlist
from modulos.indicator_management import show_top

# DEFINICION DE LA CLASE APP 
class App:  
    def __init__(self):
        self.db_users = []
        self.db_musicians = []
        self.db_listeners = []

        self.db_likes = []
        self.db_albums = []
        self.db_playlists = []
        self.db_songs = []

    def start_app(self):
        """Funcion principal del sistema, contiene menus 
        con las acciones a realizar y el llamado de otras funciones
        No retorna.
        """
        #GUARDADO DE DATOS EN LISTAS CON OBJETOS
        self.db_users, self.db_musicians, self.db_listeners, self.db_albums, self.db_playlists, self.db_songs, self.db_likes = read_files()
        print('---------------------------------------------------------------')
        print('\n       🎧🎵BIENVENIDO A METROTIFY🎵🎧')
        while True:
            option = input('''\n            INICIO USUARIO🥁
            Ingrese el numero correspondiente a la accion que desea realizar:

                1. Iniciar sesion con cuenta ya existente
                2. Registrar nuevo usuario

            >>> ''')
            if option == "1": #INICIAR SESION
                log_in(self, self.db_users)
                break
            elif option == "2": #CREAR NUEVO USUARIO
                new_user(self)
                break
            else: #VALIDACION
                print('\n           Ingreso invalido!!!❌')
                print('\n           Debe registrarse o iniciar sesion primero👍') 
        while True:
            option = input('''\n            MENU PRINCIPAL🥁
            Ingrese el numero correspondiente a la accion que desea realizar:

            1. Descargar informacion de la API (Toma en cuenta que eleminarás los datos guardados)
            2. Acceder al modulo de Gestion de perfil
            3. Acceder al modulo de Gestion musical e interacciones
            4. Acceder al modulo de Estadisticas
            5. Cerrar app

            >>> ''')

            if option == "1": #DESCARGAR API
                get_apidata()
                self.db_users, self.db_musicians, self.db_listeners, self.db_albums, self.db_playlists, self.db_songs, self.db_likes = read_files()
            elif option == "2": #FUNCIONES DE GESTION DE PERFIL
                while True:

                    print('\n           🎧🧔 MODULO DE GESTION DE PERFIL 👩🎧')
                
                    option = input('''
                    Ingrese el numero correspondiente a la accion que desea realizar:

                    1. Buscar perfil por nombre
                    2. Cambiar informacion personal
                    3. Borrar datos de la cuenta
                    4. Volver al menu principal

                    >>> ''')
                    if option == '1': #BUSCAR USUARIO POR NOMBRE
                        user_byname(self, self.db_users)
                    elif option == '2': #CAMBIAR INFORMACION PERSONAL
                        change_info(self, self.db_users)
                    elif option == '3': #BORRAR DATOS DE CUENTA
                        if delete_account(self):
                            save_data(self)
                            main()
                        '''SE LLAMA A SI MISMA PARA VOLVER A INICIAR EL PROGRAMA, YA QUE NO HAY UNA SESION GUARDADA'''
                    elif option == '4': #VOLVER AL MENU PRINCIPAL
                        break
                    else:
                        print('\n           Ingreso invalido!!!❌')
            elif option == "3": #FUNCIONES DE GESTION MUSICAL E INTERACCIONES
                print('\n            💿🎺MODULO DE GESTION DE MUSICAL E INTERACCIONES 🎹💿')
                while True: 
                    option = input('''
                Ingrese el numero correspondiente a la accion que desea realizar:
                1. Crear nuevo album/playlist
                2. Escuchar musica
                3. Volver al menu principal
                >>> ''')
                    if option == '1': #CREAR ALBUM O PLAYLIST
                        if self.db_users[-1].type == "musician": 
                            new_album(self)
                        elif self.db_users[-1].type == "listener":
                            new_playlist(self)
                    elif option == '2': #ESCUCHAR MUSICA Y DAR LIKES
                        searcher(self)
                    elif option == '3': #VOLVER AL MENU PRINCIPAL
                        break
                    else:
                        print('\n           Ingreso invalido!!!❌')
            elif option == "4": #FUNCIONES DE GESTION DE ESTADISTICAS
                while True:

                    print('\n           🔢🎸 MODULO DE GESTION DE ESTADISTICAS 🎸🔢')
                
                    option = input('''
                    Ingrese el numero correspondiente a la accion que desea realizar:

                    1. Ver TOP 5 de musicos con mayor cantidad de streams
                    2. Ver TOP 5 de albums con mayor cantidad de streams
                    3. Ver TOP 5 de canciones con mayor cantidad de streams
                    4. Ver TOP 5 de escuchas con mayor cantidad de streams
                    5. Volver al menu principal

                    >>> ''')
                    if option == '1': #MUESTRA EL TOP 5 DE MUSICOS
                        show_top(self.db_musicians, option)
                    elif option == '2': #MUESTRA EL TOP 5 DE ALBUMS
                        show_top(self.db_albums, option)
                    elif option == '3': #MUESTRA EL TOP 5 DE CANCIONES
                        show_top(self.db_songs, option)
                    elif option == '4':#MUESTRA EL TOP 5 DE ESCUCHAS
                        show_top(self.db_listeners, option)
                    elif option == '5': #VOLVER AL MENU PRINCIPAL
                        break
                    else:
                        print('\n           Ingreso invalido!!!❌')
            elif option == "5": #SALIDA DEL SISTEMA
                print('\n           Salida exitosa del sistema, hasta luego!👋')
                save_data(self) #SE REESCRIBEN LOS TXT PARA GUARDAR LOS DATOS TOMADOS DURANTE LA EJECUCION
                break
            else: #VALIDACION
                print('\n           Ingreso invalido!!!❌')
                print('\n           Seleccione una opcion del Menu(1-6)')


def main():
    app = App()
    app.start_app()

main()

    
