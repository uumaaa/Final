import Palabra as P
import re

SIGNOS_PUNTUACION = '[¡!¿?.,;:(){}\[\]"\'\«\»]'
class Verso:
    def __init__(self,contenido,signos_puntuacion:dict) -> None:
        self.contenido:list[P.Palabra] = contenido 
        self.signos_puntuacion = signos_puntuacion
        self.calcular_silabas()
    
    def __str__(self) -> str:
        sb = ''
        for palabra in self.contenido:
            sb = sb + str(palabra.silabas) + " "
        sb = sb + f'{self.silabas_fohologicas} - {self.silabas_metricas} - {self.signos_puntuacion}'
        return sb
    
    def calcular_silabas(self):
        self.silabas_fohologicas = 0
        #busqueda de sinalefas
        self.sinalefas = {}
        for idx in range(len(self.contenido)-1):
            if self.contenido[idx].palabra[-1] in P.VOCALES+'yY' and self.contenido[idx+1].palabra[0] in P.VOCALES+'yYhH':
                if len(self.contenido[idx+1].palabra) != 1 and self.contenido[idx+1].palabra[0] in 'yY': # sonido ll
                    continue
                if self.contenido[idx+1].silaba_tonica + len(self.contenido[idx+1].palabra) == 0 and len(self.contenido[idx+1].palabra) != 1: #segunda vocal tónica
                    continue
                if idx in self.signos_puntuacion: # signo que genera pausa
                    continue
                self.sinalefas[idx] = self.contenido[idx].silabas[-1] + self.contenido[idx+1].silabas[0]

        for palabra in self.contenido:
            self.silabas_fohologicas += palabra.numero_silabas


        self.silabas_metricas = self.silabas_fohologicas - len(self.sinalefas)
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
        self.versos = []
        for verso in self.poema:
            verso_normalizado = verso.replace('\n','')
            signos_puntuacion = {}
            palabras = []
            for idx,palabra in enumerate(verso_normalizado.split()):
                if palabra[-1] in SIGNOS_PUNTUACION:
                    signos_puntuacion[idx] = palabra[-1]
                palabras.append(P.Palabra(palabra))
            self.versos.append(Verso(palabras,signos_puntuacion))

texto = open("poema3.txt",mode="r",encoding="utf-8").readlines()
print(texto)
analizador = AnalizadorPoema(texto)
analizador.analizar()