from silabeador import silabeador

def divir_en_silabas(palabra:str) -> list[str]:
    pass

def acentuacion_palabra(palabra_en_silabas:list[str]) -> int:
    vocales_acentuadas = set(['á','é','í','ó','ú'])
    if len(palabra_en_silabas) == 1:
        return 1 #monosílaba
    if len(palabra_en_silabas) >= 3:
        antepenultima_silaba = palabra_en_silabas[-3]
        if antepenultima_silaba[-1] in vocales_acentuadas:
            return 4 #esdrújula
    penultima_silaba = palabra_en_silabas[-2]
    ultima_silaba = palabra_en_silabas[-1]
    if penultima_silaba[-1] in vocales_acentuadas or penultima_silaba[-2] in vocales_acentuadas:
        return 3 #grave
    if ultima_silaba[-1] in vocales_acentuadas or ultima_silaba[-2] in vocales_acentuadas:
        return 2
        
sil = silabeador.syllabify("orillas")
print(sil)