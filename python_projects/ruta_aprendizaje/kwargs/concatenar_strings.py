#
def concatenar(**palabras):
    concatenacion = ""
    for palabra in palabras:
        concatenacion += palabras[palabra]
    print(concatenacion)

concatenar(Artista = "Bad Bunny ", Cancion = "25/8 ", Album = "YHLQMDLG")
concatenar(Artista = "Feid ", Cancion = "Chimbita ", Album = "Bahia Ducati")