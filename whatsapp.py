

import  pywhatkit

numCelular = input("Digite el número de celular con indicativo del pais (+57####): ")
mensaje = input("Digite ahora el  mensaje: ")
hora = int(input("Digite la hora: "))
minuto = int(input("Digite el minuto: "))
tiempodeespera = int(input("Digite el tiempo de espera: "))
segundosCierre = int(input("Digite los segundos de cierre: "))

cerrar=input("\nDesea cerrar la ventana de Whatsapp? : s / n ") 
if cerrar == "s": 
    pywhatkit.sendwhatmsg(numCelular,mensaje,hora,minuto,tiempodeespera,True,segundosCierre)
else:
    pywhatkit.sendwhatmsg(numCelular,mensaje,hora,minuto,tiempodeespera,False,segundosCierre)  


#Para enviar a grupos  KvKSQV6m9Eg4oSqTJVONRk
#id_grupo = input("Digite el id del grupo: ")

#pywhatkit.sendwhatmsg_to_group(id_grupo,mensaje,hora,minuto,tiempodeespera,False,segundosCierre)


