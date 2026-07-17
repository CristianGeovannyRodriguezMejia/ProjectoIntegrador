from conexion import *;
import pymysql;
import os
insertbeneficiaros=[];
updatebeneficiarios=[];
deletebeneficiarios=[];
#aqui estoy insertano lo menu de beneficiarios
def MenuBeneficiarios():
    opcionesClientes ="""
    ----Gestionar Beneficiarios----
    1.Mostrar Clientes
    2.insertar un Clientes
    3.modificar Clientes
    4.Eliminar Clientes
    5. Volver al menu principal
    Digita la opcion: """
    opcClientes =0;
    while opcClientes != 5  :
        os.system("clear")
        opcClientes=int(input(opcionesClientes))
        match(opcClientes) :
         case 1 :        
            fi = MostrarBeneficiarios();
            print("\n ----Reguistros----")
            print("id_log | nombre |  accion | tabla afectada | descripcion");
            if not fi  :
                input("No existen reguistros en la base de datos");
            else :  
                for filas in fi : 
                    print(filas)
                input("\n pulse ENTER para continuar ")
                os.system("clear") 
         case 2:
            insertbeneficiaros.append(insertarBeneficiario());
            input("\n pulse ENTER para continuar ");
            os.system("clear") 
         case 3:
            updatebeneficiarios.append(ActualizarBeneficiario());
            input("\n pulse ENTER para continuar ");
            os.system("clear") 
         case 4:
            deletebeneficiarios.append(EliminarBeneficiario());
            print("\n pulse ENTER para continuar ");
            os.system("clear") 
         case 5 :
            # esta cosa hace que vuelva atraz neta python es bien practico en java para volver atras
            #tenia que hacer magia negra
                return ;


def insertarBeneficiario():
    dui= input("Digite su dui : ")
    nombre = input("Ingrese su nombres : ")
    apellido = input("Ingrese su apellidos : ")
    Fechanacimiento = input("Digite su fecha de nacimiento aa/mm/dd : ")
    dirrecion =input("Ingreses su dirrecion exacta de domicilio : ")
    telefono = input("Digite su telefono : ")
    correo = input("Ingrese una dirrecion de correo : ")

    try:
        c=Conexion()
        ps = c.cursor()

        sqlsentece = """INSERT INTO clientes (dui,nombres,apellidos,fecha_nacimiento,dirrecion,telefono,correo,fecha_reguistro) VALUES (%(dui)s,%(nombres)s,%(apellidos)s,%(fechaNacimiento)s,%(dirrecion)s,%(telefono)s,%(correo)s,NOW())"""
        columnas = {"dui": dui ,"nombres": nombre,"apellidos" : apellido, "fechaNacimiento" : Fechanacimiento,"dirrecion":dirrecion,"telefono":telefono,"coreo": correo}
        ps.execute(sqlsentece, columnas)
        c.commit()
        print("Cliente insertado con exito ")
        return columnas
    except pymysql.Error as fallo:
        print(f"error fatal : {fallo}")
        c.rollback()
    finally:
        ps.close()
        c.close()

def EliminarBeneficiario():
    try: 
        id_cliente = input("Digite el id del cliente a borrar : ")
        c = Conexion();
        ps = c.cursor()
        sqlsentence = "DELETE FROM clientes WHERE id_cliente = %(cliente)s"
        columnas = {"cliente": id_cliente}
        ps.execute(sqlsentence, columnas)
        c.commit()
        print("cliente eliminado con exito ")
    except pymysql.Error as fallo:
        print(f"error fatal : {fallo}")
        Conexion.rollback()
    finally:
        ps.close()
        c.close()

def ActualizarBeneficiario():
            try:
                id = input("Digite el id del beneficiario a modificar : ")


                dui =int("Digite el dui del cliente : ")
                nombres = input("Ingrese el nuevo nombre del beneficiario : ")
                apellidos = input("Ingrese el nuevo parentesco : ")
                fechaNacimiento = input("Ingrese el nuevo porcentaje asignado : ")
                dirrecion =input("Ingrese su dirrecion : ")
                telefono = input("ingresa tu telefono : ")
                correo = input("ingresa tu correo")
                c=Conexion()
                ps = Conexion.cursor()
                sqlsentence = "UPDATE clientes SET dui = %(Dui)s, nombres = %(Nombre)s, apellidos = %(Apellido)s, fecha_nacimiento = %(Nacimiento)s,dirrecion =%(Dirrecion)s,telefono =%(Telefono)s,correo =%(Correo)s  WHERE id_cliente = %(condicion)s"
                columnas = {"condicion": id,"Dui": dui, "Nombre": nombres, "Apellido": apellidos, "Nacimiento": fechaNacimiento,"Dirrecion" : dirrecion,"Telefono" : telefono,"Correo" : correo}
                ps.execute(sqlsentence, columnas)
                c.commit()
                print("Beneficiarios actualizado exitosamente")
            except pymysql.Error as fallo :
             print(f"error fatal : {fallo}")
             c.rollback()
            finally :
                ps.close()
                c.close()

#codigo de tabla benefisiarios no se si asi es o que pedo
def MostrarBeneficiarios():
    try :
        c =Conexion()
        ps = c.cursor()
        sqlsentence = "SELECT * FROM clientes;"
        ps.execute(sqlsentence)
        resul = ps.fetchall()
        return resul
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}")
    finally :
        ps.close()
        c.close()



