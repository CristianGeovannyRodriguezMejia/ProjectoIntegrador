import pymysql as sql

def Conexion() :
    try :
        connexion = sql.connect(
                host="10.110.152.8",
                port=3306,
                database="banco",
                user="INTEGRADOR",
                password="RETOS"
        )
        print("Se conecto ... Creo")
        return connexion;

    except sql.Error as error :
        print(f"algo fallo ... Creo {error}")
        return None;
