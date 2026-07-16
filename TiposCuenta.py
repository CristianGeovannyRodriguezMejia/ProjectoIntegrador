import pymysql 
from DBpython import *;
import os;

insert=[];
update=[];
delete=[];
def MenuCuentas() :
    opcionesCuenta = """ 
    Opciones a Elegir
    1.Mostrar Contenido
    2.Inserta un Reguistro
    3.Modificar Reguistro
    4.Eliminar Reguistro
    5.Atras
    Digita la opcion a usar :
    """
    opcCuenta =0;
    while opcCuenta != 5  :
        opcCuenta =int(input(opcionesCuenta))
        match(opcCuenta):
         case 1 :        
            print("\n ----Reguistros----")
            print("id_tipo | nombre |  tasa_interes | saldo_minimo | descripcion");
            if not MostrarContenido() :
                input("No existen reguistros en la base de datos");
            else :  
                for filas in MostrarContenido() : 
                    print(filas)
                input("\n pulse ENTER para continuar ")
         case 2:
            insert.append(InsetarContenido());
            input("\n pulse ENTER para continuar ");
         case 3:
            update.append(ActualizarContenido());
            input("\n pulse ENTER para continuar ");
         case 4:
            delete.append(EliminarContenido());
            print("\n pulse ENTER para continuar ");
         case 5 :
                return ;

def InsetarContenido() :
    
    nombre =input("escribe el nombre : ");
    tasaInteres =input("digite el interes deseado : ");
    saldoMinimo =input("Digite el saldo minimo con la que iniciara : ");
    descripcion=input("descripcion de la cuenta : ");
    
    try :
        c=Conexion();
        ps =c.cursor()
   
        sqlsentence ="INSERT INTO tipos_cuenta(nombre,tasa_interes,saldo_minimo,descripcion) VALUES (%(nombre)s,%(tasaInteres)s,%(saldoMinimo)s,%(descripcion)s)";
        columnas = {"nombre" : nombre, "tasaInteres" :tasaInteres,"saldoMinimo":saldoMinimo,"descripcion" : descripcion};
    
        ps.execute(sqlsentence,columnas);
        c.commit();
        print("trasaccion realizada con exito ");
        return columnas;
    
    except pymysql.Error as fallo :
        print(f"error fatal : {fallo}");
        #Esto cancela la ejecucion si falla algo pongo esto por que no sabia que existia XD
        c.rollback();
    finally :
        #pos esto hace lo que dice los cierra si existe en variables locales
        ps.close();
        c.close();


def EliminarContenido() :
     try :
        id=input("Digite el id de la cuenta a borrar : ")
        c=Conexion();
        ps =c.cursor();
        sqlsentence ="DELETE FROM tipos_cuenta WHERE id_tipo =%(id)s"
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
def ActualizarContenido() :
    try :
        condicion =input("Ingrese el id del reguistro a modificar : ")

        
        nombre=input("Escriba el Tipo de cuenta : ");
        tasaInteres =input("Digite la tasa de interes deseada : ");
        saldoMinimo =input("Digite el saldo minimo con el que iniciara : ");
        descripcion =input("De una descricion de su cuenta : ");
        
        c =Conexion()
        ps =c.cursor();
        sqlsentence = "UPDATE tipos_cuenta SET nombre=%(nombre)s, tasa_interes=%(tasaInteres)s, saldo_minimo=%(saldoMinimo)s, descripcion=%(Descripcion)s WHERE id_tipo=%(condicion)s  "
        columna= {"condicion" :condicion,"nombre" : nombre,"tasaInteres": tasaInteres, "saldoMinimo":saldoMinimo,"Descripcion": descripcion}
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
        sqlsentence ="SELECT * FROM tipos_cuenta;"
        ps.execute(sqlsentence)
        #no entendi bien pero baja los reguistros  de la DB y pos se la da a fila
        resul =ps.fetchall()
        return resul;
   
    except pymysql.Error as fallo :
          print(f"error fatal : {fallo}")
    finally :
         ps.close()
         c.close();

