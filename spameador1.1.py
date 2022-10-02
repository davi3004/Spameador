import time 
import random
import pyautogui

numero_de_mensajes=int(input("¿Cuántos mensajes desea enviar?:"))


print(f"Se enviarán {numero_de_mensajes} mensajes")
print("Tiene 12 segundos para ir a la página donde se va a spamear al usuarioo :)")


mensajes_que_van_a_mandar = random.choice(["XD","Hola","ei","oie","bue","we"])


time.sleep(14)


for k in range (0,numero_de_mensajes):
    pyautogui.typewrite(mensajes_que_van_a_mandar);pyautogui.press("enter")
    
