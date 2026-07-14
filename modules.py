import pymysql
from DBpython import *;

def Menu()-> int :
    opciones = """ 
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

def InsetarContenido() :
    
    nombre =input(" : ");
    tasaInteres =input("digite el interes deseado : ");
    saldoMinimo =input("Digite el saldo minimo con la que iniciara : ");
    descripcion=input("descripcion de la cuenta : ");
    
    try :
        c=Conexion();
        ps =c.cursor()
   
        sqlsentence ="INSERT INTO tipos_cuenta(nombre,tasa_interes,saldo_minimo,descripcion),%(nombre)s,%(tasaInteres)s,%(saldoMinimo)s,%(descripcion)s)";
        columnas = {"nombre" : nombre, "tasaInteres" :tasaInteres,"saldoMinimo":saldoMinimo,"descripcion" : descripcion};

    
        ps.execute(sqlsentence,columnas);
        c.commit();
        print("trasaccion realizada con exito ");
        return columnas;
    
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}");
        #Esto cancela la ejecucion si falla algo pongo esto por que no sabia que existia XD
        c.rollback();
    finally :
        #pos esto hace lo que dice los cierra si existe en variables locales
        ps.close();
        c.close();


def EliminarContenido() :
     try :
        id=input("Digite el id de la cuenta a borrar : ")
        c=Conexion();
        ps =c.cursor();
        sqlsentence ="DELETE tipos_cuenta WHERE id_tipo =%(id)s  "
        columna = {'id':id }
        ps.execute(sqlsentence,columna)
        c.commit()
        print("Usuario borrado con exito")
        return columna
     except  pymysql.Error as fallo :
         print(f"error fatal : {fallo}")
         c.rollback()
     finally :
         ps.close()
         c.close();
def ActualizarContenido() :
    try :
        condicion =input("Ingrese el id del reguistro a modificar : ")

        
        nombre=input("Escriba el Tipo de cuenta : ");
        tasaInteres =input("Digite la tasa de interes deseada : ");
        saldoMinimo =input("Digite el saldo minimo con el que iniciara : ");
        descripcion =input("De una descricion de su cuenta : ");
        
        c =Conexion()
        ps =c.cursor();
        sqlsentence = "UPDATE tipos_cuenta SET nombre=%(nombre)s, tasa_interes=%(tasaInteres)s saldo_minimo=%(saldoMinimo)s descripcion=%(Descripcion)s WHERE id_trasacciones=%(condicion)s  "
        columna= {"condicion" :condicion,"tasaInteres": tasaInteres, "saldoMinimo":saldoMinimo,"Descripcion": descripcion}
        ps.execute(sqlsentence,columna);
        c.commit();
        print("Reguistro actualizado exitosamente")
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}")
        c.rollback()
    finally :
        ps.close();
        c.close();
def MostrarContenido():
    try : 
        c=Conexion();
        ps = c.cursor();
        sqlsentence ="SELECT * FROM tipos_cuenta;"
        ps.execute(sqlsentence)
        #no entendi bien pero baja los reguistros  de la DB y pos se la da a fila
        resul =ps.fetchall()
    
        return resul;
    except pymysql.Error as fallo :
          print(f"error fatal : {fallo}")
    finally :
         ps.close()
         c.close();