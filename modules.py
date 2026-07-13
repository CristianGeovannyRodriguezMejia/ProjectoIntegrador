import pymysql
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

def InsetarContenido() :
    id =input("Digite el id  : ")
    tipo =input("Ingrese el tipo transaccion Deposito/Retiro/Tranferencia/Pago Servicio/Intereses : ");
    cuentaO =input("digite la cuenta de origen : ");
    cuentaD =input("digite la cuenta destino : ");
    monto =input("digite el monto : ");
    descripcion=input("descricion de tranferencia : ");
    usuario = input("Ingrese su nombre de ususario :")
    try :
        connexion=pymysql.connect(host='192.168.1.77'
                                  ,port=3306,
                                  user='integrador'
                                  ,password='RETOS'
                                  ,database='banco'
                                  )
        ps =connexion.cursor()
   
        sqlsentence ="INSERT INTO transacciones(id_transaccion,fecha,tipo,cuenta_origen,cuenta_destino,monto,descripcion,usuario) VALUES (%(id)s,NOW(),%(tipo)s,%(cuentaO)s,%(cuentaD)s,%(monto)s,%(descripcion)s,%(user)s)";
        columnas = {"id" : id,"tipo" : tipo, "cuentaO" :cuentaO,"cuentaD":cuentaD, "monto":monto,"descripcion" : descripcion , "user":usuario};

    
        ps.execute(sqlsentence,columnas);
        connexion.commit();
        print("trasaccion realizada con exito ");
        return columnas;
    
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}");
        #Esto cancela la ejecucion si falla algo pongo esto por que no sabia que existia XD
        connexion.rollback();
    finally :
        #pos esto hace lo que dice los cierra si existe en variables locales
        ps.close();
        connexion.close();


def EliminarContenido() :
     try :
        id=input("Digite el id de ususario a borrar : ")
        connexion=pymysql.connect(host='192.168.1.77'
                                  ,port=3306,
                                  user='integrador'
                                  ,password='RETOS'
                                  ,database='banco'
                                  )
        ps =connexion.cursor();
        sqlsentence ="DELETE transacciones WHERE id_transaccion =%(id)s  "
        columna = {'id':id }
        ps.execute(sqlsentence,columna)
        connexion.commit()
        print("Usuario borrado con exito")
        return columna
     except  pymysql.Error as fallo :
         print(f"error fatal : {fallo}")
         connexion.rollback()
     finally :
         ps.close()
         connexion.close();
def ActualizarContenido() :
    try :
        condicion =input("Ingrese el id del reguistro a modificar : ")

        id =input("Digite el id  : ")
        tipo =input("Ingrese el tipo transaccion Deposito/Retiro/Tranferencia/Pago Servicio/Intereses : ");
        cuentaO =input("digite la cuenta de origen : ");
        cuentaD =input("digite la cuenta destino : ");
        monto =input("digite el monto : ");
        descripcion=input("descricion de tranferencia : ");
        usuario = input("Ingrese su nombre de ususario :")
        connexion=pymysql.connect(host='192.168.1.77'
                                  ,port=3306,
                                  user='integrador'
                                  ,password='RETOS'
                                  ,database='banco'
                                  )
        ps =connexion.cursor();
        sqlsentence = "UPDATE transacciones SET id_transaccion =%(id)s, fecha = NOW(), tipo = %(tipo)s, cuenta_origen = %(CuentaD)s, cuenta_destino = %(cuentaD)s, monto =%(monto)s,descripcion = %(Descripcion)s,usuario =%(user)s WHERE id_trasacciones=%(condicion)s  "
        columna= {"condicion" :condicion,"id" : id,"tipo": tipo, "CuentaO":cuentaO,"CuentaD":cuentaD,"monto": monto,"Descripcion": descripcion,"user": usuario}
        ps.execute(sqlsentence,columna);
        connexion.commit();
        print("Reguistro actualizado exitosamente")
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}")
        connexion.rollback()
    finally :
        ps.close();
        connexion.close();
def MostrarContenido():
    try : 
        connexion=pymysql.connect(host='192.168.1.77'
                                  ,port=3306,
                                  user='integrador'
                                  ,password='RETOS'
                                  ,database='banco'
                                  )
        ps = connexion.cursor();
        sqlsentence ="SELECT * FROM transacciones;"
        ps.execute(sqlsentence)
        #no entendi bien pero baja los reguistros  de la DB y pos se la da a fila
        # y lo recorremos con un for como todo un pro
        resul =ps.fetchall()
    
        return resul;
    except pymysql.Error as fallo :
          print(f"error fatal : {fallo}")
    finally :
            ps.close()
            connexion.close();