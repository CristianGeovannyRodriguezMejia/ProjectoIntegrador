import pymysql;
from DBpython import *;
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

def InsetarContenido()-> None :
     
     idpersona =txt1.get()
     nombre =txt2.get();
     edad =txt.get();
     sqlsentence ="";
     columnas = ();
     connexion=pymysql.connect(host='',user='',password='',database='')
     curso=connexion.cursor();
     resul=curso.execute(sqlsentence, columnas)
    