from modules import * 
import os
opc=0;
insert=[];
delete=[];
update=[];
fila = MostrarContenido();
while opc != 5 :
    os.system("clear");
    opc=Menu();
    match(opc):
     case 1 :
         print("\n ----Reguistros----")
         if not fila :
            print("No existen reguistros en la base de datos");
         else :  
            for filas in fila :
               print(filas);     
            print("\n pulse ENTER para continuar ")      
     case 2:
        insert.append(InsetarContenido());
        print("\n pulse ENTER para continuar ");
     case 3:
         update.append(ActualizarContenido());
         print("\n pulse ENTER para continuar ");
     case 4:
        delete.append(EliminarContenido());
        print("\n pulse ENTER para continuar ");



    
