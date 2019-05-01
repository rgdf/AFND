
from textwrap import wrap

class Automata:
    #Constructor de la clase Automata

    def __init__(self, transiciones, estado_final, estado_inicial,caracteres_alf):
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.caracteres_alf = caracteres_alf
        self.resultado = None

    #Si la palabra es de long 1 y no pertenece al alfabeto, se rechaza directamente
    #Si la palabra es de long > 1 y no pertenece al alfabeto, se rechaza directamente

 
    def comprobarPalabra(self,transiciones,palabra,estado_final,estado_actual,resultado):
        if(len(palabra)>1 or len(palabra)==1):
            for cada in palabra:
                if(int(cada) > len(self.caracteres_alf)):
                    self.resultado = 'rejected'
                    return self.resultado

            for each in transiciones[int(estado_actual)][int(palabra[0])]:
                estado_actual = each
                if len(palabra)==1:
                    if (str(estado_actual) in estado_final):
                        self.resultado = 'accepted'
                    else:
                        continue
                else:
                    self.comprobarPalabra(transiciones, palabra[1:],estado_final,estado_actual,self.resultado)        
        return self.resultado
  

#Hasta que no se pulsa CTRLC no sale del bucle
def definirAlfabeto():
    try:
        caracteres=[]
        while True:
            caracteres.append(input('Introduzca los caracteres del alfabeto: '))
    except KeyboardInterrupt:
     pass
     print('\n')
    return caracteres

#Hasta que no se pulsa CTRLC no sale del bucle
def definirEstadosFinales():
    try:
        estados_finales = []
        while True:
            estados_finales.append(input('Introduzca los estados finales del automata: '))
    except KeyboardInterrupt:
      pass
    print('\n')
    return estados_finales

def definirEstadoInicial():
    return input('Introduzca el estado inicial: ')

def pedirEntradaAutomata():
    entrada = input('Introduzca una secuencia de caracteres: ')
    return list(entrada)

def pedir_numEstadosAutomata():
    num_estados = input('Introduzca el número de estados que tendrá el autómata: ')
    return int(num_estados)

#En esta función recorremos la palabra introducida y la pasamos a numeros ( a=0, b=1, etc)
#En el caso de que un carácter no esté en el alfabeto del autómata, se le asigna un índice superior al resto
#que luego nos ayuda a procesarlo en la comprobación de la palabra

def convertirCaracteresIndices(palabra,caracteres_alf):
    for index in range(len(palabra)):
        j=0
        if(palabra[index] == caracteres_alf[j]):
            palabra[index] = str(j)
        else:
            enc=False
            while(j<len(caracteres_alf)and not(enc)):
                if(palabra[index] == caracteres_alf[j]):
                    palabra[index] = str(j)
                    enc=True
                j=j+1
            if(not(enc)):
                palabra[index] = str(j+1)
    return palabra

#En esta función creamos una lista vacía, dentro de la lista de transiciones, por cada estado del autómata (línea 87)
#Después por cada carácter del alfabeto definimos las transiciones desde el estado actual
#Primero cogemos la entrada por teclado, y separamos los números de 1 en 1
#Después en el for con k convertimos los str en int
#Por último añadimos la lista con las transiciones para el caracter

def definirTransicionesAutomata(num_estados,num_caracteres,lista_transiciones,caracteres_alf):
    for i in range(num_estados):
        lista_transiciones.append([])
        for j in range(num_caracteres):
            transicion_estado = input('Introduzca los estados a los que se va con el caracter '+caracteres_alf[j]+' desde el estado '+str(i)+': ')
            transicion_estado = wrap(transicion_estado,1)
            for k in range(len(transicion_estado)):
                transicion_estado[k] = int(transicion_estado[k])
            lista_transiciones[i].append(transicion_estado)
    return lista_transiciones



def main():

