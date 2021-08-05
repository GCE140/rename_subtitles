import os

def get_elementos(texto):

    dir = input(f"\nIngrese la dirección de la carpeta de los {texto}: ")

    os.chdir(dir)
    print()
    contenido = os.listdir(os.getcwd())
    for cont in contenido:
        print(cont)

    extension = input(f"\nIngrese la extensión de los {texto} (ej: .mkv para videos o .srt para subtítulos): ").strip(" ")
    print()
    lista = []

    for i in range(len(contenido)):
        if contenido[i][-4:] == extension:
            lista.append(contenido[i])

    for elem in lista:
        print(elem)
    print()

    return lista, extension


def cambiar_subs(videos, subs, dir):

    for i in range(len(videos[0])):
        path_1 = dir + "\\" + subs[0][i]
        path_2 = dir + "\\" + str(videos[0][i][:-4]) + subs[1]
        print("\n" + path_1 + "\n-->\n" + path_2 + "\n")
        os.rename(path_1, path_2)

        
if __name__ == "__main__":
    videos = get_elementos("videos")
    subs = get_elementos("subtítulos")
    dir = os.getcwd()
    os.system('pause')
    cambiar_subs(videos, subs, dir)
    print()
    os.system('pause')
    print()
