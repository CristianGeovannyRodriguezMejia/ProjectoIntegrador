from conexion import *;
import pymysql;
import os
insertbeneficiaros=[];
updatebeneficiarios=[];
deletebeneficiarios=[];
#aqui estoy insertano lo menu de beneficiarios
def MenuBeneficiarios():
    opcionesBeneficiarios ="""
    ----Gestionar Beneficiarios----
    1.Mostrar Beneficiarios
    2.insertar un Beneficiario
    3.modificar Beneficiario 
    4.Eliminar Beneficiario 
    5. Volver al menu principal
    Digita la opcion: """
    opcBeneficiarios =0;
    while opcBeneficiarios != 5  :
        os.system("clear")
        opcBeneficiarios=int(input(opcionesBeneficiarios))
        match(opcBeneficiarios) :
         case 1 :        
            print("\n ----Reguistros----")
            print("id_log | nombre |  accion | tabla afectada | descripcion");
            if not MostrarBeneficiarios() :
                input("No existen reguistros en la base de datos");
            else :  
                for filas in MostrarBeneficiarios() : 
                    print(filas)
                input("\n pulse ENTER para continuar ")
         case 2:
            insertbeneficiaros.append(insertarBeneficiario());
            input("\n pulse ENTER para continuar ");
         case 3:
            updatebeneficiarios.append(ActualizarBeneficiario());
            input("\n pulse ENTER para continuar ");
         case 4:
            deletebeneficiarios.append(EliminarBeneficiario());
            print("\n pulse ENTER para continuar ");
         case 5 :
            # esta cosa hace que vuelva atraz neta python es bien practico en java para volver atras
            #tenia que hacer magia negra
                return ;


def insertarBeneficiario():
    id_cliente= input("Digite  el id del cliente : ")
    nombre = input("ingrese el nombre del benificiario : ")
    parentesco = input("Ingrese el parentesco : ")
    porsentaje = input("Digite el porsentaje asignado : ")
    try:
        c=Conexion()
        ps = c.cursor()

        sqlsentece = "INSERT INTO beneficiario(id_CLiente, nombre,parentesco,porsentaje)VALUES " 
        "(%(id_cliente)s,%(nombre)s,%(parentesco)s,%(porsentaje)s)"
        columnas = {"id_cliente": id_cliente, "nombre": nombre,"parentesco" : parentesco, "porsentaje" : porsentaje}
        ps.execute(sqlsentece, columnas)
        c.commit()
        print("beneficiario insertado con exito ")
        return columnas
    except pymysql.Error as fallo:
        print(f"error fatal : {fallo}")
        Conexion.rollback()
    finally:
        ps.close()
        Conexion.close()

def EliminarBeneficiario():
    try: 
        id_beneficiario = input("Digite el id del beneficiario a borrar : ")
        c = Conexion();
        ps = c.cursor()
        sqlsentence = "DELETE FROM beneficiario WHERE id_beneficiario = %(id_beneficiario)s"
        columnas = {"id_beneficiario": id_beneficiario}
        ps.execute(sqlsentence, columnas)
        c.commit()
        print("beneficiario eliminado con exito ")
    except pymysql.Error as fallo:
        print(f"error fatal : {fallo}")
        Conexion.rollback()
    finally:
        ps.close()
        Conexion.close()

def ActualizarBeneficiario():
            try:
                id_beneficiario = input("Digite el id del beneficiario a modificar : ")
                nombre = input("Ingrese el nuevo nombre del beneficiario : ")
                parentesco = input("Ingrese el nuevo parentesco : ")
                porsentaje = input("Ingrese el nuevo porcentaje asignado : ")
                c=Conexion()
                ps = Conexion.cursor()
                sqlsentence = "UPDATE beneficiario SET id_cliente = %(id_cliente)s, nombre = %(nombre)s, parentesco = %(parentesco)s, porsentaje = %(porsentaje)s WHERE id_beneficiario = %(id_beneficiario)s"
                columnas = {"id_beneficiario": id_beneficiario, "nombre": nombre, "parentesco": parentesco, "porsentaje": porsentaje}
                ps.execute(sqlsentence, columnas)
                c.commit()
                print("Beneficiario actualizado exitosamente")
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
        sqlsentence = "SELECT * FROM beneficiario;"
        ps.execute(sqlsentence)
        resul = ps.fetchall()
        return resul
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}")
    finally :
        ps.close()
        c.close()



