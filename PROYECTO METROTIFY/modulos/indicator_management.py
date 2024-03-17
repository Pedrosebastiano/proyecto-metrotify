#IMPORTACION DE LIBRERIAS
import matplotlib.pyplot as plt
import time


def show_top(list, option):
    """Funcion que permite hacer el TOP5 de una musico, album, canciones y escuchas
    No retorna. Imprime los resultados de la busqueda y llama a la funcion para graficar el top 5"""
    elementos = list[:]
    
    for i in range(len(elementos)):
        for j in range(i + 1, len(elementos)):
            if elementos[i].streams < elementos[j].streams:
                elementos[i], elementos[j] = elementos[j], elementos[i]

    top_5 = elementos[:5]

    emojis = ["🥇", "🥈", "🥉", "🏅", "🏅"]
    if top_5[4].streams == 0:
        print('\n           No hay suficientes datos para hacer un top😭\n')
    else:
        if option == "1":
            print('\n           🎖️🎹 TOP 5 MUSICOS CON MAS STREAMS 🎹🎖️\n')
            print(f'                    🎸 MUSICO 🎸                            🎧 STREAMS 🎧\n')
            title = "MUSICOS"
        elif option == "2":
            print('\n           🎖️📔 TOP 5 ALBUMS CON MAS STREAMS 📔🎖️\n')
            print(f'                    🎵 ALBUMS 🎵                            🎧 STREAMS 🎧\n')
            title = "ALBUMS"
        elif option == "3":
            print('\n           🎖️💿 TOP 5 CANCIONES CON MAS STREAMS 💿🎖️\n')
            print(f'                    🎼 CANCIONES 🎼                          🎧 STREAMS 🎧\n')
            title = "CANCIONES"
        elif option == "4":
            print('\n           🎖️🎧 TOP 5 ESCUCHAS CON MAS STREAMS 🎧🎖️\n')
            print(f'                    😜 ESCUCHA 😜                          🎧 STREAMS 🎧\n')
            title = "ESCUCHAS"
        items_names = []
        items_streams = []
        for object, i in zip(top_5, emojis):
            spaces = (42 - len(object.name))*" "
            print(f"                    {i}. {object.name}{spaces}{object.streams}")
            items_names.append(object.name)
            items_streams.append(object.streams)
        time.sleep(5)
        graphic_stadistics(items_names, items_streams, title)



def graphic_stadistics(names, streams, title):
    """Funcion que permite graficar el top 5 a traves de la libreria matplotlib
    No retorna. Grafica los items segun los streams"""
    plt.figure(figsize=(10, 6))  
    plt.bar(names, streams, color='orange')  
    plt.xlabel(title)  
    plt.ylabel('Streams') 
    plt.title(f'Top 5 de {title} Más Escuchadas') 
    plt.xticks(rotation=45) 
    plt.show() 



    