#Definimos el alfabeto del automata1
    caracteres_alf1 = ['a','b','c']
    #Definimos las transiciones del automata1
    transicionesA1 = [[[1,4,6],[3,4,6],[]] ,[[],[],[]] ,[[],[1,2,6],[]] ,[[],[],[]] ,[[3],[],[5]] ,[[],[6],[]], [[],[],[]]]    
    #Definimos los estados finales, el estado inicial y un resultado del automata1
    finales1 = ["6"]
    inicio1 = 0
    resultado1 = None
    #Creamos el automata1
    automata1 = Automata(transicionesA1,finales1,inicio1,caracteres_alf1)
    #Recogemos la entrada a reconocer por el automata1
    palabra1 = list('abbcb')
    print('w1 = ',palabra1)
    #Asignamos un índice a cada carácter
    palabra1 = convertirCaracteresIndices(palabra1,caracteres_alf1)
    #Comprobamos si la palabra es reconocida por el autómata1
    salida1 = automata1.comprobarPalabra(automata1.transiciones,palabra1,automata1.estado_final,automata1.estado_inicial, automata1.resultado)
    if(salida1 == None or salida1 == 'rejected'):
        print('La palabra No es aceptada por el autómata 1')    
    else:
        print('La palabra es aceptada por el autómata 1')

    print()

    #Definimos el alfabeto del automata2
    caracteres_alf2 = ['a','b']
    #Definimos las transiciones del autómata2
    transicionesA2 = [ [[1],[0,1]] ,[[0,2],[0]] , [[2,3],[3]] , [[4],[0]] , [[4],[5]] , [[4],[4,6]], [[6,7],[6]], [[4],[6]] ]
    #Definimos los estados finales, el estado inicial y un resultado del automata2
    finales2 = ["4","5","6","7"]
    inicio2 = 0
    resultado2 = None
    #Creamos el autómata2
    automata2 = Automata(transicionesA2,finales2,inicio2,caracteres_alf2)
    #Recogemos la entrada a reconocer por el automata2
    palabra2 = list('bbbabababaaaaabbb')
    print('w2 = ',palabra2)
    #Asignamos un índice a cada carácter
    palabra2 = convertirCaracteresIndices(palabra2,caracteres_alf2)
    #Comprobamos si la palabra es reconocida por el autómata2
    salida2 = automata2.comprobarPalabra(automata2.transiciones,palabra2,automata2.estado_final,automata2.estado_inicial, automata2.resultado)
    if(salida2 == None or salida2 == 'rejected'):
        print('La palabra No es aceptada por el autómata 2')
    else:
        print('La palabra es aceptada por el autómata 2')


    #Definimos el alfabeto del automata
    caracteres = definirAlfabeto()
    caracteres_alf = list(caracteres)
    #Definimos el número de estados que tendrá el autómata
    num_estados = pedir_numEstadosAutomata()
    #Definimos los estados finales del automata
    finales = definirEstadosFinales()
    #Definimos el estado inicial del automata
    inicio = definirEstadoInicial()
    #Definimos las transiciones del automata

    #transicionesA1 = [[[1,4,6],[3,4,6],[]] ,[[],[],[]] ,[[],[1,2,6],[]] ,[[],[],[]] ,[[3],[],[5]] ,[[],[6],[]], [[],[],[]]]                  
    #transicionesA2 = [ [[1],[0,1]] ,[[0,2],[0]] , [[2,3],[3]] , [[4],[0]] , [[4],[5]] , [[4],[4,6]], [[6,7],[6]], [[4],[6]] ]

    transiciones = []
    transiciones = definirTransicionesAutomata(num_estados,len(caracteres_alf),transiciones,caracteres_alf) 

    #Creamos el automata con los datos recogidos
    automata = Automata(transiciones,finales,inicio,caracteres_alf)
   
    #Recogemos la entrada a reconocer por el automata
    palabra = pedirEntradaAutomata()
  
    #Asignamos un índice a cada carácter
    palabra = convertirCaracteresIndices(palabra,caracteres_alf)
    salida = automata.comprobarPalabra(automata.transiciones,palabra,automata.estado_final,automata.estado_inicial,automata.resultado)
    if(salida == None or salida == 'rejected'):
        print('La palabra No es aceptada por el autómata ')
    else:
        print('La palabra es aceptada por el autómata ')

main()

