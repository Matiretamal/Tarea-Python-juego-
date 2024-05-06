import random
import time
#Declarar Variables

decision=random.randint(1,3);
repetir=random.randint(1,3);
#Mensaje de bienvenida
print("   ::::::::::::::::::::::::::::::::::::::::::\n   ::: Bienvenido a la prueba de AMOR     :::\n   ::::::::::::::::::::::::::::::::::::::::::\n");

input("   ::::::::::::::::::::::::::::::::::::::::::\n   ::: Presione ENTER para continuar...   :::\n   ::::::::::::::::::::::::::::::::::::::::::\n");
#se inicia el programa con una decision random
#dependiendo de la desicion entra en uno de los ciclos 
if decision == 1:
    for i in range (repetir): #ciclo de repticion aleatorio 
        print("   :::  Me quiere mucho      (^-^)   :::::::: \n "), time.sleep(1);
        print("   :::  Me quiere poquito    (.-.)   :::::::: \n "), time.sleep(1);
        print("   :::  No me quiere nada    (._.)   :::::::: \n "), time.sleep(1);

if decision == 2:
    print("   :::  Me quiere mucho      (^-^)   :::::::: \n "), time.sleep(1);
    for i in range (repetir):
        print("   :::  Me quiere poquito    (.-.)   :::::::: \n "), time.sleep(1);
        print("   :::  No me quiere nada    (._.)   :::::::: \n "),  time.sleep(1);
        print("   :::  Me quiere mucho      (^-^)   :::::::: \n "), time.sleep(1);
if decision == 3:
    print("   :::  Me quiere mucho      (^-^)   :::::::: \n "), time.sleep(1); #time.sleep para dar un segundo de espera
    print("   :::  Me quiere poquito    (.-.)   :::::::: \n "), time.sleep(1);
    for i in range (repetir):
        print("   :::  No me quiere nada    (._.)   :::::::: \n "), time.sleep(1);
        print("   :::  Me quiere mucho      (^-^)   :::::::: \n "), time.sleep(1);
        print("   :::  Me quiere poquito    (.-.)   :::::::: \n "), time.sleep(1);
#dependiendo de la decision tomada se escoge una respuesta final 
#entrega de mensaje 
if decision == 1:
        print("   ::::::::::::::::::::::::::::::::::::::::::\n             TE QUIERE MUCH0      (*-*) \n   ::::::::::::::::::::::::::::::::::::::::::\n");
if decision == 2:
        print("   ::::::::::::::::::::::::::::::::::::::::::\n             TE QUIERE POQUITO    (u.u) \n   ::::::::::::::::::::::::::::::::::::::::::\n");
if decision == 3:
        print("   ::::::::::::::::::::::::::::::::::::::::::\n          LO SIENTO MUCHO     (u.u) \n"),time.sleep(1);
        print("             NO TE QUIERE       (x.x)\n   ::::::::::::::::::::::::::::::::::::::::::\n");