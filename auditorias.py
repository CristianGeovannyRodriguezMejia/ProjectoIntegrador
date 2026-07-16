import pymysql
from DBpython import *;

def InsetarContenido() :
    
    nombre =input(" Ingrese el usuario a ingresar : ");
    accion =input("Ingrese la accion a realizar INSERT/UPDATE/DELETE : ");
    tablaAfectada=input("Ingrese la tabla a afectar : ");
    descripcion=input("descripcion de la accion : ");
    
    try :
        c=Conexion();
        ps =c.cursor()
   
        sqlsentence ="INSERT INTO auditoria(nombre,accion,tabla_afectada,descripcion),%(nombre)s,%(Accion)s,%(Tabla)s,%(descripcion)s)";
        columnas = {"nombre" : nombre, "Accion" :accion,"Tabla":tablaAfectada,"descripcion" : descripcion};

    
        ps.execute(sqlsentence,columnas);
        c.commit();
        print("Ingresado con exito ");
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
        id=input("Digite el id de el log a borrar : ")
        c=Conexion();
        ps =c.cursor();
        sqlsentence ="DELETE auditoria WHERE id_log =%(id)s  "
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
        condicion =input("Ingrese el id del log a cambiar : ")

        
        nombre=input("Escriba el usuario a ingresar: ");
        accion =input("Ingrese la accion a realizar INSERT/UPDATE/DELETE : ");
        tablaAfectada =input("Ingrese la tabla a realizar la accion : ");
        descripcion =input("De una descricion de la accion : ");
        
        c =Conexion()
        ps =c.cursor();
        sqlsentence = "UPDATE auditoria SET nombre=%(nombre)s, accion=%(accion)s tabla_afectada=%(Tabla)s descripcion=%(Descripcion)s WHERE id_log=%(condicion)s  "
        columna= {"condicion" :condicion,"Accion": accion, "Tabla":tablaAfectada,"Descripcion": descripcion}
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
        sqlsentence ="SELECT * FROM auditoria;"
        ps.execute(sqlsentence)
        #no entendi bien pero baja los reguistros  de la DB y pos se la da a fila
        resul =ps.fetchall()
    
        return resul;
    except pymysql.Error as fallo :
          print(f"error fatal : {fallo}")
    finally :
         ps.close()
         c.close();