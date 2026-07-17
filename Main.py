from Sucursales import * ;
from TiposCuenta import *;
from Auditorias import *;
from Clientes import *;
import os
#para prender este entorno virtual solo usa . venv/bin/activate en terminal
opc=0;
while opc != 5  :
    os.system("clear");
    opc=MenuPrincipal()
    match(opc):
     case 1 :
        MenuCuentas(); 
     case 2:
         MenuSurcusales();      
     case 3:
        MenuBeneficiarios(); 
     case 4:
        MenuAuditoria();
   


    
