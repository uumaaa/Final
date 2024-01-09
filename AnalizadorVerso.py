import re
import copy 
# constantes
# salidas
OXITONA = -1 # agudo
PARAXITONA = -2 # grave o llano
PROPARAXITONA = -3 # esdrújulo
SUPERPROPARAXITONA = -4 # sobresdrújulo
MONOSILABA = -1
# diccionarios 
VOCALES = 'aeiouáéíóúAEIOUÁÉÍÓÚ'
VOCALES_ACENTUADAS = 'áéíóúÁÉÍÓÚ'
VOCALES_BAJAS = 'aáAÁ'
VOCALES_MEDIAS = 'eéEÉoóOÓ'
VOCALES_ALTAS = 'iIuU'
VOCALES_ALTAS_ACENTUADAS = 'íÍúÚ'
CONSONANTES = 'BCDFGHJKLMNÑPQRSTVWXYZbcdfghjklmnñpqrstvwxyz'
CONSONANTES_BILABIALES = 'PBpb'
CONSONTANTES_LABIODENTALES = 'Ff'
CONSONANTES_LINGUOVERALES = 'cGCg'
CONSONANTES_LINGUODENTALES = 'DTdt'
CONSONANTES_INSEPARABLES = CONSONANTES_BILABIALES + CONSONANTES_LINGUOVERALES +\
                            CONSONTANTES_LABIODENTALES + CONSONANTES_LINGUODENTALES 
CONSONANTES_SEPARABLES =  ''.join([_ for _ in CONSONANTES if _ not in CONSONANTES_INSEPARABLES])
CONSONANTES_LIQUIDAS = 'LRlr'
CONSONANTES_NO_LUQUIDAS = ''.join([_ for _ in CONSONANTES if _ not in CONSONANTES_LIQUIDAS])
SIGNOS_PUNTUACION = '[¡!¿?.,;:(){}\[\]"\'\«\»]'

