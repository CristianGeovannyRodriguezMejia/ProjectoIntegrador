from Sucursales import * ;
from TiposCuenta import *;
import os
opc=0;
while opc != 5  :
    os.system("clear");
    opc=MenuPrincipal()
    match(opc):
     case 1 :
        MenuCuentas();
     case 2:
         MenuSurcusales()
     case 3:
         update.append(ActualizarContenido());
         print("\n pulse ENTER para continuar ");
     case 4:
        delete.append(EliminarContenido());
        print("\n pulse ENTER para continuar ");



    
