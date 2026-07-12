from modules import * 
import os
opc=0;
insert=[];
delete=[];
fila= MostrarContenido();
while opc != 5 :
    os.system("clear");
    opc=Menu();
    match(opc):
     case 1 :
      pass
     case 2:
        insert.append(InsetarContenido());
        input("PAUSA PE");
     case 3:
            print("\n ---Reguistros---")
            if not fila :
               print("No hay pe");
            else :  
               for filas in fila :
                  print(filas);
            
            input("PAUSA PE")
     case 4:
        delete.append(EliminarContenido());
     case 5 :
         pass


    