class Palabra :
    def __init__(self,palabra:str) -> None:
        self.palabra = palabra
        self.dict_silabas = {}
        self.silabas = []
        self.numero_silabas = None
        self.silaba_tonica = None
        self.silabalizar()
    
    def normalizar_pabra(self):
        self.palabra = ''.join([caracter for caracter in self.palabra if caracter in CONSONANTES+VOCALES])

    def silabalizar(self):
        self.normalizar_pabra()
        self.dividir_patrones()
        self.eliminar_duplicados()
        self.completar_silabas()
        self.encontrar_silaba_tonica()
        
    def encontrar_silaba_tonica(self):
        self.numero_silabas = len(self.silabas)
        if self.numero_silabas == 1:
            self.silaba_tonica = MONOSILABA
            return
        for idx in range(self.numero_silabas):
            for caracter in self.silabas[idx]:
                if caracter in VOCALES_ACENTUADAS:
                    self.silaba_tonica = -len(self.silabas) + idx
                    return
        if self.silabas[-1][-1] in VOCALES + 'nNsS':
            self.silaba_tonica = PARAXITONA
        else:
            self.silaba_tonica = OXITONA

    def rima_consonante(self) -> str:
        ultima_silaba_tonica = self.silabas[self.silaba_tonica]
        idx_ultima_vocal = 0
        for idx_caracter in range(len(ultima_silaba_tonica)):
            if ultima_silaba_tonica[idx_caracter] in VOCALES:
                idx_ultima_vocal = idx_caracter
        sb = ''
        for idx,silaba in enumerate(self.silabas[self.silaba_tonica:]):
            if idx == 0:
                sb += silaba[idx_ultima_vocal:]
            else:
                sb += silaba
        return sb

    def rima_asonante(self) -> str:
        ultima_silaba_tonica = self.silabas[self.silaba_tonica]
        idx_ultima_vocal = 0
        for idx_caracter in range(len(ultima_silaba_tonica)):
            if ultima_silaba_tonica[idx_caracter] in VOCALES:
                idx_ultima_vocal = idx_caracter
        sb = ''
        for idx,silaba in enumerate(self.silabas[self.silaba_tonica:]):
            if idx == 0:
                sb += silaba[idx_ultima_vocal:]
            else:
                sb += silaba
        return ''.join(_ for _ in sb if _ in VOCALES)



    def completar_silabas(self) -> None:
        silabas_nuevas = []
        if len(self.silabas) == 1:
            silabas_nuevas = copy.copy(self.silabas)
        else:
            ultima = True
            anterior = False
            for idx in range(len(self.silabas)): #busqueda de diptongos
                ultima = False
                if(anterior): anterior = False; ultima = True; continue;
                anterior = False;
                if idx >= 1:
                    if \
                    (self.silabas[idx][0] in VOCALES_ALTAS and (self.silabas[idx-1][-1] in VOCALES_MEDIAS 
                    or self.silabas[idx-1][-1] in VOCALES_BAJAS)) or (self.silabas[idx-1][-1] in VOCALES_ALTAS and (self.silabas[idx][0] in VOCALES_MEDIAS 
                    or self.silabas[idx][0] in VOCALES_BAJAS)): #diptongo creciente
                        silabas_nuevas.append(self.silabas[idx-1] + self.silabas[idx])
                        anterior = True
                    elif self.silabas[idx][0] in VOCALES_ALTAS and self.silabas[idx-1][-1] in VOCALES_ALTAS: #diptongo homogeneo
                        silabas_nuevas.append(self.silabas[idx-1] + self.silabas[idx])
                        anterior = True
                    else:
                        silabas_nuevas.append(self.silabas[idx-1])
                        ultima = True
            if ultima:
                silabas_nuevas.append(self.silabas[-1])
        
        for idx in range(len(silabas_nuevas)): #separación de cc-nn
            if idx >= 1:
                if(len(silabas_nuevas[idx])<2):
                    break
                if silabas_nuevas[idx][0] in 'cCnN' and silabas_nuevas[idx][1] in 'cCnN':
                    silabas_nuevas[idx-1] = silabas_nuevas[idx-1] + silabas_nuevas[idx][0]
                    silabas_nuevas[idx] = silabas_nuevas[idx][1:]

        for idx in range(len(silabas_nuevas)): #busqueda de hiatos acentuales
            silaba_interna = silabas_nuevas[idx]
            for idx_caracter in range(len(silaba_interna)):
                if idx_caracter >= 1:
                    if (silaba_interna[idx_caracter] in VOCALES_BAJAS or silaba_interna[idx_caracter] in VOCALES_MEDIAS) \
                    and (silaba_interna[idx_caracter-1] in VOCALES_BAJAS or silaba_interna[idx_caracter-1] in VOCALES_MEDIAS):
                        silaba = silabas_nuevas.pop(idx)
                        silabas_nuevas.insert(idx,silaba[idx_caracter:])
                        silabas_nuevas.insert(idx,silaba[:idx_caracter])

        for idx in range(len(silabas_nuevas)): #busqueda de hiatos formales
            silaba_interna = silabas_nuevas[idx]
            for idx_caracter in range(len(silaba_interna)):
                if idx_caracter >= 1:
                    if (silaba_interna[idx_caracter] in VOCALES_ALTAS_ACENTUADAS and (silaba_interna[idx_caracter-1] \
                    in VOCALES_BAJAS or silaba_interna[idx_caracter-1] in VOCALES_MEDIAS)) or \
                    (silaba_interna[idx_caracter-1] in VOCALES_ALTAS_ACENTUADAS and (silaba_interna[idx_caracter] \
                    in VOCALES_BAJAS or silaba_interna[idx_caracter] in VOCALES_MEDIAS)):
                        silaba = silabas_nuevas.pop(idx)
                        silabas_nuevas.insert(idx,silaba[idx_caracter:])
                        silabas_nuevas.insert(idx,silaba[:idx_caracter])
            
        indices_eliminar = []
        for idx in range(len(silabas_nuevas)-1): # unión de ll rr 
                if silabas_nuevas[idx][-1] in 'lLrR' and silabas_nuevas[idx+1][0] in 'lLrR':
                    silabas_nuevas[idx+1] = silabas_nuevas[idx][-1] + silabas_nuevas[idx+1]
                    if len(silabas_nuevas[idx]) == 1:
                        indices_eliminar.append(idx)
                    else:
                        silabas_nuevas[idx] = silabas_nuevas[idx][:-1]


        for idx_el in range(len(indices_eliminar)):
            silabas_nuevas.pop(indices_eliminar[idx_el]-idx_el)
        indices_eliminar = []
        for idx in range(len(silabas_nuevas)): # unión de consonantes libres
            if idx >= 1:
                if len(silabas_nuevas[idx]) == 1 and silabas_nuevas[idx] in CONSONANTES and silabas_nuevas[idx-1][-1] in VOCALES: #union izq
                    silabas_nuevas[idx-1] = silabas_nuevas[idx-1] + silabas_nuevas[idx]
                    indices_eliminar.append(idx)
                if len(silabas_nuevas[idx]) == 2 and silabas_nuevas[idx][0] in CONSONANTES and silabas_nuevas[idx][1] in CONSONANTES and silabas_nuevas[idx-1][-1] in VOCALES: #union izq
                    silabas_nuevas[idx-1] = silabas_nuevas[idx-1] + silabas_nuevas[idx]
                    indices_eliminar.append(idx)
                if len(silabas_nuevas[idx-1]) == 2 and silabas_nuevas[idx-1][0] in CONSONANTES and silabas_nuevas[idx-1][1] in CONSONANTES and silabas_nuevas[idx][0] in VOCALES: #union der
                    silabas_nuevas[idx-1] = silabas_nuevas[idx-1] + silabas_nuevas[idx]
                    indices_eliminar.append(idx)
                if len(silabas_nuevas[idx-1]) == 1 and silabas_nuevas[idx-1] in CONSONANTES and silabas_nuevas[idx][0] in VOCALES: #union derecha
                    silabas_nuevas[idx] = silabas_nuevas[idx-1] + silabas_nuevas[idx]
                    indices_eliminar.append(idx-1)

        for idx_el in range(len(indices_eliminar)):
            silabas_nuevas.pop(indices_eliminar[idx_el]-idx_el)
        self.silabas = silabas_nuevas


    def eliminar_duplicados(self) -> None:
        indices_visitados = []
        indices_repetidos = {}
        self.dict_silabas = dict(sorted(self.dict_silabas.items()))
        for llave in self.dict_silabas:
            for idx in range(len(self.dict_silabas[llave])):
                if llave+idx in indices_visitados:
                    indices_repetidos[llave] = idx
                    indices_visitados.append(llave + idx)
                else:
                    indices_visitados.append(llave + idx)
        for indice_absoluto,indice_relativo in indices_repetidos.items():
            if len(self.dict_silabas[indice_absoluto]) == 1:
                self.dict_silabas.pop(indice_absoluto)
            else:
                self.dict_silabas[indice_absoluto+1] = self.dict_silabas[indice_absoluto][indice_relativo+1:]
                self.dict_silabas.pop(indice_absoluto)
        indice_inicial = 0
        palabra = ''
        for idx in range(len(self.palabra)):
            if idx not in indices_visitados:
                palabra += self.palabra[idx]
            else:
                if len(palabra) != 0:
                    self.dict_silabas[indice_inicial] = palabra
                    palabra = ''
                indice_inicial = idx+1
                
        if len(palabra) != 0:
            self.dict_silabas[indice_inicial] = palabra
        self.silabas = [_[1] for _ in sorted(self.dict_silabas.items())]

    def tipo_palabra(self) -> str:
        return 'monosílaba' if self.silabas.__len__ == 0 else 'oxitona' if self.silaba_tonica == OXITONA \
        else 'paraxitona' if self.silaba_tonica == PARAXITONA else 'proparaxitona' if self.silaba_tonica == PROPARAXITONA \
        else 'superproparaxitona'

    def __str__(self) -> str:
        tipo_palabra = self.tipo_palabra()
        return f'{self.silabas} - {tipo_palabra}'

    def dividir_patrones(self) -> None:
        def vocal_c_vocal() -> None:
            vcv = re.compile(f'(?=([{VOCALES}][{CONSONANTES}][{VOCALES}]))')
            patrones = vcv.finditer(self.palabra)
            for c in patrones:
                self.dict_silabas[c.start()+1] = c.group(1)[1:]

        def vocal_cc_vocal() -> None:
            #caso inseparable
            vccv_inseparable = \
            re.compile(f'(?=([{VOCALES}][{CONSONANTES_INSEPARABLES}][{CONSONANTES_LIQUIDAS}][{VOCALES}]|[{VOCALES}][cC][hH][{VOCALES}]))')
            patrones = vccv_inseparable.finditer(self.palabra)
            for c in patrones:
                self.dict_silabas[c.start()+1] = c.group(1)[1:]
            #caso separable
            vccv_separable = \
            re.compile(f'(?=([{VOCALES}][{CONSONANTES_INSEPARABLES}][{CONSONANTES_NO_LUQUIDAS}][{VOCALES}]|[{VOCALES}][{CONSONANTES_SEPARABLES}][{CONSONANTES_NO_LUQUIDAS}][{VOCALES}]|[{VOCALES}][{CONSONANTES_SEPARABLES}][{CONSONANTES_LIQUIDAS}][{VOCALES}]))')
            patrones = vccv_separable.finditer(self.palabra)
            for c in patrones:
                if c.group(1)[1] in 'cC' and c.group(1)[2] in 'hH':
                    continue
                self.dict_silabas[c.start()] = c.group(1)[:2]
                self.dict_silabas[c.start()+2] = c.group(1)[2:]
        
        def vocal_ccc_vocal() -> None:
            #caso separable
            vcccv_separable = \
                re.compile(f'(?=([{VOCALES}][Nn][Ss][{CONSONANTES}]+[{VOCALES}]))')
            patrones = vcccv_separable.finditer(self.palabra)
            for c in patrones:
                print(c.group(1))
                self.dict_silabas[c.start()] = c.group(1)[:3]
            #caso inseparable
            vcccv_inseparable = \
                re.compile(f'(?=([{VOCALES}][{CONSONANTES}]+[{CONSONANTES_INSEPARABLES}][{CONSONANTES}][{VOCALES}]))')
            patrones = vcccv_inseparable.finditer(self.palabra)
            for c in patrones:
                if c.group(1)[1] in 'nN' and c.group(1)[2] in 'sS':
                    continue
    
                self.dict_silabas[c.start()+2] = c.group(1)[-3:]
        #busqueda de patrones
        vocal_c_vocal()
        vocal_cc_vocal()
        vocal_ccc_vocal()

