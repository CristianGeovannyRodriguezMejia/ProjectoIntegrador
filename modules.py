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

def InsetarContenido()-> None :
     

    id_transaccion =input("Digite el id  : ")
    tipo =input("Ingrese el tipo transaccion Deposito/Retiro/Tranferencia : ");
    cuenta_origen =input("digite la cuenta de origen : ");
    cuenta_destino =input("digite la cuenta destino : ");
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
        ps =connexion.cursor();
   
        sqlsentence ="INSEtipo =txt3.get();RT INTO transacciones(id_transaccion,fecha,tipo,cuenta_origen,cuenta_destino,monto,descripcion,usuario,) VALUES (%s,NOW(),%s,%s,%s,%s,%s,%s)";
        columnas = (id_transaccion,tipo,cuenta_origen,cuenta_destino,monto,descripcion,usuario,);

    
        ps.execute(sqlsentence,columnas)
        connexion.commit()
        print("Creo que se reguistro con exito")
    
    except pymysql.Error as fallo :
        print(f"Nose que paso pero : {fallo}")
        #Esto cancela la ejecucion si falla algo pongo esto por que no sabia que existia XD
        if connexion in locals(): connexion.rollback();
    finally :
        #pos esto hace lo que dice los cierra
       if ps in locals() : ps.close()
       if connexion in locals() : connexion.close()
    
    
    