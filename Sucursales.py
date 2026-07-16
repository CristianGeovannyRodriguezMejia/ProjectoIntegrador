import pymysql
from DBpython import *;
insertSucusal={};
updateSucursal={};
deleteSurcusal={};
def MenuSurcusales():
    opcionesSucusal = """ 
    === GESTION DE SUCURSALES ===
    1. Mostrar Sucursales
    2. Insertar Sucursales
    3. Actualizar sucursal
    4. Eliminar sucursal
    5. Atras
    Digita la opción deseada: """
    opcSucursal=0;
    while opcSucursal != 5  :
        opcSucursal =int(input(opcionesSucusal))
        match(opcSucursal):
         case 1 :        
            print("\n ----Reguistros----")
            print("id_tipo | nombre |  tasa_interes | saldo_minimo | descripcion");
            if not mostrar_sucursales() :
                input("No existen reguistros en la base de datos");
            else :  
                for filas in mostrar_sucursales() : 
                    print(filas)
                input("\n pulse ENTER para continuar ")
         case 2:
            insertSucusal.append(insertar_Sucursal());
            input("\n pulse ENTER para continuar ");
         case 3:
            updateSucursal.append(actualizar_sucursal());
            input("\n pulse ENTER para continuar ");
         case 4:
            deleteSurcusal.append(eliminar_sucursal());
            print("\n pulse ENTER para continuar ");
         case 5 :
                return ;

#gestion de sucursales (carlos)
def insertar_Sucursal():
        print ("=== Registrar sucursal ===")
        #no pedimos id por lo que dijimos en clase del autoincrement que se agrega auto
        nombre = input("Digite el nombre de la sucursal: ")
        direccion = input("Digite la direccion de la sucursal: ")
        telefono = input("Digite el telefono de la sucursal: ")
        ciudad = input("Digite la ciudad de la sucursal: ")

        conexion = Conexion()
        if conexion is None:
            return None
        
        try:
            ps = conexion.cursor()
            sqlsetence = """
                insert into sucursales(nombre, direccion, telefono, ciudad)      
                values (%(nombre)s, %(direccion)s, %(telefono)s, %(ciudad)s)
            """

            columnas = {
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "ciudad": ciudad
            }

            ps.execute(sqlsetence, columnas)
            conexion.commit()
            print("Se registro la sucursal correctamente")
            return columnas
        except pymysql.Error as fallo:
            print(f"Error al registrar la sucursal: {fallo}")
            conexion.rollback()
        finally:
            ps.close()
            conexion.close()
    

def mostrar_sucursales():
        conexion = Conexion()
        if conexion is None:
            return []
        try:
            ps = conexion.cursor()
            sqlsentence = "SELECT nombre, direccion, telefono, ciudad FROM sucursales"
            ps.execute(sqlsentence)
            resultados = ps.fetchall()
            return resultados
        except pymysql.Error as fallo:
            print(f"Error al obtener las sucursales: {fallo}")
            return []
        finally:
            ps.close()
            conexion.close()
    
def eliminar_sucursal():
        print("=== Eliminar sucursal ===")
        id_suc = input("Digite el ID de la sucursal a eliminar: ")

        conexion = Conexion()
        if conexion is None:
            return None
        
        try:
            ps = conexion.cursor()
            sqlsentence = "delete from sucursales where id_sucursal = %(id_suc)s"
            columnas = {"id": id_suc}
            ps.execute(sqlsentence, columnas)
            conexion.commit()
            print("Sucursal eliminada correctamente")
            return columnas
        except pymysql.Error as fallo:
            print(f"Error al eliminar la sucursal: {fallo}")
            conexion.rollback()
        finally:
            ps.close()
            conexion.close()


def actualizar_sucursal():
        print("=== Actualizar sucursal ===")
        id_suc = input("Digite el ID de la sucursal a actualizar: ")
        nombre = input("Digite el nuevo nombre de la sucursal: ")
        direccion = input("Digite la nueva direccion de la sucursal: ")
        telefono = input("Digite el nuevo telefono de la sucursal: ")
        ciudad = input("Digite la nueva ciudad de la sucursal: ")

        conexion = Conexion()
        if conexion is None:
            return None
        
        try:
            ps = conexion.cursor()
            sqlsentence = """
                update sucursales
                set nombre = %(nombre)s, direccion = %(direccion)s, telefono = %(telefono)s, ciudad = %(ciudad)s
                where id_sucursal = %(id_suc)s
            """
            columnas = {
                "id": id_suc,
                "nombre": nombre,
                "direccion": direccion,
                "telefono": telefono,
                "ciudad": ciudad
            }
            ps.execute(sqlsentence, columnas)
            conexion.commit()
            print("Sucursal actualizada correctamente")
            return columnas
        except pymysql.Error as fallo:
            print(f"Error al actualizar la sucursal: {fallo}")
            conexion.rollback()
        finally:
            ps.close()
            conexion.close()

#Menu principal que controla los submenus para las otras bases
#de datos tremendo me eh roto la cabeza con esta wea
def MenuPrincipal() -> int :
    opciones = """ 
    === CONTROL DE BASE DE DATOS BANCO ===
    1. Gestionar Tipos Cuenta
    2. Gestionar Sucursales
    3. Gestionar Beneficiarios
    4. Gestionar Auditoria
    Digita el número de la tabla a gestionar:  """
    try:
        return int(input(opciones))
    
    except ValueError:
        return 0