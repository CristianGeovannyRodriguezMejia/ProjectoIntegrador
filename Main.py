from modules import * 
import os
opc=0;
insert=[];
while opc != 6 :
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
        pass


    
