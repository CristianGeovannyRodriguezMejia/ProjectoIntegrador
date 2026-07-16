import pymysql
from conexion import *;
#Aca creo la variables globales 
insertAuditoria=[];
updateAuditoria=[];
deleteAuditoria=[];
#creacion del submenu de auditorias aunque es de sucursales jajaj
def MenuAuditoria():
    opcionesAuditoria = """ 
    === GESTION DE AUDITORIA ===
    1. Mostrar reguistros de auditoria
    2. Insertar  reguistros a auditoria
    3. Actualizar regustros de auditoria
    4. Eliminar regustros de auditoria
    5. Atras
    Digita la opción deseada: """
    opcAuditoria =0;
    while opcAuditoria != 5  :
        opcAuditoria=int(input(opcionesAuditoria))
        match(opcAuditoria) :
         case 1 :        
            print("\n ----Reguistros----")
            print("id_log | nombre |  accion | tabla afectada | descripcion");
            if not MostrarContenido() :
                input("No existen reguistros en la base de datos");
            else :  
                for filas in MostrarContenido() : 
                    print(filas)
                input("\n pulse ENTER para continuar ")
         case 2:
            insertAuditoria.append(InsetarContenido());
            input("\n pulse ENTER para continuar ");
         case 3:
            updateAuditoria.append(ActualizarContenido());
            input("\n pulse ENTER para continuar ");
         case 4:
            deleteAuditoria.append(EliminarContenido());
            print("\n pulse ENTER para continuar ");
         case 5 :
            # esta cosa hace que vuelva atraz neta python es bien practico en java para volver atras
            #tenia que hacer magia negra
                return ;

#esta funcion es para insertar contenido en la tabla, como el id_log tine autoincremen no lo pongo
def InsetarContenido () :
    #esto es para pedir datos al usuario
    nombre =input("Ingrese el usuario a ingresar : ");
    accion =input("Ingrese la accion a realizar INSERT/UPDATE/DELETE : ");
    tablaAfectada=input("Ingrese la tabla a afectar : ");
    descripcion=input("descripcion de la accion : ");
    
    try :
        #llamado a la connexion en DBpython
        c=Conexion();
        #creacion del un cursor es un puntenro practicamente
        ps =c.cursor()
        #creacion de la consulta sql
        sqlsentence ="INSERT INTO auditoria(usuario,fecha,accion,tabla_afectada,descripcion)VALUES (%(nombre)s,NOW(),%(Accion)s,%(Tabla)s,%(descripcion)s)";
        columnas = {"nombre" : nombre, "Accion" :accion,"Tabla":tablaAfectada,"descripcion" : descripcion};

        #ejecucion de esta gracias al puntero
        ps.execute(sqlsentence,columnas);
        #hacer que se guarde
        c.commit();
        print("Ingresado con exito ");
        return columnas;
     #esto es mas que todo para errores
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}");
        #Esto cancela la ejecucion si falla algo pongo esto por que no sabia que existia XD
        #lo que hace es que si la cosa llega a fallar vuelve la base de datos a su estado
        #original
        c.rollback();
    finally :
        #pos esto hace lo que dice los cierra 
        ps.close();
        c.close();

#esta es para eliminar contenido de la tabla en base a su id_log de pelos la verdad
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

#actualizar contendo de la tabla algo cmo el profe lo hizo
def ActualizarContenido() :
    try :
        condicion =input("Ingrese el id del log a cambiar : ")

        
        nombre=input("Escriba el usuario a ingresar: ");
        accion =input("Ingrese la accion a realizar INSERT/UPDATE/DELETE : ");
        tablaAfectada =input("Ingrese la tabla a realizar la accion : ");
        descripcion =input("De una descricion de la accion : ");
        
        c =Conexion()
        ps =c.cursor();
        sqlsentence = "UPDATE auditoria SET fecha=NOW() usuaio=%(nombre)s, accion=%(accion)s tabla_afectada=%(Tabla)s descripcion=%(Descripcion)s WHERE id_log=%(condicion)s  "
        columna= {"condicion" :condicion,"nombre": nombre,"Accion": accion, "Tabla":tablaAfectada,"Descripcion": descripcion}
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
        #no entendi bien pero baja los reguistros  e la DB y pos da una tulpa algo asi 
        # y eso puedo retornar 
        resul =ps.fetchall()
    
        return resul;
    except pymysql.Error as fallo :
          print(f"error fatal : {fallo}")
    finally :
         ps.close()
         c.close();