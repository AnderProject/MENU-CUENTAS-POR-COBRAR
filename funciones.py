import os

def borrarPantalla():
    os.system("cls")

def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")