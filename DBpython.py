import pymysql as sql

def Conexion() :
    try :
        connexion = sql.connect(
                host="192.168.1.77",
                port=3306,
                database="banco",
                user="integrador",
                password="RETOS"
        )
        print("Se conecto ... Creo")
        return connexion;

    except sql.Error as error :
        print(f"algo fallo ... Creo {error}")
        return None;
