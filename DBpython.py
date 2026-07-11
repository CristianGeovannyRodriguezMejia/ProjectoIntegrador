import pymysql as sql


try :
    connexion = sql.connect(
            host="192.168.1.77",
            port=3306,
            database="banco",
            user="integrador",
            password="RETOS"
    )
    print("Se conecto ... Creo")

except sql.Error as error :
    print(f"Pos algo fallo ... Creo {error}")