import Palabra as P
import re

class Verso:
    def __init__(self,contenido) -> None:
        self.contenido:list[P.Palabra] = contenido 
        self.calcular_silabas()
    
    def __str__(self) -> str:
        sb = ''
        for palabra in self.contenido:
            sb = sb + str(palabra.silabas) + " "
        sb = sb + str(self.silabas_fohologicas) + "-" + str(self.silabas_metricas)
        return sb
    
    def calcular_silabas(self):
        self.silabas_fohologicas = 0
        #busqueda de sinalefas
        sinalefas = 0
        for idx in range(len(self.contenido)-1):
            if self.contenido[idx].palabra[-1] in P.VOCALES+'yY' and self.contenido[idx+1].palabra[0] in P.VOCALES+'yYhH':
                if len(self.contenido[idx+1].palabra) != 1 and self.contenido[idx+1].palabra[0] in 'yY':
                    continue
                sinalefas += 1

        for palabra in self.contenido:
            self.silabas_fohologicas += palabra.numero_silabas


        self.silabas_metricas = self.silabas_fohologicas - sinalefas
        if self.contenido[-1].silaba_tonica == P.OXITONA or self.contenido[-1].silaba_tonica == P.MONOSILABA:
            self.tipo = P.OXITONA
            self.silabas_metricas = self.silabas_metricas + 1
        if self.contenido[-1].silaba_tonica == P.PROPARAXITONA:
            self.tipo = P.PROPARAXITONA
            self.silabas_metricas = self.silabas_metricas - 1
        if self.contenido[-1].silaba_tonica == P.SUPERPROPARAXITONA:
            self.tipo = P.SUPERPROPARAXITONA
            self.silabas_metricas = self.silabas_metricas - 2


class AnalizadorPoema:
    def __init__(self,poema:list[str]) -> None:
        self.poema = poema
        self.versos:list[Verso] = []
        self.rimas = []

    def analizar(self):
        self.limpiar_poema()
        for verso in self.versos:
            print(verso)
        self.buscar_rimas()
        
    def buscar_rimas(self):
        for idx in range(len(self.versos)-2):
            #print(self.versos[idx].contenido[-1].rima_asonante())
            pass

    
    def limpiar_poema(self):
        for verso in self.poema:
            texto_normalizado = re.sub(r'[^a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]', ' ', verso)
            texto_normalizado = re.sub(r'\s+', ' ', texto_normalizado) #remplazo de espacios multiples
            _ = texto_normalizado.strip()
            palabras_en_verso = []
            for palabra in _.split():   
                p = P.Palabra(palabra)
                palabras_en_verso.append(p)
            self.versos.append(Verso(palabras_en_verso))


texto = open("poema3.txt",mode="r",encoding="utf-8").readlines()
analizador = AnalizadorPoema(texto)
analizador.analizar()