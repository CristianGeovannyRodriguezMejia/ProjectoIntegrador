import pymysql as sql
from config import (DB_HOST,DB_NAME,DB_PASSWORD,DB_PORT,DB_USER);
def Conexion() :
    try :
        connexion = sql.connect(
                host=DB_HOST,
                port=DB_PORT,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
        )
        print("Se conecto ... Creo")
        return connexion;

    except sql.Error as error :
        print(f"algo fallo ... Creo {error}")
        return None;