class Verso:
    def __init__(self,contenido,signos_puntuacion:dict) -> None:
        self.contenido:list[Palabra] = contenido 
        self.signos_puntuacion = signos_puntuacion
        self.calcular_silabas()
    
    def __str__(self) -> str:
        sb = ''
        for palabra in self.contenido:
            sb = sb + str(palabra.silabas) + " "
        if len(self.sinalefas) != 0:
            sb += f'\nSINALEFAS:\n'
            for sinalefa in self.sinalefas:
                sb += f'{self.sinalefas[sinalefa]} entre palabra {sinalefa+1} y {sinalefa +2} \n'
        sb += \
            f'\nsilabas fohologicas:{self.silabas_fohologicas}, silabas metricas:{self.silabas_metricas}, tipo:{self.obtener_tipo()}'
        return sb
    
    def obtener_tipo(self):
        return 'oxitono' if self.tipo == OXITONA \
        else 'paraxitono' if self.tipo == PARAXITONA else 'proparaxitono'
    
    def calcular_silabas(self):
        self.silabas_fohologicas = 0
        #busqueda de sinalefas
        self.sinalefas = {}
        for idx in range(len(self.contenido)-1):
            if self.contenido[idx].palabra[-1] in VOCALES+'yY' and self.contenido[idx+1].palabra[0] in VOCALES+'yYhH':
                if len(self.contenido[idx+1].palabra) > 1 and self.contenido[idx+1].palabra[0] in 'yY': # sonido ll
                    continue
                if self.contenido[idx+1].silaba_tonica + len(self.contenido[idx+1].palabra) == 0 and len(self.contenido[idx+1].palabra) != 1: #segunda vocal tónica
                    continue
                if idx in self.signos_puntuacion: # signo que genera pausa
                    continue
                self.sinalefas[idx] = self.contenido[idx].silabas[-1] + '-' + self.contenido[idx+1].silabas[0]
        for palabra in self.contenido:
            self.silabas_fohologicas += palabra.numero_silabas
        self.silabas_metricas = self.silabas_fohologicas - len(self.sinalefas)
        self.tipo = PARAXITONA
        if self.contenido[-1].silaba_tonica == OXITONA:
            self.tipo = OXITONA
            self.silabas_metricas = self.silabas_metricas + 1
        if self.contenido[-1].silaba_tonica == PROPARAXITONA:
            self.tipo = PROPARAXITONA
            self.silabas_metricas = self.silabas_metricas - 1
        if self.contenido[-1].silaba_tonica == SUPERPROPARAXITONA:
            self.tipo = SUPERPROPARAXITONA
            self.silabas_metricas = self.silabas_metricas - 2


