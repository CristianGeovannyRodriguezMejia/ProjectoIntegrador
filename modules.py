import os ;

def Menu()-> int :
    opciones = """" 
    Opciones a Elegir
    1.Mostrar Contenido
    2.Inserta un Reguistro
    3.Modificar Reguistro
    4.Eliminar Reguistro
    5.Salir
    Digita la opcion :
    """
    opc =int(input(opciones))
    return opc

#def MostrarContenido()-> None :
    