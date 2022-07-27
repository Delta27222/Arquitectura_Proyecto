import os
import subprocess
import serial

puerto_Serial = serial.Serial(port='COM1',baudrate='1200', bytesize=8)

def run():
    while puerto_Serial.isOpen():
        port_info = puerto_Serial.read()

        print(port_info)
        if (port_info == b'1'):
            print('Opennig Notepad')
            os.system('Notepad')
        elif (port_info == b'2'):
            print('Opennig Opera')
            subprocess.call(r'C:\Users\Delta27222\AppData\Local\Programs\Opera GX\launcher.exe')
        elif (port_info == b'3'):
            print('Opennig Word')
            subprocess.call(r'C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE')
        elif (port_info == b'4'):
            print('Opennig Calculator')
            os.system("calc")
        else:
            print('No podemos abrir ninguna aplicacion, envie un dato correcto 😢')

        print('Hasta luego mi compañero 😉')


if __name__ == '__main__':
    run()