class Poema:
    def __init__(self,poema:list[str]) -> None:
        self.poema = poema
        self.versos:list[Verso] = []
        self.rimas = {}
        self.analizar()

    def __str__(self) -> str:
        sb = f'ANALISIS:\nVERSOS:{len(self.versos)}'
        for verso in self.versos:
            sb+= f'\n {verso}'
        
        sb += f'\nPOEMA:\nsilabas fohologicas:{self.silabas_fohologicas}, silabas metricas:{self.silabas_metricas}'
        sb += '\nRIMAS:\n'
        for rima,tipo in self.rimas.items():
            sb += f'rima {tipo[0]} entre versos {tipo[1]} con sonido {rima}\n'
        return sb

    def analizar(self):
        self.limpiar_poema()
        self.buscar_rimas()
        self.calcular_silabas()
    
    def calcular_silabas(self):
        self.silabas_metricas = 0
        self.silabas_fohologicas = 0
        for verso in self.versos:
            self.silabas_metricas += verso.silabas_metricas
            self.silabas_fohologicas += verso.silabas_fohologicas
    def buscar_rimas(self):
        for idx in range(len(self.versos)-2):
            # rima consonante
            a = self.versos[idx].contenido[-1].rima_consonante()
            b= self.versos[idx+2].contenido[-1].rima_consonante()
            if(a == b):
                self.rimas[a] = ('consonante',(idx,idx+2))
                continue # si es consonante tambien es asonante
            a = self.versos[idx].contenido[-1].rima_asonante()
            b= self.versos[idx+2].contenido[-1].rima_asonante()
            if(a == b):
                self.rimas[a] = ('asonante',(idx,idx+2))

    
    def limpiar_poema(self):
        self.versos = []
        for verso in self.poema:
            verso_normalizado = verso.replace('\n','')
            signos_puntuacion = {}
            palabras = []
            for idx,palabra in enumerate(verso_normalizado.split()):
                if palabra[-1] in SIGNOS_PUNTUACION:
                    signos_puntuacion[idx] = palabra[-1]
                palabras.append(Palabra(palabra))
            self.versos.append(Verso(palabras,signos_puntuacion))


texto = open("poema.txt",mode="r",encoding="utf-8").readlines()
poema = Poema(texto)
print(poema)
