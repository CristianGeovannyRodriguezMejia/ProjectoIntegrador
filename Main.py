from modules import * 
import os
opc=0;
insert=[];
delete=[];
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
        pass
     case 4:
        delete.append(EliminarContenido());
     case 5 :
         pass


    
