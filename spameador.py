import time 
import random
import pyautogui 


numero_de_mensajes = int(input("¿Cuántos mensajes desea enviar?:"))
mensaje_que_se_va_a_mandar = str(input("¿Qué mensaje desea enviar?:"))

print(f"Se enviarán {numero_de_mensajes} mensajes")
print(f"Se enviara el siguiente mensaje: {mensaje_que_se_va_a_mandar} ")
mensaje = str(input("¿Es correcto? SOLO y,n ?"))

while mensaje == "y":
 break
else:
 numero_de_mensajes = int(input("¿Cuántos mensajes desea enviar?:"))
 mensaje_que_se_va_a_mandar = str(input("¿Qué mensaje desea enviar?:"))
 print(f"Se enviarán {numero_de_mensajes} mensajes")
 print(f"Se enviara el siguiente mensaje: {mensaje_que_se_va_a_mandar} ")
 
print("Tiene 9 segundos para ir a la página donde se va a spamear al usuario :)")
print("Buena suerte :3")

time.sleep(14)
for k in range (0,numero_de_mensajes):
    pyautogui.typewrite(mensaje_que_se_va_a_mandar);pyautogui.press("enter")