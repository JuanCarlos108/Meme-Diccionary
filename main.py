import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'XD': 'Se usa cuando se quiere referir de manera sarcastica a algo',
            'POV': 'Se usa para refrerir a un punto de vista',
            'When': 'Se refiere para una situacion que no se quiera usar el cuando',
            'But': 'Se usa para referir un pero en una oracion o meme',
            'Skibidi': 'Se referiere a una serie de animacion de Skibidi Toilet, no tiene un significado en si, puede variar',
            'Lmao': 'Se usa como risa, tiene variantes como Lmfao',
            'Eso Tilin': 'Aveces se refiere a animos a alguien, otra veces como burla, viene del video de el Dios Tilin bailando mientras alguien lo anima diciendo dicha frase'
            }
print(meme_dict.keys())
word = input("Escribe una palabra que no entiendas o Sorprendeme : ").upper()
if word in meme_dict.keys():
    print('El significado es:', meme_dict[word])
elif word == 'Sorprendeme':
    wordr = r.choice(list(meme_dict.keys()))
    print('La palabra es:', wordr, ' y el significado es:', meme_dict[wordr])
else:
    print('Esa palabra no esta en el diccionario')
